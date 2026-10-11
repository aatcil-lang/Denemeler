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
