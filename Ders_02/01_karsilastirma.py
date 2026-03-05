# Karşılaştırma işlemleri sonucunda True veya False değeri döner (Boolean)

sayi1 = 10
sayi2 = 5

print("Eşit mi?", sayi1 == sayi2)
print("Eşit değil mi?", sayi1 != sayi2)
print("Büyük mü?", sayi1 > sayi2)
print("Küçük mü?", sayi1 < sayi2)

# Mantıksal Operatörler (and, or, not)
print("Mantıksal Operatörler")
print("and:", sayi1 > sayi2 and sayi1 > 0)
print("or:", sayi1 > sayi2 or sayi1 < 0)
print("not:", not (sayi1 > sayi2))

# Membership Operatörleri (in, not in)
print("Membership Operatörleri")
liste = [1, 2, 3, 4, 5]
print("in:", 3 in liste)
print("not in:", 6 not in liste)

# Identity Operatörleri (is, is not)
print("Identity Operatörleri")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("is:", a is b) 
print("is not:", a is not c)


# unary operatörler (negatif, pozitif, mantıksal not)
print("Unary Operatörler")
x = 5
print("Negatif:", -x)
print("Pozitif:", +x)
print("Mantıksal not:", not (x > 0))
x+=5 # x = x + 5 --> x = 10

# bitwise operatörler (and, or, xor, not, shift)
print("Bitwise Operatörler")
a = 5  # 0101
b = 3  # 0011
print("Bitwise AND:", a & b)  # 0001
print("Bitwise OR:", a | b)   # 0111
print("Bitwise XOR:", a ^ b)  # 0110
print("Bitwise NOT:", ~a)     # 1010 (negatif sayı)
print("Bitwise Shift Left:", a << 1)  # 1010 (10)
print("Bitwise Shift Right:", a >> 1) # 0010 (2)

# Ternary Operatör
print("Ternary Operatör")
sayi = 10
sonuc = "Pozitif" if sayi > 0 else "Negatif"
print(sonuc)

