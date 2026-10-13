import json,re
K={}
for s in json.load(open('kaynaklar_guncel.json'))['results']:
    for k in s['kayit_set']: K[k['id']]=k
fm={p['db_id']:p for p in json.load(open('match.json'))['pairs'] if p.get('db_id')}
hm={x['id']:x for x in json.load(open('hh_eslesme.json'))}
cf=json.load(open('cat.json'))['entries']; ch=json.load(open('cat_hh.json'))
E=json.load(open('eslesme_ham.json'))
src=lambda i:(K[i]['kaynak'] or {}).get('id')
def no_of(t):
    m=re.match(r'\s*\[(\d+)\]',t or ''); return int(m.group(1)) if m else None
def ref(i): return f"{K[i]['sayfa_numarasi']} [{no_of(K[i]['tam_metin'])}]" if no_of(K[i]['tam_metin']) else K[i]['sayfa_numarasi']
def cattext(i):
    if src(i)==2:
        p=fm.get(i); return (p or {}).get('cat_text'), (p or {}).get('vakif')
    x=hm.get(i)
    return (x or {}).get('cat'), None
# elle çözülenler (gerekçesi notta)
FORCE={'375':{'H':1435},'1289/M':{'F':3518},'2436':{'F':None,'H':1751},'285':{'H':None},'478':{'H':1515}}
NOTE={
 '305':"Listede Fenârî ref. “2a? [2]”; doğrusu 2b [2] (veritabanı nüshası ve ilişkili kayıt aynı yeri gösteriyor).",
 '2711':"Listede Fenârî ref. “2a [72]”; doğrusu 9a [72] (nüsha ve ilişkili kayıt tutarlı).",
 '2436':"ÇELİŞKİ: Listedeki ref. (FK 30b [64] / HK 35a [62]) Fatih 4828'e ait. Veritabanında Fatih 2436 nüshası Hacıhasanzâde 52b [87] (Fusûlü’l-İmâdî) kaydına bağlı; tabloda bu kayıt verildi. Listede “2436 tekrar istenecek” notu var.",
 '263':"Veritabanında Fatih 263 nüshası YOK. Listedeki ref. Fatih 2634 ile aynı; metinler bu ref.'e göre verildi. 263/2634 karışıklığı kontrol edilmeli.",
 '375':"Hacıhasanzâde 39b'de iki ayrı bölümde [2] var; ilişkili kayıt bağıyla Keşşâf olan seçildi.",
 '1289/M':"Fenârî 47a'da iki ayrı bölümde [3] var; nüsha bağıyla Hâşiye-i Şerh-i Adud olan seçildi.",
 '285':"ÇELİŞKİ: Listedeki HK ref. 73a [10] Fatih 2856'ya ait. Veritabanında Fatih 285 nüshası Fenârî 49b [3] (Tefsîr-i Sûre-i Yûsuf) kaydına bağlı; ilişkili Hacıhasanzâde kaydı listede notu düşülen 43b [98]. Tabloda bunlar verildi.",
 '478':"ÇELİŞKİ: Listedeki ref. 77b [24] Fatih 4786'ya ait. Veritabanında Fatih 478 nüshası Hacıhasanzâde 43a [82] (Tefsîru’l-Vasît, 2. cilt) kaydına bağlı; tabloda bu kayıt verildi.",
}
rows=[]
for r in E:
    f=r['fatih']; n=NOTE.get(f,'')
    pick={}
    for tag,kay in (('F',2),('H',1)):
        c=r[tag]['nusha_ids'] or (r[tag]['ref_ids'] if len(r[tag]['ref_ids'])==1 else [])
        pick[tag]=c[0] if c else None
    # karşı kaynağı ilişkili kayıttan tamamla
    for a,b in (('F','H'),('H','F')):
        if pick[a] and not pick[b] and K[pick[a]]['iliskili_kayit'] and f not in FORCE:
            pick[b]=K[pick[a]]['iliskili_kayit']
    pick.update(FORCE.get(f,{}))
    if f=='285': pick['H']=K[3570]['iliskili_kayit']
    checks=[]
    for tag in 'FH':
        rid=r[tag]['ref_ids']
        if pick[tag] and r['fk' if tag=='F' else 'hk'] and pick[tag] not in rid and f not in NOTE:
            checks.append(f"{'Fenârî' if tag=='F' else 'Hacıhasanzâde'} ref. listede {r['fk' if tag=='F' else 'hk']}, veritabanında {ref(pick[tag])}")
    if pick['F'] and pick['H'] and K[pick['F']]['iliskili_kayit']!=pick['H'] and K[pick['H']]['iliskili_kayit']!=pick['F']:
        checks.append("Fenârî ve Hacıhasanzâde kayıtları veritabanında birbirine ilişkili değil")
    nus=[h[0] for h in r['nusha']]
    how=[]
    if nus: how.append("nüsha kaydı ("+", ".join(nus)+")")
    else: how.append("nüsha kaydı yok")
    out=dict(sira=r['sira'],fatih=f)
    for tag in 'FH':
        i=pick[tag]
        if i:
            t,_=cattext(i)
            if not t:
                cr=[c for c in (cf if tag=='F' else ch) if c['page']==K[i]['sayfa_numarasi'] and c['no']==no_of(K[i]['tam_metin'])]
                t=cr[0]['text'] if len(cr)==1 else None
            out[tag]=dict(id=i,ref=ref(i),bolum=K[i]['bolum_basligi'],text=t,db=K[i]['tam_metin'],eksik=t is None)
        else: out[tag]=None
    out['yontem']="; ".join(how); out['not']="; ".join(x for x in [n,*checks,r['not_']] if x)
    rows.append(out)
json.dump(rows,open('tablo.json','w'),ensure_ascii=False,indent=1)
for o in rows:
    print(o['sira'],o['fatih'],'F',o['F'] and (o['F']['id'],o['F']['ref'],o['F']['eksik']),'H',o['H'] and (o['H']['id'],o['H']['ref'],o['H']['eksik']),'|',o['not'][:150])
