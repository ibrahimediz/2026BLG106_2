yas = int(input("Yaşınızı girin: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    kalan_yil = 18 - yas
    print(f"Ehliyet almak için {kalan_yil} yıl daha beklemelisiniz.")
