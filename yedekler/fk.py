# Fatih kütüphanesi API: güvenli kayıt/kitap güncelleme yardımcıları
import json,os,urllib.request,urllib.error,datetime,sys
B="https://backend.fatihkutuphanesi.com/api"
YED="/home/user/Denemeler/yedekler"
def token():
    r=urllib.request.Request(B+"/token/",data=json.dumps({"username":os.environ["FATIH_KULLANICI"],"password":os.environ["FATIH_SIFRE"]}).encode(),headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r))["access"]
H={"Authorization":"Bearer "+token(),"Content-Type":"application/json"}
def g(u): return json.load(urllib.request.urlopen(urllib.request.Request(B+u,headers=H)))
def patch(u,body): return urllib.request.urlopen(urllib.request.Request(B+u,method="PATCH",data=json.dumps(body).encode(),headers=H))
idof=lambda v: v.get("id") if isinstance(v,dict) else v
def ksum(x):
    return dict(tam_metin=x["tam_metin"],bolum=x["bolum_basligi"],sayfa=x["sayfa_numarasi"],notlar=x["notlar"],tur=x["tur"],
        vakif=idof(x["vakif"]),mustensih=idof(x["mustensih"]),kaynak=idof(x["kaynak"]),iliskili=idof(x["iliskili_kayit"]),
        kodik=idof(x.get("kodikolojik_bilgi")),kitaplar=sorted(k["id"] for k in x["kitap_set"]),
        bilgiler=sorted(b["id"] for b in x.get("bilgi_set") or []),nushalar=sorted(n["id"] for n in x.get("nusha_set") or []))
def bsum(x): return dict(isim=x["isim"],isim2=x["isim2"],disiplin=x["disiplin"],kapsam=x["kapsam"],yazar=idof(x["yazar"]),kayit=idof(x["kayit"]),kaynak=idof(x["kaynak"]))
def opt(o):
    if not o: return None
    d={"value":o["id"],"label":o["isim"]}
    if str(d["value"])==str(d["label"]): raise SystemExit("DURDURULDU: value==label")
    return d
def stamp(): return datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
def counts(): return g("/sahislar/?page_size=1")["count"],g("/kaynaklar/?page_size=1")["count"]
def fix_kayit(rid,repl):
    bk=g(f"/kayitlar/{rid}/"); json.dump(bk,open(f"{YED}/kayit_{rid}_{stamp()}.json","w"),ensure_ascii=False,indent=1)
    t=bk["tam_metin"]
    for o,n in repl:
        if t.count(o)!=1: raise SystemExit(f"DURDURULDU #{rid}: «{o}» {t.count(o)} kez geçiyor")
        t=t.replace(o,n)
    if not(bk["tur"] and bk["vakif"] and bk["kaynak"]): raise SystemExit(f"DURDURULDU #{rid}: tür/vâkıf/kaynak boş")
    body={"tam_metin":t,"bolum_basligi":bk["bolum_basligi"],"sayfa_numarasi":bk["sayfa_numarasi"],"vakif":opt(bk["vakif"]),"vakif_new":False,
          "mustensih":opt(bk["mustensih"]),"mustensih_new":False,"tur":{"value":bk["tur"],"label":bk["tur"]},"kaynak":opt(bk["kaynak"]),"kaynak_new":False}
    s0=ksum(bk); patch(f"/kayitlar/{rid}/",body); a=g(f"/kayitlar/{rid}/"); s1=ksum(a)
    d={k for k in s0 if s0[k]!=s1[k]}
    if d!={"tam_metin"} or s1["tam_metin"]!=t: raise SystemExit(f"DURDURULDU #{rid}: beklenmeyen fark {d}")
    print(f"KAYIT #{rid} ✓\n  önce : {bk['tam_metin'].splitlines()[0]}\n  sonra: {t.splitlines()[0]}")
    return a
def fix_kitap(kid,repl):
    kb=g(f"/kitaplar/{kid}/"); json.dump(kb,open(f"{YED}/kitap_{kid}_{stamp()}.json","w"),ensure_ascii=False,indent=1)
    if kb["kaynak"] is not None: raise SystemExit(f"DURDURULDU kitap #{kid}: kaynak dolu, künye alanları ayrıca ele alınmalı")
    i=kb["isim"]
    for o,n in repl:
        if i.count(o)!=1: raise SystemExit(f"DURDURULDU kitap #{kid}: «{o}» {i.count(o)} kez")
        i=i.replace(o,n)
    kay=g(f"/kayitlar/{idof(kb['kayit'])}/") if kb["kayit"] else None
    body={"isim":{"value":i,"label":i},"isim2":kb["isim2"],"disiplin":{"value":kb["disiplin"],"label":kb["disiplin"]},"kapsam":{"value":kb["kapsam"],"label":kb["kapsam"]},
          "yazar":opt(kb["yazar"]),"yazar_new":False,"kayit":{"value":kay["id"],"label":kay["tam_metin"]} if kay else None,"kaynak":None,"kaynak_new":False,"kunye_bilgisi":"","link":""}
    b0=bsum(kb); k0=ksum(kay) if kay else None
    patch(f"/kitaplar/{kid}/",body); b1=bsum(g(f"/kitaplar/{kid}/"))
    d={k for k in b0 if b0[k]!=b1[k]}
    if d!={"isim"} or b1["isim"]!=i: raise SystemExit(f"DURDURULDU kitap #{kid}: beklenmeyen fark {d}")
    if kay and ksum(g(f"/kayitlar/{kay['id']}/"))!=k0: raise SystemExit(f"DURDURULDU: kitap güncellemesi kayıt #{kay['id']}'i değiştirdi")
    print(f"KİTAP #{kid} ✓ (yazar: {(kb['yazar'] or {}).get('isim')})\n  önce : {kb['isim']}\n  sonra: {i}")
