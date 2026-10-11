# Vâkıf Eksikleri: Onay Listesi

**Kaynak:** veritabanının güncel hâli (11.10.2026) ve *Kataloglar Transkripsiyon.docx* (Fenârî ve Hacıhasanzâde katalogları)
**Ayrıntılı tablo:** [`vakif_eksikleri.csv`](vakif_eksikleri.csv). Tabloda her kayıt için veritabanı metni ve katalog metni yan yana durur.
**Hiçbir değişiklik yapılmadı.** Onaylanan maddeler, A–C düzeltmelerinde olduğu gibi yedekli ve doğrulamalı biçimde işlenecek.

## Genel durum

| Kaynak | Kayıt | Vâkıfı boş | “[bilgi yok]” |
|---|---:|---:|---:|
| Fenarizade | 1293 | **0** | 19, katalogla tutarlı (vâkıfı bilinmeyen ve kayıp kitaplar) |
| Hacıhasanzade | 1783 | **121** | 15 |

Hacıhasanzade'deki 136 kaydın 135'i katalogda neredeyse birebir karşılığını buldu (benzerlik ≥ 0,85). Kalan bir kayıt elle kontrol edildi. Bu kayıtların hemen hepsi katalogun **II. bölümünde** (*İlhâkāt-ı Kadîme*). Bu bölümde vâkıf, her kaydın kendi metnindeki “Vakf-ı …” ibaresinden belli oluyor.

**Eşleştirme yöntemi:** Her ibare için veritabanında aynı ibareyi taşıyan ve vâkıfı **zaten girilmiş** kayıtlara bakıldı. Öneriler bu mevcut kullanıma dayanıyor.

## Önerilen atamalar (vâkıfı boş 121 kayıt)

| # | Katalogdaki ibare | Kayıt | Önerilen vâkıf | Dayanak |
|---|---|---:|---|---|
| V1 | Vakf-ı Kādîzâde / Kādızâde | 92 | **Kādızâde (#434)** | Aynı ibareyi taşıyan 43 kaydın 43'ü bu şahısta |
| V2 | Vakf-ı Ahmed Kâbilî | 11 | **Mevlânâ Kâbilîzâde (#9)** | Aynı ibareyi taşıyan 79 kaydın 79'u bu şahısta |
| V3 | Vakf-ı Hatîbzâde | 7 | **Mevlânâ Hatîbzâde (#10)** | 74 kaydın 74'ü bu şahısta |
| V4 | Vakf-ı (Mevlânâ) Musannifek | 3 | **Mevlânâ Musannifek (#11)** | 78 kaydın 78'i bu şahısta |
| V5 | Katalogun V. bölümü (Halebîzâde), #2045 | 1 | **Halebîzâde (#741)** | Bölüm başlığı: *“…bi-Halebîzâde elletî vakafehâ…”* |
| V6 | Vakf-ı Bâzergânzâde | 5 | Veritabanında bu şahıs **yok**. Yeni şahıs kaydı açılmalı | Sizin kararınız |
| V7 | Vakf-ı (Mevlânâ) Kāsım bin Hasan el-Karamânî | 2 | Veritabanında **yok**. Yeni şahıs kaydı açılmalı | Sizin kararınız. Benzer bir ad var: #198 *Kāsım bin İbrâhîm el-Karamanî*, ama baba adı farklı |

Toplam: 92 + 11 + 7 + 3 + 1 + 5 + 2 = **121**.

## Dokunulmaması önerilenler

| # | Durum | Kayıt |
|---|---|---:|
| V8 | Katalogda *“Mine’l-kütübi’l-gayri maʿlûme”* (vâkıfı bilinmeyen) yazıyor. Veritabanındaki “[bilgi yok]” doğru | 14 |
| V8* | #1942 (61a [46]): katalogda *“Mine’l-kütübi’l-**maʿlûm** vâkıfuhâ”* yazıyor ama vâkıf adı yok. Komşu kayıtlara bakılırsa “gayri” kelimesi düşmüş olmalı. “[bilgi yok]” kalsın, transkripsiyon kontrol edilsin | 1 |

## Ayrıca karar gerektiren tutarsızlık

| # | Durum | Kayıt |
|---|---|---:|
| V9 | Katalogun **IV. Şeyhzâde** ve **V. Halebîzâde** bölümlerinin başlığı: *“Mevlânâ … Şeyhzâde / Halebîzâde’nin vakfedip (vakafehâ) Sultan Mehmed Camii’ne koyduğu kitaplar”*. Veritabanında bu kayıtların çoğu **II. Mehmed**’e bağlı: Şeyhzâde bölümünde 44 kaydın 43'ü, Halebîzâde bölümünde 332 kaydın 314'ü. Yalnızca 1 kayıt Şeyhzâde'ye (#570), 17 kayıt Halebîzâde'ye (#741) bağlı. | 357 |

Bu bilinçli bir tercih olabilir: kitaplar Fatih Camii'ne konduğu için II. Mehmed'e bağlanmış olabilir. Ama aynı bölümden 18 kaydın Şeyhzâde ve Halebîzâde'ye bağlı olması, uygulamanın tutarlı olmadığını gösteriyor. Seçenekler:
- **(a)** Bölüm başlığına göre bütün kayıtları Şeyhzâde (#570) ve Halebîzâde'ye (#741) bağlamak.
- **(b)** Hepsini II. Mehmed'de bırakıp aykırı 18 kaydı II. Mehmed'e çevirmek.
- **(c)** Şimdilik dokunmamak.
