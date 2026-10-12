# Kayıt metninden temel kodikolojik alanları çıkaran okuyucu
import re,unicodedata
def strip(s):
    s=unicodedata.normalize("NFKD",s); return "".join(c for c in s if not unicodedata.combining(c))
def key(s): return strip((s or "").replace("ı","i").replace("İ","i")).lower().replace("ğ","g").replace("'","").replace("‘","").replace("ʿ","").strip()
NUM={"bir":1,"iki":2,"üç":3,"dört":4,"beş":5,"altı":6,"yedi":7,"sekiz":8,"dokuz":9,"on":10,"yirmi":20,"otuz":30,"kırk":40,"elli":50,"altmış":60,"yetmiş":70,"seksen":80,"doksan":90,"yüz":100,"bin":1000}
def words2num(ws):
    total=0;cur=0
    for w in ws:
        v=NUM.get(w)
        if v is None: return None
        if v==100: cur=(cur or 1)*100
        elif v==1000: total+=(cur or 1)*1000; cur=0
        else: cur+=v
    return total+cur or None
KAGIT={"dimesk":"Dimeşkî","dimesk":"Dimeşkî","semerkand":"Semerkandî","haseb":"Haşebî","sultan":"Sultanî","hind":"Hindî"}
EBAT={("tamam","a"):"Tamamına",("tamam","dan"):"Tamamından kırılmış",("nisf","a"):"Nısfına",("nisf","dan"):"Nısfından kırılmış",("rub","a"):"Rub'una",("rub","dan"):"Rub'undan kırılmış"}
RENK={"siyah":"siyah","siyâh":"siyah","beyâz":"beyaz","beyaz":"beyaz","nohûdî":"nohudî","nohudî":"nohudî","kırmız":"kırmızı"}
def cap(s): return s[:1].upper()+s[1:] if s else s
def extract(t):
    out={"kagit_turu":"","kagit_ebadi":"","kagit_sekli":"","aciklama":"","cild_turu":"","cild_materyal":"","varak_adedi":"","_notlar":[]}
    t1=(t or "").split("\n[Derkenar]")[0]
    # kâğıt türü + ebat
    kinds=set(re.findall(r"\b(Dimeşk|D[ıi]meşk|Semerkand|Haşeb|Sult[âa]n[îi] k|Hind[îi])",t1))
    if len({key(x)[:4] for x in kinds})>1: out["_notlar"].append("metinde birden fazla kâğıt türü geçiyor")
    m=re.search(r"\b(Dimeşk[īîi]|D[ıi]meşk[īîi]|Semerkand[îi]|Haşeb[îi]|Sult[âa]n[îi]|Hind[îi])\s+(?:k[âa][gğ][ıi]d\s+)?(tam[âa]m|n[ıi]sf|rub[ʿ‘']?)(?:ı|u)?(na|ndan|dan)?\b",t1)
    if m:
        k=key(m.group(1)); out["kagit_turu"]=next(v for kk,v in KAGIT.items() if k.startswith(kk))
        size=key(m.group(2)).rstrip("'"); size="rub" if size.startswith("rub") else ("nisf" if size.startswith("nisf") else "tamam")
        suf="dan" if (m.group(3) or "").endswith("dan") else "a"
        tail=t1[m.end():m.end()+25]
        if suf=="dan" and not re.match(r"\s*kırıl",tail): out["_notlar"].append("ebat: '…dan' ama 'kırılmış' yok")
        out["kagit_ebadi"]=EBAT[(size,suf)]
    if not out["kagit_turu"]:
        m2=re.search(r"\b(Dimeşk[īîi]|D[ıi]meşk[īîi]|Semerkand[îi]|Haşeb[îi])\b(?=\s*(?:\.|,|\[|üzere|k[âa][gğ][ıi]d))",t1)
        if m2: k=key(m2.group(1)); out["kagit_turu"]=next(v for kk,v in KAGIT.items() if k.startswith(kk))
    if re.search(r"\bk[üu]mm[îi]\b",t1,re.I): out["kagit_sekli"]="Kümmî"
    elif re.search(r"\bmukatta[ʿ‘']?\b",t1,re.I): out["kagit_sekli"]="Mukattaʿ"
    # cilt
    m=re.search(r"([^.,;:]*?)\bcild(?:li|le)\b",t1,re.I)
    if m:
        ws=m.group(1).strip().split()
        ws=[w for w in ws if w.lower() not in("ve",)]
        # sadece cilt ifadesine ait son kelimeler (en fazla 5)
        ws=ws[-5:]
        low=[w.lower() for w in ws]
        if any(w.startswith("mukavv") for w in low):
            i=next(i for i,w in enumerate(low) if w.startswith("mukavv"))
            pre=[w for w in low[:i] if not w.startswith("kâğıd") and not w.startswith("kâgıd") and w!="cedîd"]
            if any(w.startswith("kâğıd") or w.startswith("kâgıd") for w in low[:i]) and pre:
                out["cild_materyal"]=cap(" ".join(RENK.get(w,w) for w in pre)+" kağıt")
            out["cild_turu"]="Mukavva cilt"
        elif ws:
            out["cild_turu"]=cap(" ".join(RENK.get(w,w) for w in low)+" cilt")
    # varak
    tl=t1.replace("İ","i").replace("I","ı").lower()
    tl=re.sub(r"\[(\w+)\]",r"\1",tl).replace("va[ra]k","varak")
    tl=re.sub(r"[“\"][^”\"]*[”\"]",lambda x:" "*len(x.group(0)),tl)  # alıntıları (eski defter) yok say
    ms=list(re.finditer(r"((?:(?:bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi|otuz|kırk|elli|altmış|yetmiş|seksen|doksan|yüz|bin)\s+)+)(\??\s*)varak\b",tl))
    if len(ms)>1: out["_notlar"].append(f"metinde {len(ms)} varak sayısı var; sonuncusu alındı")
    m=ms[-1] if ms else None
    if m:
        ctx=tl[max(0,m.start()-12):m.end()+3]
        if "[" in ctx or "…" in ctx or "..." in ctx:
            out["_notlar"].append("varak sayısı metinde eksik/yıpranmış"); return out
        n=words2num(m.group(1).lower().split())
        if n: out["varak_adedi"]=str(n)
        if "?" in m.group(2): out["_notlar"].append("varak sayısı belirsiz (?)")
    return out
