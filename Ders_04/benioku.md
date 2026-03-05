# Ders 4: Veri Yapıları (Listeler ve Sözlükler)

Bu hafta birden fazla veriyi tek bir değişkende saklamamızı sağlayan yapıları inceleyeceğiz.

## Konu Başlıkları
1.  **Listeler (Lists)**: Sıralı ve değiştirilebilir veri koleksiyonları.
    - Tanımlama: `liste = [1, 2, "elma"]`
    - Erişim: `liste[0]`
    - Metotlar: `append()`, `remove()`, `pop()`, `sort()`
2.  **Sözlükler (Dictionaries)**: Anahtar-Değer (Key-Value) çiftlerinden oluşan yapılar.
    - Tanımlama: `sozluk = {"ad": "Ali", "yas": 25}`
    - Erişim: `sozluk["ad"]`
3.  **Demetler (Tuples)**: Listelere benzer ancak değiştirilemezler (Immutable).
    - Tanımlama: `demet = (1, 2, 3)`
    - Kullanım alanı: Değişmemesi gereken sabit veriler (örn. koordinatlar).
4.  **Kümeler (Sets)**: Eşsiz elemanlar barındıran sırasız koleksiyonlardır.
    - Tanımlama: `kume = {1, 2, 3}`
    - Özellikleri: Tekrar eden veri barındırmaz, matematiksel küme işlemleri (birleşim, kesişim) yapılabilir.

## Örnekler
- `01_listeler.py`: Liste oluşturma ve elemanlara erişim.
- `02_liste_metotlari.py`: Listeye ekleme, çıkarma işlemleri.
- `03_sozlukler.py`: Sözlük tanımlama, `get`, `update`, `items` gibi gelişmiş metotlar.
- `05_demetler_ve_kumeler.py`: Tuple ve Set veri yapılarının detaylı kullanımı.
- `04_alisveris_listesi.py`: Basit bir alışveriş listesi uygulaması.
