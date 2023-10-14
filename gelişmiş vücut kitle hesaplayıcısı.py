print("Vücüt kitle indeksi hesaplayıcısı")
a = float(input("Boyunuz(metre cinsinden):"))
b = float(input("kilonuz:"))
c = float(b/(a**2))
print("{:.2f}".format(c))
if (c <= 18.5):
    print("Zayıfsınız")
elif (c <= 25):
    print("Normalsiniz")
elif (c <= 30):
    print("kilolusunuz")
else:
    print("Obezsiniz")

