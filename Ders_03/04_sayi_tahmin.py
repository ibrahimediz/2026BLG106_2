import random

tutulan_sayi = random.randint(1, 100)
print("1 ile 100 arasında bir sayı tuttum.")

while True:
    tahmin = int(input("Tahmininiz: "))
    
    if tahmin < tutulan_sayi:
        print("Daha büyük bir sayı girin.")
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir sayı girin.")
    else:
        print("Tebrikler! Bildiniz.")
        break # Doğru bilince döngüden çık
