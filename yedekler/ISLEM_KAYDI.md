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
