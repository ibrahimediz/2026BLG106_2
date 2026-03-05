# Ders 03: Döngüler (Loops) ve İterasyon Mantığı

Bu derste programlarımızda tekrar eden işlemleri otomatikleştirmek, koleksiyonlar (listeler, metinler vb.) üzerinde eleman eleman gezinmek (iterasyon) için kullandığımız döngü yapılarını (`for` ve `while`) örneklerle ve farklı kullanım senaryolarıyla detaylıca inceleyeceğiz.

## 1. Neden Döngülere İhtiyacımız Var?
Diyelim ki ekrana 10 kere "Merhaba" yazdırmanız gerekiyor. Alt alta 10 tane `print("Merhaba")` yazabilirsiniz. Peki ya 1 milyon kere yazdırmanız gerekirse? Veya elinizdeki 5.000 kişilik müşteri listesinin hepsine tek tek e-posta atmanız gerekirse?

İşte bilgisayarların en iyi yaptığı iş olan "yorulmadan aynı işi tekrar tekrar hızlıca yapma" görevini döngüler üstlenir.

## 2. `for` Döngüsü
`for` döngüsü, önceden sayısı belli olan tekrarlarda veya bir liste/metin gibi "tek tek dolaşılabilen (iterable)" nesnelerin her bir elemanına sırasıyla erişmek için kullanılır.

### A) `range()` Fonksiyonu ile Belirli Sayıda Tekrar
`range(baslangic, bitis, artis)` şeklinde çalışarak sayı dizileri oluşturmamızı sağlar.
- **Sadece Bitiş Verilirse:** `range(5)` -> 0'dan başlar 5'e (dahil değil) kadar gider. (0, 1, 2, 3, 4)
- **Başlangıç ve Bitiş:** `range(2, 6)` -> [2, 3, 4, 5]
- **Artış Miktarı:** `range(1, 10, 2)` -> [1, 3, 5, 7, 9]

```python
# 0'dan 4'e kadar sayıları tek tek ekrana yazdırma
for i in range(5):
    print("Mevcut döngü adımı (i değişkeni):", i)

# Alt alta 5 kere metin yazdırma
for tur in range(5):
    print("Seni çok seviyorum Python!")
```

### B) Bir Metin veya Listenin İçinde Dolaşmak (Iterasyon)
Python'da bir string (metin), esasında karakterlerin arka arkaya dizildiği bir gruptur. `for` ile kelimenin harfleri arasında gezebilirsiniz.

```python
isim = "Python"
# Her turda "isim" değişkeninden bir harf çekilir ve "harf" değişkenine atanır.
for harf in isim:
    print("Geçerli harf:", harf)
# Çıktı: P, y, t, h, o, n (alt alta)

# (İleride göreceğimiz) Listelerde dolaşım:
isimler = ["Ali", "Veli", "Ayşe"]
for kisi in isimler:
    print(f"Hoş geldin {kisi}!")
```

## 3. `while` Döngüsü
`while` döngüsü, belirli bir tekrar sayısı vermediğimiz, ancak **koşul (şart) doğru (True) olduğu sürece** dönmeye devam eden döngülerdir.

### Sonsuz Döngü Tuzağı ⚠️
Eğer `while` şartını sağlayan döngü bloklarında sayacı veya şartı kıracak bir işlem yapmazsanız, bilgisayarınız döngüden çıkamaz (Sonsuz Döngü).

```python
sayac = 1
while sayac <= 5:
    print(f"{sayac}. tur")
    sayac += 1 # Sayacı 1 artırıyoruz. Bunu yazmazsak sayac hep 1 kalır ve döngü ASLA BİTMEZ!

print("Döngü başarıyla tamamlandı.")
```

### Ne Zaman `for`, Ne Zaman `while` Seçilmeli?
- **For:** Tekrar sayısı tam olarak belliyse (Bir listenin sonuna kadar git, 10 kere ekrana bas gibi).
- **While:** Döngünün ne zaman biteceğini kullanıcının kararlarına veya belirsiz bir şartın gerçekleşmesine bağladıysanız. (Örn: Kullanıcı 'q' tuşuna basana kadar hesap makinesini çalıştır).

## 4. Döngüleri Kontrol Etmek (`break` ve `continue`)

Döngüler normalde şart bitene kadar çalışır. Bazen onları manuel olarak müdahale edip değiştirmemiz gerekir.

### A) `break` (Döngüyü Tamamen Kırmak)
Aradığınız veriyi bulduğunuzda veya sistemin acil olarak durması gerektiğinde döngüyü *derhal ve tamamen* sonlandırmak için kullanılır.

```python
# Örnek: Şifre bulma sistemi (Sonsuz hak yok, 3 yanlışta sistemi kilitleriz)
hak = 3
while hak > 0:
    sifre = input("Şifrenizi giriniz: ")
    if sifre == "1234":
        print("Sisteme hoş geldiniz!")
        break # Şifre doğru, sonsuz döngüyü kır ve çık
    else:
        hak -= 1
        print(f"Yanlış şifre! Kalan hakkınız: {hak}")

if hak == 0:
    print("Hesabınız bloke edildi!")
```

### B) `continue` (Adımı Atlayıp Devam Etmek)
Döngüyü tamamen bitirmek yerine, sadece içindeki bulunduğu "o anki turu" görmezden gelip **yarım bırakarak** döngünün başından, yani sıradaki elemandan devam etmesini sağlar.

```python
# Örnek: 1'den 10'a kadar saydırırken 3'ün katlarını sevmiyorsak onları atlayalım.
for sayi in range(1, 11):
    if sayi % 3 == 0:
        continue # sayi 3, 6 veya 9 olduğunda alttaki print'i ATLAR. Sıradaki sayıya geçer.
    print(sayi)
# Çıktı: 1 2 4 5 7 8 10
```

---

## 💻 Bölüm Sonu Egzersizleri

1. **Çarpım Tablosu (for):** 
   Kullanıcıdan bir 1 ile 10 arasında rakam isteyin. Bu rakama ait çarpım tablosunu ekrana yazdıran programı kodlayın. *(Örnek Çıktı (5 girdiyse): 5 x 1 = 5, 5 x 2 = 10, ... 5 x 10 = 50)*
2. **Kelimedeki Sesli Harf Avcısı (for & continue):** 
   Kullanıcıdan uzun bir cümlemesini `input` ile isteyin. Cümledeki tüm "a, e, i, ı, o, ö, u, ü" harflerinin (sesli harflerin) kaç adet olduğunu sayan ve toplamı yazdıran bir algoritma yazın.
3. **Akıllı Atm (while & break):**
   Kullanıcının hesabında 5000 TL bakiye olsun. Bir sonsuz `while` döngüsü oluşturun (`while True:` kullanabilirsiniz). 
   - Ekrana "Çekmek istediğiniz tutar (Çıkmak için 'q' tuşuna basınız): " metni çıkarın.
   - Kullanıcı 'q' girerse `break` ile programdan çıkın.
   - Kullanıcı sayı girerse ve bu sayı 5000'den büyükse (bakiyesi yetmiyorsa) uyarı verip tekrar döngünün başına döndürün.
   - Yeterli bakiyesi varsa bakiyeden tutarı eksiltip yeni bakiyeyi ekrana yazdırın.
