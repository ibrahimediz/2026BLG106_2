kullanici_adi = "admin"
sifre = "1234"

girilen_ad = input("Kullanıcı adı: ")
girilen_sifre = input("Şifre: ")

if girilen_ad == kullanici_adi and girilen_sifre == sifre:
    print("Giriş başarılı!")
elif girilen_ad == kullanici_adi and girilen_sifre != sifre:
    print("Şifre yanlış!")
else:
    print("Kullanıcı bulunamadı!")
