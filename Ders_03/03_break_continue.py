# break kullanımı
print("Break örneği:")
for i in range(10):
    if i == 5:
        break # 5'e gelince döngüden çık
    print(i)

print("-" * 20)

# continue kullanımı
print("Continue örneği:")
for i in range(5):
    if i == 2:
        continue # 2'yi atla, devam et
    print(i)
