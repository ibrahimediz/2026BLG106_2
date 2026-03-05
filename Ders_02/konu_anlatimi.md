# Ders 02: Operatörler, Karar Yapıları ve Döngülere Giriş

Bu derste programımızın dümdüz yukarıdan aşağıya doğru ilerlemesini engelleyecek, belirli şartlar altında farklı kodların çalışmasını sağlayacak "Karar Yapılarını" (`if-elif-else`) uçtan uca öğreneceğiz. Öncesinde bu kuralları (şartları) yazmamıza imkan tanıyan Operatörleri incelemeliyiz.

## 1. Operatörler

Python'da değişkenler üzerinde işlemler, kıyaslamalar yapmak için matematiksel veya mantıksal semboller kullanırız. 

### A) Matematiksel ve Atama Operatörleri
Günlük matematikte kullandığımız operatörlerin kod tarafındaki karşılıklarıdır:
- `+`, `-`, `*`, `/` : Toplama, Çıkarma, Çarpma, Bölme
- `//` (Tam Bölme): Bölme işleminin ondalık kısmını atar, sadece tam sayı döner (`10 // 3 = 3`).
- `%` (Mod Alma): Bir sayının diğerine bölümünden **kalanı** verir (`10 % 3 = 1`). Çift-Tek sayı bulmada çok sık kullanılır (Sayının `% 2`'si 0 ise çifttir).
- `**` (Üs Alma): Sayının üssünü alır (`2 ** 3 = 8`).
- Atama Operatörleri (`=, +=, -=`): Bir değişkene değer atamak (`yas = 20`) veya var olan değerini artırmak/azaltmak (`yas += 1` ifadesi `yas = yas + 1` ile aynıdır) için kullanılır.

### B) Karşılaştırma Operatörleri
Bu operatörler iki değeri karşılaştırır ve geriye **mutlaka** mantıksal bir değer (`True` veya `False`) döner. Şart bloklarının (`if`) kalbinde yer alırlar.

- `==` (Eşit mi?): `5 == 5` -> `True`, `"Ali" == "Veli"` -> `False`. (Atama olan tek eşittir `=` ile karıştırmayın!).
- `!=` (Eşit değil mi?): İki değer birbirinden farklıysa `True` döner.
- `>`, `<`, `>=`, `<=` : Büyüktür, Küçüktür, Büyük Eşittir, Küçük Eşittir. (`5 >= 5` -> `True`).

### C) Mantıksal Operatörler (`and`, `or`, `not`)
Eğer tek bir koşulumuz yoksa, "Boyu 1.80'den uzun **VE** kilosu 80'den azsa" gibi çoklu koşulları birbirine bağlamak için kullanılır.

- `and` (Ve): Bağladığı **TÜM** koşulların doğru (`True`) olması gerekir. Biri bile `False` olursa sonuç `False` olur.
  - Örnek: `kullanici_adi == "admin" and sifre == "123"` (Her ikisi de doğruysa sisteme girer).
- `or` (Veya): Bağladığı koşulların **EN AZ BİR TANESİNİN** doğru olması yeterlidir.
  - Örnek: `not_ortalamasi > 50 or projesi_var_mi == True` (Öğrenci not ortalamasını tuttursa da geçer, projesi varsa da geçer).
- `not` (Değil): Çıkan bir mantıksal sonucun tam tersini alır (`True` ise `False` yapar).

### D) Üyelik ve Kimlik Operatörleri
- **Üyelik (`in`, `not in`):** Bir değerin (harfin, sayının), bir veri dizisi (örneğin metin veya liste) içinde bulunup bulunmadığına bakar. (Örn: `"a" in "Merhaba"` -> `True`).

---

## 2. Karar Yapıları (If - Elif - Else)

Şuana kadar yazdığımız kodlar hep baştan sona sırayla çalışıyordu. Ancak gerçek dünyada uygulamalar kararlar alırlar (Kullanıcı giriş yaptıysa Anasayfaya yönlendir, şifresi hatalıysa uyarı göster gibi). Bunu Karar yapısıyla sağlarız.

Python'da girinti (indentation - satır başındaki boşluklar) **HAYATİ ÖNEME SAHİPTİR.** Bir if bloğunun içindeki kod, `if` yazısına göre bir "Tab" veya 4 boşluk içeriden başlamalıdır.

### Temel `if` Kullanımı
Eğer bir koşul doğruysa o işlem yapılır. Yanlışsa hiçbir şey yapmadan program sonraki satırlardan devam eder.

```python
hava_durumu = "Yağmurlu"

if hava_durumu == "Yağmurlu":
    print("Şemsiyeni almayı unutma!") # Bu satır sadece hava yağmurluysa çalışır.
    
print("Bu yazı her zaman çalışır çünkü if'in dışındayız (hizasına geri döndük).")
```

### `if - else` (Eğer - Değilse)
Koşul sağlanıyorsa A planını, sağlanmıyorsa B planını uygulamak demektir.

```python
yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    print("Mekana giriş yapabilirsiniz.")
else:
    print("Reşit olmadığınız için girişiniz yasaktır!")
```

### Çoğul Koşullar `if - elif - else`
Eğer ihtimallerimiz iki taneden daha fazlaysa (örneğin sıcaklık 30'dan büyükse çok sıcak, 20-30 arasıysa ılık, 10-20 arasıysa serin, geri kalansa soğuk gibi) aradaki bağlaçlarımız `elif` (Else If'in kısaltması) olur.
Program yukarıdan aşağı koşulları kontrol eder; ilk `True` bulduğu bloga girer, onu çalıştırır ve **diğerlerini hiç kontrol etmeden karar yapısından toptan çıkar**.

```python
sinav_notu = int(input("Notunuzu girin (0-100): "))

if sinav_notu >= 90:
    print("Harika! Harf notun: AA")
elif sinav_notu >= 80:
    print("Çok İyi! Harf notun: BA")
elif sinav_notu >= 70:
    print("İyi! Harf notun: BB")
elif sinav_notu >= 50:
    print("Geçtin! Harf notun: CC")
else:
    print("Kaldın. Harf notun: FF")
    # Eğer nota örneğin "75" girilirse, program 90 ve 80 koşullarını yanlış kabul eder atlar,
    # 70 koşulunda True alır, içeriğini okur ve anında else kısmına gitmeden çıkar.
```

---

## 3. Döngülere Başlangıç (`while` ve `for`)

Yukarıdaki ehliyet örneğinde, kullanıcı yanlış yaş girdiğinde program bitiyordu. Tekrar sormak istersek? Veya 1'den 1000'e kadar yazdırmak istersek 1000 tane `print` mi yazacağız? Hayır. Belirli işleri tekrar tekrar yaptıran, programın kalbinin atmasını sağlayan mekanizmalar **döngülerdir.**

### A) `while` Döngüsü
`if` yapısına çok benzer. Fakat `if` koşula uyunca içini 1 kez yapıp çıkarken, `while` koşula uyduğu **SÜRECE** içini döne döne yapmaya devam eder.

```python
sayac = 1

while sayac <= 5: 
    print(f"{sayac}. kez Merhaba!")
    # Sayacı artırmazsak, sayac hep 1 kalır ve bilgisayar saniyede milyonlarca kez merhaba yazdırarak çöker!
    sayac += 1 
    
print("Döngü bitti!")
```

### B) `for` Döngüsü ve `range()`
Sabit bir aralıkta veya bir küme (liste, metin) içinde dolaşmak, tur atmak için kullanılır. `range(başlangıç, bitiş, artış)` komutu ile sayı aralığı verilir.

```python
# 1'den başlayıp 10'a kadar (10 DAHİL DEĞİL!) dönecek.
for sayi in range(1, 10): 
    print(sayi)
    
# Bir ismin harflerinde tek tek dolaşma
kelime = "PYTHON"
for harf in kelime:
    print("Mevcut harf:", harf)
```

### İç İçe Yapılar ve Kontrol İfadeleri (`break` & `continue`)
Programlar büyük oranda "Döngülerin İçine Açılmış İf/Else" komutlarından oluşur.
- `break`: Bir şart sağlandığında döngüyü resmen yok dercesine kırmak, acil çıkış yapmak için kullanılır.
- `continue`: Sadece o anki adımı atlayıp döngünün sıradaki elemanından turuna devam etmesi için kullanılır.

*Ders içindeki `05_kontrol_yapilari.py` örneği, döngüler ile karar yapılarının birleştiği oldukça detaylı algoritmalar barındırır.*

---

## 💻 Bölüm Sonu Egzersizleri

1. **Çift mi Tek mi?**
   Kullanıcıdan `input` ile bir tam sayı alınız. Mod alma (`%`) operatörünü kullanarak sayının Çift mi yoksa Tek mi olduğunu if-else yapısıyla ekrana bastırınız.
2. **Kullanıcı Girişi Simülasyonu:**
   Sistemde belirlenmiş bir kullanıcı adı (örneğin: `admin`) ve şifre (örneğin: `123123`) değişkenlerde tutulsun. Kullanıcıdan `input` ile ad ve şifre isteyin. 
   - İkisi de doğruysa "Sisteme Başarıyla Giriş Yaptınız", 
   - Yanlış bilgiler girilirse "Hatalı Kullanıcı adı veya Şifre", 
   şeklinde uyarı veren program kodlayın (Yardımcı eleman: `and` operatörü).
3. **Faktöriyel Hesaplayıcı (Zorluk: Orta):**
   Bir sayının faktöriyeli, 1'den o sayıya kadar tüm tam sayıların çarpımıdır (Örn: 4! = 1*2*3*4 = 24).
   Kullanıcıdan bir sayı isteyin. Bir `for` veya `while` döngüsü yardımıyla bu sayının faktöriyelini bulup ekrana yazdıran kodu yazınız. (İpucu: `carpim = 1` şeklinde bir geçiş değişkeni kullanmalısınız).
