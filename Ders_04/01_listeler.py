meyveler = ["Elma", "Armut", "Kiraz", "Muz"]

print("Listenin tamamı:", meyveler)
print("İlk eleman:", meyveler[0])
print("Son eleman:", meyveler[-1])

# Slicing (Dilimleme)
print("İlk iki meyve:", meyveler[0:2])

# Eleman değiştirme
meyveler[1] = "Karpuz"
print("Güncel liste:", meyveler)

# Listeyi döngü ile gezme
for meyve in meyveler:
    print("Meyve:", meyve)
