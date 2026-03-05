print(range(5)) # range(5)
print(*range(5),sep=";") # 0;1;2;3;4
print(*range(2,10)) # 2;3;4;5;6;7;8;9
print(*range(2,10,2)) # 2;4;6;8
print(*range(10,1,-2)) # 10;8;6;4;2
#####################
# Kontrol Yapıları
# while
sayi = 0
while sayi < 5:
    print(sayi)
    sayi += 1
# 0 1 2 3 4
#####################
# for
for i in range(5):
    print(i)
# 0 1 2 3 4

liste = [1,2,3,4,5,6]
for item in liste:
    print(item)

################## Soru
"""
girilen ifade içerisinde yer alan büyük harflerin sayısını veren programı yazınız
"""
giris = input("ifadeyi giriniz:")
sayac = 0
for item in giris:
    if item.isupper():
        sayac += 1
else:
    print("büyük harf sayısı",sayac)

############### Noktalama işareti gelirse döngüyü durdurunuz
from string import punctuation
giris = input("ifadeyi giriniz:")

sayac = 0
for item in giris:
    if item in punctuation:
        print("Noktalama işareti bulundu, döngü durduruluyor.")
        break
    if item.isupper():
        sayac += 1
else:
    print("büyük harf sayısı",sayac)
######################


from string import punctuation
giris = input("ifadeyi giriniz:")

sayac = 0
for item in giris:
    if item in punctuation:
        print("Noktalama işareti bulundu, döngü durduruluyor.")
        continue
    if item.isupper():
        sayac += 1
else:
    print("büyük harf sayısı",sayac)



###############
# içerisinde en az 1 büyük harf, 1 küçük harf ve 1 rakam bulunan ve 1 noktalama işareti bir şifre oluşturunuz. 
# Şifre oluşturulmazsa kullanıcıya neden oluşturulamadığını söyleyiniz.
# şifrenin kontrolü ve üretimi ile ilgili kodları yazınız
################


from string import punctuation, ascii_uppercase, ascii_lowercase, digits
from random import choice
karakterlistesi = [ascii_uppercase, ascii_lowercase, digits, punctuation]
bharf = kharf = rakam = noktalama = False
while not (bharf and kharf and rakam and noktalama):
    sifre = ""
    for i in range(12):
        karakter = choice(choice(karakterlistesi))
        sifre += karakter
    else:
        for item in sifre:
            if item.isalpha():
                if item.isupper():
                    bharf = True
                else:
                    kharf = True 
            elif item in digits:
                rakam = True
            elif item in punctuation:
                noktalama = True
print("Oluşturulan şifre:", sifre)