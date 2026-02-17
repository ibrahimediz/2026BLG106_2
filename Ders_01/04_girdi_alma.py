# Kullanıcıdan veri almak için input() kullanılır
# input() her zaman string döndürür

ad = input("Adınız nedir? ")
print("Merhaba", ad)

# Sayısal işlem yapmak için dönüştürmek gerekir
dogum_yili = input("Doğum yılınız: ")
yas = 2024 - int(dogum_yili)
print("Tahmini yaşınız:", yas)
