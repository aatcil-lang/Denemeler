# Müstensih Eksikleri: Onay Listesi

**Kapsam:** Fenarizade ve Hacıhasanzade kayıtları içinde, metninde “hatt” geçen ama müstensih alanı boş olan **295 kayıt**: 268'i Fenarizade'de, 27'si Hacıhasanzade'de.
**Ayrıntılı tablo:** [`mustensih_eksikleri.csv`](mustensih_eksikleri.csv). Tabloda her kayıt için metinden okunan ad, eşleşen şahıs(lar) ve metindeki ifade yer alıyor.
**Durum:** Bu listedeki hiçbir değişiklik henüz yapılmadı. İşlem, kodikolojik toplu işlem bittikten sonra başlayacak.

## Mevcut kullanıma göre kurallar

Müstensihi zaten girilmiş 320 kayıttan şu kurallar çıkarıldı:
- **“Bi-hattı X”:** müstensih X.
- **“Bi-hattı müʾellifihî”:** müstensih, eserin müellifi.
- **Eserin bir kısmı vâkıfın hattıyla:** ayrı bir şahıs kaydı kullanılıyor. Örnek: *Mevlânâ Musannifek (evvelinden birazı)* (#508).

## Gruplar

| # | Grup | Kayıt | Yapılacak |
|---|---|---:|---|
| M1 | “Bi-hattı X”; X veritabanında **tek** şahıs kaydıyla birebir eşleşiyor | 141 | Mevcut şahsa bağlanacak |
| M2 | “Bi-hattı X”; X veritabanında **yok** | 55 (53 farklı ad) | Yeni şahıs açılıp bağlanacak |
| M3 | “Bi-hattı X”; X adıyla **birden fazla** şahıs kaydı var | 16 | **Karar gerekiyor** (aşağıda) |
| M4 | Musannifek'in kendi hattı (“Bi-hattı Musannifek”, “kendi hattıyla”, “ve bi-hattıhî”) | 43 | Mevlânâ Musannifek'e (#11) bağlanacak |
| M5 | Eserin yalnızca bir kısmı Musannifek'in hattıyla | 9 | **Karar gerekiyor** (aşağıda) |
| M6 | “Bi-hattı müʾellifihî” (müellifin kendi hattı) | 7 | Ad yazılıysa o şahıs; yazılı değilse kitabın kayıtlı yazarı |
| M7 | “İbn Haşşâb hattıyla” (#2544) | 1 | **Karar gerekiyor**: mevcut *Muhammed bin Muhammed el-Haşşâb* mı, yeni şahıs mı? |
| X | “bi-hattı mağribî”, “bi’l-hattı’l-Kûfî”, “bi-hattın vâzıh” gibi yazı türü ya da yazı netliği bildiren ifadeler | 23 | **Dokunulmayacak**; bunlar müstensih bilgisi değil |

## Karar gereken konular

**M3. Aynı ada sahip birden fazla şahıs kaydı.** Veri girişi sırasında aynı ad için farklı zamanlarda ayrı şahıs kayıtları açılmış. Örnekler:
- “Muhammed bin Halîl”: #230, #131, #384 ve #204.
- “Muhammed bin Hüsâmeddîn”: #307 ve #226.

Bunların aynı kişi olup olmadığı belli değil, çünkü yaygın adlar. Seçenekler:
- **(a)** En çok müstensih olarak kullanılan kayda bağlamak. Kopyalar daha sonra ayrı bir çalışmada birleştirilebilir.
- **(b)** Her kayıt için yeni şahıs açmamak, bu 16 kaydı şimdilik boş bırakmak.

**M5. Kısmi Musannifek hattı.** Kayıtlara göre önerim:

| Kayıt | İfade | Öneri |
|---|---|---|
| #1438, #3421 | “Evvelinde bir iki varak Musannifek hattıyla” | #508 *Mevlânâ Musannifek (evvelinden birazı)* |
| #3446 | “Evvelinden bir cüz Musannifek hattıyla” | #508 |
| #3462 | “Evvelinden bir mikdâr Mevlânâ Musannifek hattıyla” | #508 (veritabanında bu ifade için zaten kullanılıyor) |
| #3467 | “Evvel sahîfesi ve âhir sahîfesi … Musannifek hattıyla” | #508 |
| #1862, #3463 | “Kenârında metin … Musannifek / Vâkıf hattıyla yazılmış” | Boş bırakılsın: asıl metnin müstensihi değil, kenardaki metni yazmış |
| #3478 | “Evvelinde altı varak mikdârı Mevlânâ Vâkıf hattıyla **zahriyyât**” | Boş bırakılsın: zahriye notu, istinsah değil |
| #3502 | Mecmuanın birçok risâlesi “bi-hattıhî” | #11 *Mevlânâ Musannifek* (eserlerin çoğu onun hattıyla) |

## Not

M2'de açılacak yeni şahıslar, metindeki adla birebir açılacak. Köşeli parantezle tamamlanmış harfler adın içine alınacak (“Zekeriyy[â]” → “Zekeriyyâ”). Kısaltılmış ya da eksik görünen adlar (ör. “Niʿmetullâh b”) açılmadan önce ayrıca kontrol edilecek.
