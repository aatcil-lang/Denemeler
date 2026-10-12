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

def set_vakif(rid,sahis,metin_icermeli=None):
    """Boş vâkıf alanını verilen şahısla doldurur; yalnızca vâkıf değişmeli."""
    bk=g(f"/kayitlar/{rid}/"); json.dump(bk,open(f"{YED}/kayit_{rid}_{stamp()}.json","w"),ensure_ascii=False,indent=1)
    if bk["vakif"] is not None: raise SystemExit(f"DURDURULDU #{rid}: vâkıf artık boş değil ({bk['vakif']['isim']})")
    if not (bk["tur"] and bk["kaynak"]): raise SystemExit(f"DURDURULDU #{rid}: tür/kaynak boş")
    if metin_icermeli and not __import__("re").search(metin_icermeli,bk["tam_metin"]): raise SystemExit(f"DURDURULDU #{rid}: metinde beklenen ibare yok")
    v={"value":sahis["id"],"label":sahis["isim"]}
    if str(v["value"])==str(v["label"]): raise SystemExit("DURDURULDU: value==label")
    body={"tam_metin":bk["tam_metin"],"bolum_basligi":bk["bolum_basligi"],"sayfa_numarasi":bk["sayfa_numarasi"],"vakif":v,"vakif_new":False,
          "mustensih":opt(bk["mustensih"]),"mustensih_new":False,"tur":{"value":bk["tur"],"label":bk["tur"]},"kaynak":opt(bk["kaynak"]),"kaynak_new":False}
    s0=ksum(bk); patch(f"/kayitlar/{rid}/",body); s1=ksum(g(f"/kayitlar/{rid}/"))
    d={k for k in s0 if s0[k]!=s1[k]}
    if d!={"vakif"} or s1["vakif"]!=sahis["id"]: raise SystemExit(f"DURDURULDU #{rid}: beklenmeyen fark {d}")

def change_vakif(rid,from_id,sahis):
    """Vâkıfı from_id olan kaydı verilen şahsa geçirir; yalnızca vâkıf değişmeli."""
    bk=g(f"/kayitlar/{rid}/"); json.dump(bk,open(f"{YED}/kayit_{rid}_{stamp()}.json","w"),ensure_ascii=False,indent=1)
    cur=(bk["vakif"] or {}).get("id")
    if cur==sahis["id"]: return "zaten"
    if cur!=from_id: raise SystemExit(f"DURDURULDU #{rid}: vâkıf beklenen değil ({(bk['vakif'] or {}).get('isim')})")
    if not (bk["tur"] and bk["kaynak"]): raise SystemExit(f"DURDURULDU #{rid}: tür/kaynak boş")
    v={"value":sahis["id"],"label":sahis["isim"]}
    if str(v["value"])==str(v["label"]): raise SystemExit("DURDURULDU: value==label")
    body={"tam_metin":bk["tam_metin"],"bolum_basligi":bk["bolum_basligi"],"sayfa_numarasi":bk["sayfa_numarasi"],"vakif":v,"vakif_new":False,
          "mustensih":opt(bk["mustensih"]),"mustensih_new":False,"tur":{"value":bk["tur"],"label":bk["tur"]},"kaynak":opt(bk["kaynak"]),"kaynak_new":False}
    s0=ksum(bk); patch(f"/kayitlar/{rid}/",body); s1=ksum(g(f"/kayitlar/{rid}/"))
    d={k for k in s0 if s0[k]!=s1[k]}
    if d!={"vakif"} or s1["vakif"]!=sahis["id"]: raise SystemExit(f"DURDURULDU #{rid}: beklenmeyen fark {d}")
    return "değişti"

def create_kodik(rid,oneri):
    """Kodikolojik bilgisi olmayan kayda sitenin 'Bilgi Ekle' formuyla aynı yükle bilgi oluşturur."""
    import urllib.request
    bk=g(f"/kayitlar/{rid}/"); json.dump(bk,open(f"{YED}/kayit_{rid}_{stamp()}.json","w"),ensure_ascii=False,indent=1)
    if bk.get("kodikolojik_bilgi") or bk.get("bilgi_set"): return ("atlandı","zaten kodikolojik bilgisi var")
    if not (bk["tur"] and bk["vakif"] and bk["kaynak"]): raise SystemExit(f"DURDURULDU #{rid}: tür/vâkıf/kaynak boş")
    body={"id":"","hatt":[{"hatt_turu":"","hatt_sekli":"","aciklama":""}],"zahriye_exists":False,"zahriye":"",
          "kagit_turu":oneri["kagit_turu"],"aciklama":"","kagit_ebadi":oneri["kagit_ebadi"],"kagit_sekli":oneri["kagit_sekli"],
          "murekkep_count":1,"murekkep":[{"renk":"","ilgili_ibare":""}],"cedvel_exists":False,"cedvel":"",
          "cild_turu":oneri["cild_turu"],"cild_materyal":oneri["cild_materyal"],"varak_adedi":oneri["varak_adedi"],"note":"",
          "kayit":rid,"tam_metin":bk["tam_metin"]}
    s0=ksum(bk)
    r=urllib.request.urlopen(urllib.request.Request(B+"/kodikolojikbilgiler/",method="POST",data=json.dumps(body).encode(),headers=H))
    if r.status>=300: raise SystemExit(f"DURDURULDU #{rid}: HTTP {r.status}")
    a=g(f"/kayitlar/{rid}/"); s1=ksum(a)
    d={k for k in s0 if s0[k]!=s1[k]}
    if not d<= {"kodik","bilgiler"} or not s1["bilgiler"]: raise SystemExit(f"DURDURULDU #{rid}: kayıtta beklenmeyen fark {d} / bilgiler {s1['bilgiler']}")
    bid=s1["bilgiler"][0]; b=g(f"/kodikolojikbilgiler/{bid}/")
    F=["kagit_turu","kagit_ebadi","kagit_sekli","cild_turu","cild_materyal","varak_adedi"]
    bad={f:(oneri[f],b.get(f)) for f in F if (oneri[f] or "")!=(b.get(f) or "")}
    if bad: raise SystemExit(f"DURDURULDU #{rid}: kodikolojik alanlar beklenenden farklı {bad}")
    return ("oluşturuldu",bid,d)
