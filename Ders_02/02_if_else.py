not_ = int(input("Notunuzu girin: "))

if not_ >= 50:
    print("Geçtiniz!")
    print("Tebrikler!")
else:
    print("Kaldınız.")

# Çoklu koşul (elif)
puan = int(input("Puanınızı girin (0-100): "))

if puan >= 90:
    print("Harika!")
elif puan >= 70:
    print("İyi.")
elif puan >= 50:
    print("Orta.")
else:
    print("Daha çok çalışmalısın.")


