import sys,json,re,unicodedata,collections,urllib.request,urllib.error; sys.path.insert(0,".")
import fk
DRY="--uygula" not in sys.argv
plan=json.load(open("../mustensih_plan.json"))
def n(s):
    s=(s or "").replace("ı","i").replace("İ","i").replace("’","'").replace("ʾ","").replace("ʿ","").replace("‘","")
    s=unicodedata.normalize("NFKD",s); s="".join(c for c in s if not unicodedata.combining(c)).lower()
    s=re.sub(r"\b(b\.|bin|ibn|ibni|b)\b","bin",s); s=re.sub(r"[\[\]\(\)?.,]","",s); return re.sub(r"\s+"," ",s).strip()
sah=fk.g("/sahislar/?page_size=10000"); sah=sah["results"] if isinstance(sah,dict) else sah
idx=collections.defaultdict(list)
for s in sah: idx[n(s["isim"])].append(s)
byid={s["id"]:s for s in sah}
jobs=[];problems=[]
for o in sorted(plan,key=lambda o:o["id"]):
    m=o["madde"]
    if m.startswith("X"): continue
    if m in("M4 Musannifek (tam)","M5 Musannifek (kısmi)"): jobs.append((o["id"],"id",11,m)); continue
    if m.startswith("M1"): jobs.append((o["id"],"id",o["eslesme"][0][0],m)); continue
    if m.startswith("M3") or m.startswith("M7"): jobs.append((o["id"],"id",o["secim"],m)); continue
    if m.startswith("M2"):
        ad=o["ad"]
        if re.search(r"\bb$|[?…]",ad) or len(ad.split())<2: problems.append((o["id"],m,f"ad şüpheli: {ad!r}")); continue
        jobs.append((o["id"],"ad",ad,m)); continue
    if m.startswith("M6"):
        if o.get("m6_secim"): jobs.append((o["id"],"id",o["m6_secim"],m)); continue
        if o["ad"]:
            hit=idx.get(n(o["ad"]),[])
            jobs.append((o["id"],"id",hit[0]["id"],m) if len(hit)==1 else (o["id"],"ad",o["ad"],m)); continue
        k=fk.g(f"/kayitlar/{o['id']}/"); ys=[b["yazar"] for b in k["kitap_set"] if b.get("yazar")]
        if len({y["id"] for y in ys})==1: jobs.append((o["id"],"id",ys[0]["id"],m))
        else: problems.append((o["id"],m,f"müellif kitapta kayıtlı değil ({len(ys)} yazar)"))
print("işlenecek:",len(jobs),collections.Counter(j[3][:2] for j in jobs),"| yeni ad:",len({n(j[2]) for j in jobs if j[1]=='ad'}),"| sorunlu:",len(problems))
for p in problems: print("  SORUNLU",p)
if DRY:
    for j in jobs[:6]: print("  örnek",j, byid.get(j[2],{}).get("isim") if j[1]=="id" else "(yeni)")
    sys.exit()
created={}
def get_or_create(ad):
    k=n(ad)
    if k in created: return created[k]
    hit=fk.g(f"/sahislar/?isim={urllib.parse.quote(ad)}&page_size=50"); hit=hit["results"] if isinstance(hit,dict) else hit
    hit=[h for h in hit if n(h["isim"])==k]
    if hit: created[k]=hit[0]; return hit[0]
    body={"isim":ad,"isim2":"","dogum_tarihi":"","dogum_tarihi_hijri":"","olum_tarihi":"","olum_tarihi_hijri":"","kaynak":"","kunye_bilgisi":"","link":""}
    c0=fk.counts()[0]
    r=urllib.request.urlopen(urllib.request.Request(fk.B+"/sahislar/",method="POST",data=json.dumps(body).encode(),headers=fk.H))
    hit=fk.g(f"/sahislar/?isim={urllib.parse.quote(ad)}&page_size=50"); hit=[h for h in (hit["results"] if isinstance(hit,dict) else hit) if n(h["isim"])==k]
    if fk.counts()[0]!=c0+1 or len(hit)!=1: raise SystemExit(f"DURDURULDU: şahıs oluşturma doğrulanamadı {ad!r}")
    json.dump(hit[0],open(f"{fk.YED}/sahis_{hit[0]['id']}_olusturuldu_{fk.stamp()}.json","w"),ensure_ascii=False,indent=1)
    created[k]=hit[0]; print(f"  yeni şahıs #{hit[0]['id']} {ad}",flush=True); return hit[0]
import urllib.parse
done=[]
for i,(rid,kind,val,m) in enumerate(jobs,1):
    s=get_or_create(val) if kind=="ad" else (byid.get(val) or fk.g(f"/sahislar/{val}/"))
    bk=fk.g(f"/kayitlar/{rid}/"); json.dump(bk,open(f"{fk.YED}/kayit_{rid}_{fk.stamp()}.json","w"),ensure_ascii=False,indent=1)
    if bk["mustensih"]: print(f"  atlandı #{rid}: müstensih artık dolu",flush=True); continue
    if not(bk["tur"] and bk["vakif"] and bk["kaynak"]): raise SystemExit(f"DURDURULDU #{rid}: tür/vâkıf/kaynak boş")
    body={"tam_metin":bk["tam_metin"],"bolum_basligi":bk["bolum_basligi"],"sayfa_numarasi":bk["sayfa_numarasi"],"vakif":fk.opt(bk["vakif"]),"vakif_new":False,
          "mustensih":fk.opt(s),"mustensih_new":False,"tur":{"value":bk["tur"],"label":bk["tur"]},"kaynak":fk.opt(bk["kaynak"]),"kaynak_new":False}
    s0=fk.ksum(bk); fk.patch(f"/kayitlar/{rid}/",body); s1=fk.ksum(fk.g(f"/kayitlar/{rid}/"))
    d={k for k in s0 if s0[k]!=s1[k]}
    if d!={"mustensih"} or s1["mustensih"]!=s["id"]: raise SystemExit(f"DURDURULDU #{rid}: beklenmeyen fark {d}")
    done.append((rid,s["id"],m))
    if i%50==0 or i==len(jobs): print(f"  {i}/{len(jobs)} işlendi | son #{rid}",flush=True)
json.dump(done,open("../mustensih_olusan.json","w"))
bad=[rid for rid,sid,_ in done if fk.idof(fk.g(f"/kayitlar/{rid}/")["mustensih"])!=sid]
print(f"SON KONTROL: {len(done)-len(bad)}/{len(done)} doğru {bad} | yeni şahıs: {len(created)} | şahıs/kaynak: {fk.counts()}",flush=True)
