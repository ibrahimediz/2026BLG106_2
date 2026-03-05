# Ders 04: Gelişmiş Veri Yapıları (Listeler, Sözlükler, Demetler ve Kümeler)

Şuana kadar öğrendiğimiz değişkenler (`isim = "Ahmet"` veya `yas = 25`) tek bir veriyi taşıyabiliyordu. Ya 50 öğrencinin notlarını, bir şirketin veritabanındaki yüzlerce müşteriyi, ya da aynı "Araba"ya ait Marka, Model, Yıl, Fiyat bilgilerini tek bir kalemde topluca saklamak istersek? 

İşte burada "Veri Yapıları / Koleksiyonlar" devreye girer. Python'da verilerin organize edilmesi için 4 temel yapı vardır.

## 1. Listeler (Lists) ➔ `[]`
Sıralı, değiştirilebilir (mutable) ve aynı değerden birden fazla bulundurabilen en esnek ve en çok kullanılan veri tipleridir. Listeleri gerçek hayattaki "alışveriş veya yapılacaklar listesi" gibi düşünebilirsiniz; elemanlar eklenebilir, silinebilir, sırası değiştirilebilir.

```python
# Köşeli parantez ile tanımlanır
meyveler = ["Elma", "Armut", "Kiraz", "Muz", "Elma"] # Gördüğünüz gibi "Elma" iki kez eklenebilir.

# Karışık veri tiplerini de alabilirler!
karisik_liste = ["Ahmet", 25, 3.14, True] 
```

### İndeksleme (Erişim) ve Dilimleme (Slicing)
Liste içindeki bir veriye ulaşmak için o verinin "Oda Numarası"nı bilmemiz gerekir. Programlamada bu numaralara **İndeks (Index)** denir ve çok kritik bir kural olarak numaralandırma **HER ZAMAN 0'dan başlar!**

```python
takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]
print(takimlar[0]) # Galatasaray
print(takimlar[2]) # Beşiktaş

# En sondaki eleman için -1 indeksi kullanılır (Çok pratik bir Python özelliğidir)
print(takimlar[-1]) # Trabzonspor

# Dilimleme: Listenin belirli bir aralığını kopyalama a[baslangic:bitis]
# (Bitiş indeksi dahil edilmez!)
print(takimlar[0:2]) # Galatasaray ve Fenerbahçe'yi getirir
print(takimlar[2:])  # 2. indeksten başla cümlenin sonuna kadar al (Beşiktaş, Trabzonspor)
print(takimlar[:3])  # Başlangıçtan başla 3. indekse kadar al (GS, FB, BJK)
```

### Operasyonlar (Metotlar)
```python
is_listesi = ["Market", "Fatura", "Temizlik"]

# 1. Eleman Ekleme (Listenin sonuna)
is_listesi.append("Spor Yap") 
# 2. Araya Eleman Ekleme (1 numaralı indeksi kırmak, diğerlerini sağa kaydırmak)
is_listesi.insert(1, "Doktora Git") 
# 3. İisme Göre Eleman Silme (Bulduğu ilk eşleşeni siler)
is_listesi.remove("Fatura")
# 4. İndekse Göre Eleman Silme ve Okuma (En sondakini veya verilen indektekini siler döner)
silinen = is_listesi.pop(-1)
# 5. Alfabetik veya Sayısal Sıralama
sayilar = [10, 5, 100, 2]
sayilar.sort() # [2, 5, 10, 100]
```

## 2. Sözlükler (Dictionaries) ➔ `{}`
Gerçek hayattaki bir yabancı dil sözlüğünü düşünün. Bir "Kelime / Anahtar (Key)" ararsınız ve karşılığında bir "Açıklama / Değer (Value)" bulursunuz.
Sözlükler verileri `Anahtar: Değer` çiftleri halinde tutar. İngilizce telefon rehberi veya Veritabanı sorgularının dönüştüğü en iyi yerdir.

```python
ogrenci = {
    "isim": "Ahmet",
    "soyisim": "Yılmaz",
    "yas": 22,
    "bolum": "Bilgisayar Programcılığı",
    "notlar": [80, 95] # Bir sözlüğün içi liste barındırabilir!
}

# Değerlere erişmek için indeks(sayı) değil, Anahtarların isimleri kullanılır:
print("Öğrenci Adı:", ogrenci["isim"])
print("Vize Notu", ogrenci["notlar"][0])

# OLMAYAN bir anahtar sorulduğunda program hata(Crash) vermesin diye .get() metodu hayat kurtarır:
print(ogrenci.get("mezuniyet_yili", "Böyle bir bilgi bulunamadı"))

# Yeni bir eklenti veya güncelleme
ogrenci["sehir"] = "Bursa" # 'sehir' yoksa yeni oluşturur
ogrenci["yas"] = 23        # 'yas' zaten var olduğu için günceller (Üzerine yazar)
```

