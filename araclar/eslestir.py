import json,re,collections
from yazma_listesi import L
nus=json.load(open('nushalar.json'))
K={}
for s in json.load(open('kaynaklar_guncel.json'))['results']:
    for k in s['kayit_set']: K[k['id']]=k
fm={p['db_id']:p for p in json.load(open('match.json'))['pairs'] if p.get('db_id')}
hm={x['id']:x for x in json.load(open('hh_eslesme.json'))}
cf=json.load(open('cat.json'))['entries']; ch=json.load(open('cat_hh.json'))
def key(s):
    m=re.match(r'\s*0*(\d+)\s*(M)?',s or '')
    return (int(m.group(1)),'M' if m.group(2) else '') if m else None
byno=collections.defaultdict(list)
for n in nus:
    if (n['koleksiyon'] or {}).get('isim')=='Fatih' and n['kayit']:
        byno[key(n['koleksiyon_numarasi'])].append((n['koleksiyon_numarasi'],n['kayit']['id'],n['kayit']['kaynak']))
def no_of(t):
    m=re.match(r'\s*\[(\d+)\]',t or ''); return int(m.group(1)) if m else None
def dbref(kaynak,page,no):
    return [k['id'] for k in K.values() if (k['kaynak'] or {}).get('id')==kaynak and (k['sayfa_numarasi'] or '').strip()==page and no_of(k['tam_metin'])==no]
def catref(cat,page,no): return [c for c in cat if c['page']==page and c['no']==no]
out=[]
for lab,fno,fk,hk,note in L:
    k=key(fno.replace('/',''))
    hits=byno.get(k,[])
    if k[1]=='' : hits=[h for h in hits]
    r=dict(sira=lab,fatih=fno,fk=fk,hk=hk,not_=note,nusha=hits)
    for tag,kay,ref,cat,mp in (('F',2,fk,cf,fm),('H',1,hk,ch,hm)):
        nids=[h[1] for h in hits if h[2]==kay]
        rids=dbref(kay,ref[0],ref[1]) if ref else []
        crs=catref(cat,ref[0],ref[1]) if ref else []
        r[tag]=dict(nusha_ids=nids,ref_ids=rids,cat=[((c['vakif'] or '')[:40],(c['bolum'] or '')[:40],c['text']) for c in crs],
                    nusha_cat=[(i,K[i]['sayfa_numarasi'],(mp.get(i) or {}).get('cat_text') or (mp.get(i) or {}).get('cat')) for i in nids])
    out.append(r)
json.dump(out,open('eslesme_ham.json','w'),ensure_ascii=False,indent=1)
for r in out:
    F,Hh=r['F'],r['H']
    print(r['sira'],r['fatih'],'nüsha:',[h[0] for h in r['nusha']],'| F n',F['nusha_ids'],'ref',F['ref_ids'],'cat',len(F['cat']),'| H n',Hh['nusha_ids'],'ref',Hh['ref_ids'],'cat',len(Hh['cat']))
