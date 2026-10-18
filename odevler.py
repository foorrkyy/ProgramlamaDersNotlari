'''
Ödev 1:
Girilen 30 sayıdan en ufağını bulan kod:
'''
sayilar = []
for d in range(0, 29):
    sayilar += input("Bir sayı giriniz: (Bu işlem 30 defa tekrar edecektir) ")

enKucuk = sayilar[0]
for e in sayilar:
    if e < enKucuk:
        enKucuk = e
    else:
        pass

print(enKucuk)
'''
Ödev 2:
Girilen bir sayının çarpma işlemi kullanmadan üssünü alan bir program:
'''
sayi = int(input("Bir sayi giriniz: "))
ilkSayi = sayi
for sayac in range(1, sayi):
    sayi = sayi + ilkSayi

print(sayi)
'''
Ödev 3:
3 basamaklı bir sayının basamaklarını bulan program:
'''
sayi = str(input("3 basamaklı bir sayı giriniz: "))

sonuc = int(sayi[0]) + int(sayi[1]) + int(sayi[2])

print(sonuc)
'''
12.10.2026
Ödev 1:
100 - 999 arasındaki armstrong sayısı.
'''
armstrong = 0
for s in range(100, 1000):
    s = str(s)
    toplam = int(s[0])**3 + int(s[1])**3 + int(s[2])**3
    if toplam == int(s):
        armstrong += 1
    else:
        pass
print(armstrong)
'''
Ödev 2:
tahmin oyunu
'''
import random;
seviye = 1
hak = 5 # +3
aralik = 20 # 40, 80
bss = random.randint(0, aralik)

# Doğru bilirse cevaplama hakkı azalmayacak
while hak > 0:
    print(f"Seviye: {seviye}, 0 ile {aralik} aralığındaki sayılar")
    #print("bss: ", bss)
    tahmin = int(input("Bilgisayarın seçtiği sayıyı tahmin ediniz: "))

    if tahmin == bss:
        bss = random.randint(0, aralik)
        print("Tebrikler! Doğru bildiniz!")
        seviye += 1
        print(f"Bir sonraki seviyeye atladınız. Seviye: ", seviye)
        aralik += 20
        hak += 3
        print("Kalan haklarınız: ", hak)
        if seviye == 3:
            print("Tebrikler! Kazandınız!")
            print("Skor: ", (hak * 30))
            break
    elif tahmin < bss:
        hak -= 1
        print("Yanlış! Daha büyük bir sayı deneyiniz: ")
        print("Kalan haklarınız: ", hak)
    else:
        hak -= 1
        print("Yanlış! Daha küçük bir sayı deneyiniz: ")
        print("Kalan haklarınız: ", hak)

'''
Ödev 3:
    -1 girilmediği sürece sayıların ortalamasını bulan program
'''
girdi = input("-1 dışında ortalamasını almak istediğiniz sayıları arasında boşluk bırakarak giriniz: ")
girdi = girdi.split()
adet = 0;
toplam = 0

for g in girdi:
    g = int(g)
    if g == -1:
        print("-1 girdiniz! Lütfen tekrar deneyiniz")
        break
    toplam += g
    adet += 1

print("girdiğiniz sayıların toplamı: ", toplam/adet)
