def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        return "Hata: Sıfıra bölünemez!"
    return x / y

print("10 + 5 =", topla(10, 5))
print("10 - 5 =", cikar(10, 5))
print("10 * 5 =", carp(10, 5))
print("10 / 5 =", bol(10, 5))
