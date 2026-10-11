# Fenârî Kataloğu Transkripsiyonu ile Veritabanının Karşılaştırması

**Karşılaştırılan kaynaklar**

- **Katalog:** *Kataloglar Transkripsiyon.docx* dosyasının “Fenârî Kataloğu Transkripsiyonu” kısmı (D.HMH.SFTH.d.21941-B). Hacıhasanzâde kataloğu bu karşılaştırmaya dahil edilmedi.
- **Veritabanı:** fatihkutuphanesi.com, *Fenarizade* kaynağı. Veri 11.10.2026'da API üzerinden çekildi.

Ayrıntılı tablo [`fenari_katalog_veritabani_karsilastirma.csv`](fenari_katalog_veritabani_karsilastirma.csv) dosyasındadır. Tabloda her kayıt için iki metin yan yana durur, kaydın durumu ve fark özeti verilir. Dosya Excel'de doğrudan açılır.

## Kısa cevap

Veritabanı kataloğu **büyük ölçüde birebir yansıtıyor**. Katalogdaki 1298 kaydın 1293'ü veritabanında var. Veritabanında katalogda karşılığı olmayan kayıt yok. Her kayıt kataloğun aynı varakında yer alıyor ve aynı vâkıfa bağlanmış. Metin farklarının çok büyük kısmı transkripsiyon tercihi ya da okuma farkıdır. Ancak aşağıda sıralanan **5 eksik kayıt** ve **yaklaşık 30 içerik farkı** düzeltilmeye değer.

| Durum | Kayıt | Oran |
|---|---:|---:|
| Metin aynı (noktalama, şapka ve dipnot işaretleri yok sayılınca) | 966 | %74,4 |
| Yalnızca biçimsel fark (*Kitâb-ı el-* ~ *Kitâbü'l-*, izafet *-i* vb.) | 114 | %8,8 |
| Küçük okuma ve yazım farkı (*Zehîra/Zahîra*, *Bekr/Bekir*, harekeler vb.) | 184 | %14,2 |
| İçerik farkı (eser adı, şahıs adı, eksik kelime, varak sayısı) | 29 | %2,2 |
| Veritabanında yok | 5 | %0,4 |
| **Toplam katalog kaydı** | **1298** | |

Yapısal kontroller:

- **Varak:** Eşleşen 1293 kaydın hepsi katalogdaki aynı varakta.
- **Vâkıf:** Katalogdaki 12 vâkıf bölümünün hepsi veritabanındaki vâkıf şahsıyla tutarlı. “Diğer âlimler” ve “zâyiʿ” bölümlerinde metinde geçen *Vakf-ı …* ibaresi de veritabanındaki vâkıfla örtüşüyor.
- **Bölüm toplamları:** Bölüm başlarındaki *Cümle/Cemʿan* sayıları, kataloğun kendi kayıt sayısıyla tutuyor. Toplam 796 sultânî + 41 bedel + 389 diğer vâkıflar + 15 = 1241 kitap. Buna 57 kayıp kitap kaydı eklenince 1298 eder.

## 1. Veritabanında eksik olan 5 kayıt

Eksiklerin hepsi XI. bölümdedir (*Eski defterde adı geçen, mevcut olmayan ancak zâyiʿ defterinde kayıtlı kitaplar*), 56b varağı. Bu bölümün 49 kaydından 44'ü veritabanına girilmiş. Bölümün son beş kaydı eksik:

| Katalog | Kayıt | Vâkıf |
|---|---|---|
| 56b [9] | *Cild-i evvel-i Kenz-i Şerh-i Îzâh*, 197 v. | Kâbilîzâde |
| 56b [10] | *Misbâh Şerhi*, 107 v. | Kâbilîzâde |
| 56b [11] | *Metn-i Şemsiyye*, mecmua tavrında, 27 v. | **Musannifek** |
| 56b [12] | *Fârisî Hikâyet*, kendi hattı ve telifi, ebter, 240 v. | **Musannifek** |
| 56b [13] | *Uʿcûbetü'l-Fetâvâ*, Farsça, kendi hattıyla, 269 v. | **Musannifek** |

Bu durum Musannifek listesini doğrudan etkiliyor. Kataloğa göre Musannifek'in Fenârî defterindeki vakıfları, mevcut 81 cilde ek olarak zâyiʿ kaydı düşülmüş bu **3 kitabı** da içeriyor. Bunların ikisi kendi telifi.

## 2. Numaralandırma farkları (19 kayıt)

Bu farklarda veritabanı doğru, transkripsiyon hatalı görünüyor:

- **Kâbilîzâde, Tefsir (36b–37a):** Transkripsiyonda **[5] numarası iki kez** kullanılmış. Bu yüzden ikinci [5]'ten (*Tefsîr-i Kebîr*, oysa doğrusu [6]) bölüm sonuna kadar her numara bir eksik kalıyor. Bölümün son kaydı katalogda [21], veritabanında [22]. Veritabanı numaraları düzeltilmiş hâliyle veriyor.
- **Hatîbzâde, Müteferrika (43a):** Varak değişince transkripsiyonda numaralandırma yeniden [1]'den başlamış. *Şerh-i Tezkire* kayıtları katalogda [1] ve [2], veritabanında [3] ve [4]. Bölüm 42b'de [1] ve [2] ile başladığı için doğrusu [3] ve [4]'tür.

## 3. Bölüm başlığı farkı (6 kayıt)

- **Âlâiyyeli Muhyiddîn, 48a–48b, [1]–[6]:** Katalogda *Tafsîlü Kütübi'l-Arabiyye* bölümünde olan altı kayıt, veritabanında *Tafsîlü Kütübi't-Tefâsîr* başlığıyla girilmiş. Bu kayıtlar Hâşiye-i Mutavvel, Şerh-i Miftâh, Mutavvel, Metn-i Miftâh ve Kâfiye-Misbâh-Avâmil'dir. Konuları belâgat ve nahiv olduğu için veritabanındaki başlık hatalı görünüyor.

Başlıklardaki diğer farklar yalnızca yazım farkıdır ve tutarsızlık sayılmaz. Örneğin katalogda sultânî bölümlerinin başlıklarında *mine'l-Evkāfi's-Sultâniyye* eki var, veritabanında yok; *Furûʿ* ve *Fürû‘* yazımları da değişiyor. Kayıp kitap bölümlerinin (X–XII) başlıkları veritabanında açıklayıcı ifadelerle verilmiş. VIII. (Mîşeved Acem) ve IX. (diğer âlimler) bölümlerinde katalogda ilim alt başlığı yok; bu bölümlerin 72 kaydı veritabanında “BAŞLIKSIZ” başlığıyla girilmiş, bu da katalogla tutarlı.

## 4. İçerik farkları (29 kayıt)

Her satırda önce katalog, sonra veritabanı okuması verilmiştir.

**a) Eser kimliğini etkileyenler**

