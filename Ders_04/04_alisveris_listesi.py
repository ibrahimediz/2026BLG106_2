alisveris_listesi = []

while True:
    print("\n--- Alışveriş Listesi ---")
    print("1. Ürün Ekle")
    print("2. Listeyi Gör")
    print("3. Ürün Sil")
    print("4. Çıkış")
    
    secim = input("Seçiminiz (1-4): ")
    
    if secim == "1":
        urun = input("Eklenecek ürün: ")
        alisveris_listesi.append(urun)
        print("Eklendi.")
    elif secim == "2":
        print("Listeniz:")
        for i, urun in enumerate(alisveris_listesi):
            print(f"{i+1}. {urun}")
    elif secim == "3":
        silinecek = input("Silinecek ürün adı: ")
        if silinecek in alisveris_listesi:
            alisveris_listesi.remove(silinecek)
            print("Silindi.")
        else:
            print("Ürün bulunamadı.")
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim.")