## 3. Demetler (Tuples) ➔ `()`
Listelere aşırı benzerler. Aralarındaki TEK devasa fark: **Demetler Immutable (Değiştirilemez) yapılardır.** Bir demet (Tuple) tanımlandıysa, doğuştan gelen özellikleri ile gömülür. Eleman eklenemez, çıkarılamaz, sıralaması değiştirilemez. 

**(Neden varlar?):** Yanlışlıkla verilerin silinmesinin istenmediği kritik güvenlik önlemi gerektiren noktalarda (Veritabanı bağlantı şifreleri, koordinatlar vb.) veya Python'un arka planında okuma performansı listelere göre daha yüksek olduğu için tercih edilir.

```python
aylar = ("Ocak", "Şubat", "Mart", "Nisan")
print(aylar[0]) # Ocak

# aylar.append("Mayıs") # UYARI: HATA VERİR
# aylar[0] = "Aralık"   # UYARI: HATA VERİR
```

## 4. Kümeler (Sets) ➔ `{}`
Matematikteki kümelerin birebir aynısıdır. İki kritik kuralı vardır:
1. Bir kümede aynı elemandan (Tekrarlayan veriden) sadece ama sadece **1 tane** bulunabilir.
2. Sırasızdırlar. Yani "Bana birinciyi getir `[0]`" gibi indeks mantığı işlemi yapamazsınız, çünkü her defasında rastgele dizilirler.

**(Neden varlar?):** Elinizde içinde 10 bin kelime olan bir metin var ve siz "Bu metinde kullanılan FARKLI kelimeleri bana bul" demek istiyorsunuz. Metni olduğu gibi listeye değil, Kümeye (`set`) atarsanız sistem tüm tekrar edenleri anında çöpe atar ve size eşsiz listeyi verir. Ayrıca bir verinin kümede olup olmadığına bakmak listelere bakmaktan binlerce kat daha hızlıdır.

```python
sayilar = {1, 2, 3, 3, 3, 3, 4, 5, 5}
print(sayilar) # Çıktı: {1, 2, 3, 4, 5}

# Matematiksel Küme İşlemleri (Gerçek gücü buradadır)
kume1 = {"Elma", "Armut", "Kiraz"}
kume2 = {"Karpuz", "Muz", "Elma"}

print(kume1 & kume2) # Kesişim (& veya .intersection()): İkisinde de olanlar -> {'Elma'}
print(kume1 | kume2) # Birleşim (| veya .union()): Hepsini tekrarsız birleştir -> {'Karpuz', 'Muz', 'Elma', 'Armut', 'Kiraz'}
print(kume1 - kume2) # Fark (- veya .difference()): kume1'de olup kume2'de olmayanlar -> {'Armut', 'Kiraz'}
```

---

## 💻 Bölüm Sonu Egzersizleri

1. **Öğrenci Not Defteri Sistemi (Liste ve Sözlük):**
   1. Boş bir liste oluşturun. (`okul = []`)
   2. Kullanıcıdan `input` ile sırasıyla Öğrenci Adı, Yaşı ve Okul Numarasını alın.
   3. Bu 3 bilgiyi tek bir "sözlük" `{}` içinde paketleyip, oluşturduğunuz boş `okul` listesine `.append()` ile ekleyin.
   4. Bunu bir `for` döngüsü ile 3 farklı öğrenci verisi alacak şekilde tekrarlatın.
   5. En sonunda listeyi ekrana yazdırın.
2. **Kopya Filtreleme (Küme):**
   Bir sınıftaki öğrencilerin okültesindeki en sevdiklerin filmlerinin sorulduğunu varsayın. Şöyle bir liste gelmiş:
   `filmler = ["Inception", "Matrix", "Interstellar", "Matrix", "Avengers", "Inception"]`
   Sadece SET (Küme) dönüşümü özelliğini kullanarak, öğrencilerin önerdiği "Farklı" filmlerin listesini ekrana bastıran kodu (2-3 satırda) yazınız.
3. **Plaka Sözlüğü (Sözlük Modifikasyonu):**
   `plakalar = {"İstanbul": 34, "İzmir": 35, "Konya": 42}` adında bir sözlüğünüz olsun.
   - Ankara(06) bilgisini bu sözlüğe ekleyin.
   - Bursa'nın plakasını bulmak için `.get()` metodunu kullanın ki, sistemde Bursa yoksa hata(Crash) vermeden `Bulunumadı` mesajı dönsün.
   - Konya'nın plakasını `del` veya `.pop()` metodu ile silin.
   - Son durumu ekrana formatlı olarak (Örn: "Şehir: İstanbul, Plaka: 34") bir `for k, v in sözlük.items()` döngüsüyle satır satır yazdırın.