| Varak/No | Katalog | Veritabanı |
|---|---|---|
| I, 17b [102] | *Kitâb-ı **Şerh-i** Câmiʿu's-Sagîr* | *Kitâb-ı Câmiʿu's-Sagîr* |
| I, 30a [49] | *Kitâb-ı **Şerh-i** Lübbü'l-Elbâb …* | *Kitâb-ı Lübbü'l-Elbâb …* |
| I, 15a [31], [32] | *Şerh-i **Mecmaʿ**-i Musannef* | *Şerh-i **Cemʿ**-i Musannef* |
| I, 22b [244] | *Kitâbü'd-**Diyât**'dan Kitâbü'l-**Meʿâkıle**'ye* | *Kitâbü'z-**Ziyât**'dan Kitâbü'l-**Muʿâkale**'ye* |
| II, 34b [7] | *Şerh-i **Nukāye*** | *Şerh-i **Nikāye*** |
| I, 12b [54] | *Şerh-i **Ahsîkesî*** | *Şerh-i **Ahsîketî*** |
| I, 32a [7] | Mecmua içeriği: *hâşiyetün uhrâ ale'ş-şerhi'l-**mezkûr*** | *Hâşiye uhrâ alâ li'ş-Şerh li'**z-Zukûr*** (veritabanındaki okuma bozuk görünüyor) |

**b) Varak sayısı**

| Varak/No | Katalog | Veritabanı |
|---|---|---|
| IV, 39a [22] *Mebsût* | İki yüz yirmi iki varak | İki yüz **yüz** yirmi iki varak (veritabanında “yüz” iki kez yazılmış) |

**c) Veritabanında eksik kalan kelimeler**

| Varak/No | Katalog | Veritabanı |
|---|---|---|
| VI, 46a [3] *Muhtasaru'l-Muntazam* (Musannifek) | *Saffâh'dan **sene** erbaʿ ve sebʿîn ve **hamsü**-miʾe senesinde* | *Saffâh'dan erbaʿ**a** ve sebʿîn ve **hamse**-miʾe senesinde* |
| XI, 54b [8] *Esbâb-ı Nüzûl* | *Ciğerî cildli. **Köhne.*** | “Köhne” yok |
| XI, 55a [21] *Şerh-i Manzûme-i Müntekā* | ***Cild-i evvel.** Mutavassıtu'l-hâl* | ***Evveli** mutavassıtu'l-hâl* |
| XII, 56b [2] *İhtiyâr* derkenarı | *Mevlânâ Seydî **Dede bin?** Mevlânâ Abdî'den* | *Mevlânâ Seydî **…?** Mevlânâ Abdî'den* |

