# Veritabanı İşlem Kaydı

## 11.10.2026 — A2: kayıt #3545, bölüm başlığı
- **Değişiklik:** `bolum_basligi`: “Tafsîlü Kütübi’t-Tefâsîr” → “Tafsîlü Kütübi’l-Arabiyye”
- **Yedek:** `kayit_3545_20261011T220310Z.json` (değişiklikten önceki hâl)
- **Olay:** İlk istekte yalnızca `bolum_basligi` gönderildi. Sunucunun güncelleme kodu (`defter/viewsets.py`, `KayitViewset.update`) istekte bulunmayan `tur`, `vakif` ve `kaynak` alanlarını boşalttı. Kayıt yaklaşık 2 dakika boyunca türsüz, vâkıfsız ve kaynaksız kaldı.
- **Geri yükleme:** Sitenin kendi düzenleme formunun gönderdiği biçimle bütün alanlar yedekten yeniden gönderildi. Yeni şahıs kaydı oluşmadı (şahıs sayısı 718'de kaldı). İlişkili kayıt #1876 ve kitap kaydı #3526 değişmedi.
- **Son durum:** Kayıt, yedekle bölüm başlığı dışında aynı.

## Bundan sonraki işlemler için kural
Kayıt güncellemeleri **her zaman tam form yüküyle** gönderilmeli:
`tam_metin`, `bolum_basligi`, `sayfa_numarasi`, `vakif` {value,label}, `vakif_new`: false, `mustensih` {value,label} veya null, `mustensih_new`: false, `tur` {value,label}, `kaynak` {value,label}, `kaynak_new`: false.
`value` ile `label` aynı olursa sunucu yeni şahıs veya kaynak oluşturuyor; bu yüzden bu ikisinin farklı olduğu her seferinde kontrol edilmeli.

Not: Sitenin kendi “ilişkilendir” düğmesi yalnızca `iliskili_kayit` gönderiyor. Aynı hata yüzünden bu düğme de tür, vâkıf ve kaynak alanlarını boşaltıyor olabilir. Site geliştiricisine bildirilmeli.

## 11.10.2026 — A3–A7: kayıtlar #3546–#3550, bölüm başlığı
- **Değişiklik:** Her kayıtta `bolum_basligi`: “Tafsîlü Kütübi’t-Tefâsîr” → “Tafsîlü Kütübi’l-Arabiyye” (Âlâiyyeli Muhyiddîn, 48a [2] – 48b [6])
- **Yöntem:** Her kayıt önce yedeklendi (`kayit_<id>_<zaman>.json`). Mevcut değerler kontrol edildikten sonra tam form yükü gönderildi.
- **Doğrulama:** Her kayıtta değişen tek alan bölüm başlığı. Kontrol edilen alanlar: tür, vâkıf, kaynak, müstensih, metin, varak, ilişkili kayıt, kitap, nüsha ve kodikolojik bağlantılar. Şahıs sayısı (718) ve kaynak sayısı (3) değişmedi.

## 11.10.2026 — A1: kayıt #3279, varak sayısı yazımı
- **Değişiklik:** `tam_metin` içinde “İki yüz yüz yirmi iki varak.” → “İki yüz yirmi iki varak.” (Kâbilîzâde, 39a [22] *Mebsût*)
- **Doğrulama:** Değişen tek alan `tam_metin`. Tür, vâkıf (#9), kaynak (#2) ve diğer bağlantılar aynı kaldı. Kodikolojik bilgideki varak adedi zaten 222'ydi. Şahıs sayısı 718'de kaldı.

## 11.10.2026 — A8: kayıt #3656 ve kitap #3635, “Köhne” eklendi
- **Kayıt metni:** “Ciğerî cildli. Esbâb-ı Nüzûl…” → “Ciğerî cildli. **Köhne.** Esbâb-ı Nüzûl…” (XI, 54b [8])
- **Kitap adı (#3635):** “…cigerî cildli, Esbâb-ı Nüzûl-i Kur’ân…” → “…cigerî cildli, **köhne**, Esbâb-ı Nüzûl-i Kur’ân…” (alandaki mevcut küçük harf ve virgül düzeni korundu)
- **Yöntem:** Kitap güncellemesi sitenin kitap formuyla aynı yapıda gönderildi (`isim`, `disiplin`, `kapsam`, `yazar`, `kayit`, `kaynak` için `{value, label}` biçimi).
- **Doğrulama:**
  - Kayıtta yalnızca `tam_metin` değişti.
  - Kitapta yalnızca `isim` değişti; `isim2`, `disiplin`, `kapsam`, `yazar`, `kayit` ve `kaynak` aynı kaldı.
  - Kitap güncellemesi kayıt kaydını etkilemedi.
  - Şahıs sayısı 718'de, kaynak sayısı 3'te kaldı.

## 11.10.2026 — B1, B2 (seçenek b: yazmadaki okuma korunur, katalogdaki düzeltme köşeli parantezle eklenir)
- **B1, kayıt #2881** (I, 22b [244] *Mebsût*), metin: “Kitâbü’z-Ziyât’dan … Kitâbü’l-Muʿâkale’ye” → “Kitâbü’z-Ziyât **[Diyât]**’dan … Kitâbü’l-Muʿâkale **[Meʿâkıle]**’ye”. Dayanak: katalog, 34. dipnot.
- **B2, kayıt #2604** (I, 12b [54]), metin: “Şerh-i Ahsîketî min…” → “Şerh-i Ahsîketî **[Ahsîkesî]** min…”. Dayanak: katalog, 28. dipnot.
- **B2, kitap #2587**, eser adı: “Kitâb-ı Şerh-i Ahsiketî.” → “Kitâb-ı Şerh-i Ahsiketî **[Ahsîkesî]**.”
- **Doğrulama:**
  - Kayıtlarda yalnızca `tam_metin` değişti, kitapta yalnızca `isim` değişti.
  - Kitap güncellemesi kayıt kaydını etkilemedi.
  - Şahıs sayısı 718'de, kaynak sayısı 3'te kaldı.
- **Araç:** Bundan sonraki işlemler aynı denetimleri yapan `fk.py` yardımcısıyla yapılıyor: yedek alma, değiştirilecek ifadenin tam bir kez geçtiğini kontrol etme, tam form yükü gönderme, alan alan doğrulama.

## 11.10.2026 — C1–C11 (seçenek a: katalog okuması yazıldı)
Her maddede yalnızca listelenen fark değiştirildi. İşlemden önce kuru çalıştırma yapıldı: değiştirilecek her ifadenin güncel kayıtta tam bir kez geçtiği, kitabın doğru kayda bağlı olduğu ve tür, vâkıf ve kaynak bilgilerinin dolu olduğu kontrol edildi.

| Madde | Kayıt / Kitap | Önce | Sonra |
|---|---|---|---|
| C1 | #2739 / #2722 | Kitâb-ı Câmiʿu’s-Sagīr | Kitâb-ı **Şerh-i** Câmiʿu’s-Sagīr |
| C2 | #3076 / #3058 | Kitâb-ı Lübbü’l-Elbâb | Kitâb-ı **Şerh-i** Lübbü’l-Elbâb |
| C3 | #2668 / #2651 | Şerh-i Cemʿ-i Musannef | Şerh-i **Mecmaʿ**-i Musannef |
| C4 | #2669 / #2652 | Şerh-i Cemʿ-i Musannef | Şerh-i **Mecmaʿ**-i Musannef |
| C5 | #3174 / #3156 | Metn-i Nikāye (kitapta: Nikāye [Nukāye]) | Metn-i **Nukāye** |
| C6 | #3488 (Musannifek) | Saffâh’dan erbaʿa ve sebʿîn ve hamse-miʾe | Saffâh’dan **sene erbaʿ** ve sebʿîn ve **hamsü**-miʾe |
| C7 | #3669 / #3648 | Evveli mutavassıtu’l-hâl | **Cild-i evvel.** mutavassıtu’l-hâl |
| C8 | #3694 (derkenar) | Mevlânâ Seydî …? Mevlânâ Abdî | Mevlânâ Seydî **Dede bin?** Mevlânâ Abdî |
| C9 | #3337 / #3319 | Tavâliʿ-i Abrî | Tavâliʿ-i **İbrî** |
| C10 | #2497 | ve’l-Busti bâbına | ve’l-**Busuti** bâbına |
| C11 | #3123 / #3105 | Hâşiye uhrâ alâ li’ş-Şerh li’z-Zukûr | **hâşiyetün uhra ale’ş-şerhi’l-mezkûr** |

**Doğrulama:**
- Kayıtlarda yalnızca `tam_metin`, kitaplarda yalnızca `isim` değişti.
- Kitap güncellemeleri bağlı kayıtları etkilemedi.
- Şahıs sayısı 718'de, kaynak sayısı 3'te kaldı.

**Not:** C11 mecmuasında, listelenmeyen başka bozukluklar da sürüyor (ör. “Seyyid Ali **alâ** ve Havâşî”).

## 11.10.2026 — V1–V5: Hacıhasanzade'de vâkıfı boş 114 kayda vâkıf atandı
Dayanak: katalogdaki “Vakf-ı …” ibaresi (Halebîzâde için katalog bölümü) ve veritabanında aynı ibareyi taşıyan kayıtlardaki mevcut kullanım. Ayrıntılar `vakif_onay_listesi.md` ve `vakif_eksikleri.csv` dosyalarında.

| Madde | Kayıt | Vâkıf | Şahsın vâkıf sayısı |
|---|---:|---|---|
| V1 | 92 | Kādızâde (#434) | 45 → 137 |
| V2 | 11 | Mevlânâ Kâbilîzâde (#9) | 172 → 183 |
| V3 | 7 | Mevlânâ Hatîbzâde (#10) | 156 → 163 |
| V4 | 3 | Mevlânâ Musannifek (#11) | 160 → 163 |
| V5 | 1 (#2045) | Halebîzâde (#741) | 17 → 18 |

- **Denetimler:** Her kayıt önce yedeklendi. İşlemden önce vâkıfın hâlâ boş olduğu ve kaydın kendi metninde beklenen ibarenin geçtiği kontrol edildi. İşlemden sonra yalnızca vâkıf alanının değiştiği doğrulandı.
- **Durma:** 56. kayıtta (#1742) işlem durdu, çünkü metinde ibare “Kâdızâde” (â ile) yazılmıştı. Kayıt elle incelendi. Denetim bu yazım biçimini de kabul edecek şekilde genişletildi ve kalan kayıtlarla devam edildi.
- **Son kontrol:** 114 kaydın 114'ü doğru. Tür ve kaynak bilgileri dolu. Şahıs sayısı 718'de, kaynak sayısı 3'te kaldı.

## 11.10.2026 — V9: Şeyhzâde ve Halebîzâde bölümlerindeki 358 kaydın vâkıfı II. Mehmed'den katalogdaki vâkıfa geçirildi
- **Karar:** Kullanıcı, kayıtların katalogdaki vâkıfa bağlanmasını istedi. Dayanak, katalog bölüm başlıkları: *“Tafsîlü Kütübi Mevlânâ el-Meşhûr bi-Şeyhzâde / bi-Halebîzâde elletî vakafehâ…”*
- **Kapsam:**
  - Katalogun IV. bölümü (Şeyhzâde): 43 kayıt, Mevlânâ el-meşhûr bi-Şeyhzâde (#570) şahsına bağlandı.
  - Katalogun V. bölümü (Halebîzâde): 315 kayıt, Halebîzâde (#741) şahsına bağlandı.
  - Değişen kayıtlar 63b–83a varakları arasında. Bu aralıkta başka bir vâkıf bölümü yok.
- **Ön denetim:** Metninde “Vakf” geçen 6 kaydın hepsinde bu kelime *Kitâbü’l-Vakf* bölüm adı olarak geçiyor; vâkıf bildirmiyor. Eşleşmesi zayıf çıkan 3 kayıt elle kontrol edildi.
- **İşlem denetimi:** Her kayıt önce yedeklendi. İşlemden önce vâkıfın II. Mehmed (#1) olduğu doğrulandı. İşlemden sonra yalnızca vâkıf alanının değiştiği doğrulandı.
- **Son kontrol:** 358 kaydın 358'i doğru.
- **Şahısların vâkıf sayıları:**
  - Şeyhzâde: 1 → **44**. Katalogdaki bölüm toplamı 44, birebir aynı.
  - Halebîzâde: 18 → **333**. Katalogdaki bölüm toplamı 333, birebir aynı.
  - II. Mehmed: 2044 → 1686.
- Şahıs sayısı 718'de, kaynak sayısı 3'te kaldı.

## 12.10.2026 — V6, V7: iki yeni şahıs kaydı açıldı, 7 kayda vâkıf atandı
- **Sorun:** Sitenin şahıs ekleme ucu (`POST /api/sahislar/`) çalışmıyor. `defter/viewsets.py` (satır ~468) `Sahis.objects.create(...)` çağrısına `dogum_tarihi_hicri` ve `olum_tarihi_hicri` adlarını gönderiyor, oysa modeldeki alanlar `..._hijri`. Sonuç: *“Sahis() got unexpected keyword arguments”* hatası (HTTP 500). İki deneme yapıldı, ikisinde de kayıt oluşmadı; şahıs sayısı 718'de kaldı. **Site geliştiricisine bildirilmeli:** sitenin “Şahıs Ekle” formu da bu yüzden çalışmıyor olmalı.
- **Kullanılan yol:** Yeni şahıslar, kayıt düzenleme formundaki “yeni vâkıf” seçeneğiyle açıldı (`vakif` = `{value: ad, label: ad}`, `vakif_new: true`). Bu, sitenin kendi arayüzünün kullandığı yol. Her gruptaki ilk kayıtta yeni şahıs açıldı, kalan kayıtlar yeni şahsın numarasıyla bağlandı.
- **V6:** Yeni şahıs **#768 “Bâzergânzâde”**. 5 kayıt bu şahsa bağlandı: #1507–#1511 (42b [74] – 43a [78]).
- **V7:** Yeni şahıs **#769 “Mevlânâ Kāsım bin Hasan el-Karamânî”**. 2 kayıt bu şahsa bağlandı: #1480 ve #1481 (41b [47]–[48]).
- **Doğrulama:**
  - Her kayıtta yalnızca vâkıf alanı değişti.
  - Şahıs sayısı her adımda tam 1 arttı (718 → 720); kaynak sayısı 3'te kaldı.
  - Son kontrol: 7 kaydın 7'si doğru.
  - Yeni şahısların vâkıf sayıları beklenen değerlerde (5 ve 2).

## 12.10.2026 — Kadızâde kayıtlarının ayrılması
- **Karar (kullanıcı):** #434 yalnızca vâkıf Kadızâde olarak kalacak. Müellif Kadızâde-i Rûmî ayrı bir şahıs olacak. Bunun için yeni kayıt açılmadı; yalnızca müellif olarak kullanılan #564 yeniden adlandırıldı.
- **Şahıs #564**, ad: “Kâdızâde” → **“Kādızâde-i Rûmî”**. Sitenin şahıs düzenleme formuyla aynı yük gönderildi. Değişen tek alan `isim`. İkinci ad, tarihler, kaynak ve vâkıf/müstensih/yazar bağlantıları aynı kaldı.
- **Kitap #1410** (*Kitâb-ı Şerhu Çağmînî*, kayıt #1415, 38a [15]), yazar: #434 → **#564**. Değişen tek alan `yazar`. Bağlı kayıt #1415 değişmedi.
- **Son durum:**
  - #434 Kādızâde: vâkıf 137, yazar 0.
  - #564 Kādızâde-i Rûmî: yazar 4 (Şerh-i Çağmînî, Şerhü’l-Çağmînî, Şerhu Eşkâli’t-Teʾsîs, Havâşî Şerhi Eşkâli’t-Teʾsîs), vâkıf 0.
  - Şahıs sayısı 720'de, kaynak sayısı 3'te kaldı.

## 12.10.2026 — Geliştirici düzeltmelerinin doğrulanması
- **3. madde (DEBUG):** Düzelmiş. 404 sayfaları artık sade “Not Found” döndürüyor; URL listesi ve kod gösterilmiyor.
- **5. madde:** Düzelmiş. `OPTIONS` istekleri 200 dönüyor. `page_size=5000` isteği 200 dönüyor; yanıt 1000 kayıtla sınırlanmış ve 13 saniye sürdü.
- **4. madde (filtre):** Düzelmiş. Arayüz artık `/api/sahislar/?isim=…&rol=…` adresini kullanıyor.
  - “kadizade”, “kadızâde” ve “Kādızâde” aramalarının üçü de `rol=vakif` ile yalnızca #434'ü getiriyor.
  - Aynı arama `rol=yazar` ile yalnızca #564'ü getiriyor.
- **1. madde (güncellemenin alan silmesi):** Düzelmiş.
  - Test: #3545'e yalnızca `bolum_basligi` mevcut değeriyle gönderildi. Hiçbir alan değişmedi; tür, vâkıf ve kaynak korundu.
  - Düz kimlik numarasıyla (`{"vakif": 12}`) gönderilen istek de artık 200 dönüyor ve hiçbir şey değişmiyor.
  - Test öncesi yedek: `kayit_3545_*_test.json`.
- **2. madde (Şahıs Ekle):** Test edilmedi. Test, veritabanında deneme amaçlı bir şahıs kaydı oluşturmayı gerektiriyor.

## 12.10.2026 — Kodikolojik bilgiler: deneme kaydı
- **Okuyucu:** `araclar/kodik_extract.py`. Elle doldurulmuş yaklaşık 1570 kayıtta doğrulandı. Önerinin girilmiş değerle aynı çıkma oranı: kâğıt türü %99,3, varak %99,2, cilt türü %98,4, cilt malzemesi %97,7, kâğıt ebadı %94,9.
- **Kullanıcı onayı:** 30 kayıtlık pilot tablo (`kodikolojik_pilot.csv`) uygun bulundu.
- **Deneme:** Kayıt #1064 için kodikolojik bilgi **#1603** oluşturuldu (Dimeşkî / Tamamına / Mukavva cilt / Yeşil kağıt / 371 varak).
  - Yük, sitenin “Bilgi Ekle” formuyla aynı; mürekkep ve hat için birer boş satır gönderildi.
  - Sunucu başarılı istekte boş yanıt dönüyor. Bu yüzden oluşan kayıt, ana kayıt üzerinden okunarak doğrulandı.
- **Doğrulama:**
  - Tek kopya oluştu; toplam kodikolojik kayıt sayısı 1573 → 1574.
  - Ana kayıtta yalnızca kodikolojik bilgi bağlantısı değişti.