**d) Şahıs adı okuması:** Katalogda *Muhammed*, veritabanında *Mehmed* (13 kayıt): I 12b [54], [58]; 16a [57]; 17a [89]; 18a [116]; 19b [155]; 20b [187]; 25b [319]; 27b [29]; 29b [31]; II 34b [4]; VII 48b [2]; IX 50b [1]; ayrıca V 41a [10] *İbrî* ~ *Abrî* ve I 8b [51] *Busutî* ~ *Bustî*.

**e) Arapça ibare ve gramer okuması:** I 6b [1] *صلاتها* ~ *صلوتها*; I 8a [34]; I 19b [160] *Risâleti Ali* ~ *Bir [Ri]sâle Ali*; I 20b [181] *Kitâbün manzûmun* ~ *Kitâb-ı manzûme*; II 35b [2]; VII 49a [12]. Katalog Arapça terkipleri iʿrâblı okumuş, veritabanı Türkçe izafetle okumuş. Bu tutarsızlık değil, okuma tercihidir.

## 5. Sistematik (biçimsel) farklar

Bu farklar içerik farkı sayılmadı. Yine de iki metni birebir eşitlemek istenirse bilinmesi gerekir:

- **Dipnot işaretleri:** Katalogda 74 kayıtta dipnot işareti var, örneğin *Seffâh'a[67]*. Veritabanında dipnot yok. Dipnotların içeriği de (ör. 171. dipnot: “Doğrusu Mahzenü'l-Esrâr olmalıdır”) veritabanına aktarılmamış.
- **Yazım:** Katalog *kâgıd* yazıyor, veritabanı *kâğıd*. Katalogda *Kitâb-ı el-X* biçimi, veritabanında *Kitâbü'l-X* biçimi kullanılıyor. Katalog *Buhârî-i Kirmânî* yazarken veritabanında izafet *-i* düşmüş. Ayrıca *Ebû Bekr* ~ *Ebî Bekir*, *Seffâh* ~ *Saffâh*, *Zehîra* ~ *Zahîra* gibi farklar var.
- **Derkenarlar:** Katalogda ayrı paragraf olarak duruyor, veritabanında aynı kaydın metnine “[Derkenar]” satırıyla eklenmiş. İçerik bakımından aynılar.

## Musannifek bölümü (VI) özelinde

- Kataloğun VI. bölümündeki **81 kaydın 81'i** veritabanında var. Varaklar (43a–46b), bölüm başlıkları ve numaralar birebir aynı.
- Metin karşılaştırması: 65 kayıt aynı, 7 kayıtta biçimsel fark, 8 kayıtta küçük okuma farkı, 1 kayıtta içerik farkı var.
  - **Küçük okuma farkları:** 43a [7] *havâşî* ~ *havâşîden*; 46a [11] *Zeynüddîn **Hâfî*** ~ ***Hâmî***; 46b [17] Arapça kasîde mısraı *وتمني* ~ *وتمنع*.
  - **İçerik farkı:** 46a [3]'teki tarih ibaresi (yukarıda 4c'de).
- Katalogda Musannifek'e ait olup veritabanında bulunmayan **3 zâyiʿ kitap** var (XI, 56b [11]–[13]; bkz. 1. bölüm).

## Yöntem

1. DOCX dosyası düz metne çevrildi. Kataloğun Fenârî kısmında vâkıf bölümleri (I–XII), ilim bölümleri ([A.], [B.] …), varak işaretleri ([43a] gibi) ve numaralı kayıtlar ayrıştırıldı. Derkenarlar ve ikinci paragrafa taşan kayıt devamları önceki kayda eklendi.
2. Veritabanındaki 1293 Fenarizade kaydı çekildi.
3. Eşleştirme metin benzerliğiyle yapıldı. Aynı varak ve aynı numara eşleşmeye ek puan verdi. Varak farkı en çok bir sayfa olabildi. Eşleşmeyen kayıtlar elle kontrol edildi.
4. Metinler karşılaştırılmadan önce şapkalar, ʿ ʾ işaretleri, noktalama ve dipnot işaretleri kaldırıldı ve *ğ/g* ile *ı/i* eşitlendi. Kalan farklar dört gruba ayrıldı: biçimsel, küçük okuma farkı, içerik farkı ve eksik kayıt. İçerik farkı sayılan 29 kaydın her biri tek tek okunarak doğrulandı.
