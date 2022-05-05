"""Beşgen sayılar P(n)=n(3n−1)/2 şeklinde üretilir ve ilk 10 adet beşgen sayı 1, 5, 12, 22, 35, 51, 70, 92, 117, 145 şeklindedir.
P(4) + P(7) = P(8) = 22 + 70 = 92 sonucu bir beşgen sayıdır.
Konsoldan girilen bir sayının beşgen değeri iki adet beşgen sayının toplamı olup olmadığını bularak sayıları konsola yazınız.
Örnek: Girdi:8 ise Çıktı:P(4) + P(7) şeklinde konsola yazılacaktır."""

print("         *** BİR SAYININ BEŞGEN DEĞERİNİN, İKİ ADET BEŞGEN SAYININ TOPLAMI OLUP OLMADIĞINI BULAN PROGRAM ***")
print("\n")
print(""" - BİLGİ: BEŞGEN SAYILAR "P(X)=X(3X−1)/2" ŞEKLİNDE ÜRETİLİR. ("X", BEŞGEN DEĞERİNİ HESAPLAMAK İSTEDİĞİNİZ SAYIDIR!)""")
print("\n")

besgenSayilar = [] #Beşgen sayıları alması için dizi tanımlanması

a = 1
c = 0

while c<1000: #En büyük beşgen sayı 1000 olacak şekilde while döngüsünün devam etmesi
    c = a*(3*a-1)/2
    c = int(c)
    a+=1

    besgenSayilar.append(c) #Beşgen sayıların diziye aktarılması

besgenSayilar.pop() #Dizideki istemediğimiz son eleman olan 1000'in üstündeki beşgen değerin diziden çıkarılması

z = 1
print(" + 1000'E KADAR OLAN BEŞGEN SAYILAR : ")
print("\n")

for x in besgenSayilar:
    print(" * P({})= {}".format(z, int(x))) #1000'e kadar olan beşgen sayıların değerlerinin ekrana verilmesi

    z+=1

besgenSayi=0

while True: #Kullanıcı tarafından enter'a basılana kadar programın devam etmesi için sonsuz döngü oluşturulması

    print("\n")
    besgenSayi = int(input(" - BEŞGEN DEĞERİNİ HESAPLAMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ (PROGRAMI SONLANDIRMAK İÇİN ENTER'A BASINIZ!) : "))
    k = besgenSayi * (3 * besgenSayi - 1) / 2 #Beşgen değer hesaplanması
    k = int(k) #Bölme işlemi olduğu için çıkan sonucun tam kısmının alınması

    if (int(besgenSayi) == 0):
        print("\n")
        print(" +     0'DAN BÜYÜK BİR SAYI GİRİNİZ!")
        print("\n")

    elif(int(besgenSayi)<0):
        print("\n")
        print(" +     POZİTİF BİR SAYI GİRİNİZ!")
        print("\n")

    elif(int(besgenSayi) > 0 and int(besgenSayi) < 26):

        print("\n")
        print(" +     {} SAYISININ BEŞGEN DEĞERİ = {}".format(besgenSayi, int(k)))
        print("\n")

        sayac=0
        for p in besgenSayilar: #Koşulu gerçekleştirebilmesi için iç içe döngü oluşturulup, bu döngünün diziyi taraması
            for m in besgenSayilar:
                if (p + m == k):
                    if(p==m): #Beşgen değerin aynı iki beşgen değerin toplamı şeklinde ekrana verilmemesi için koşul oluşturulması
                        print(" +     {} DEĞERİ İKİ ADET FARKLI BEŞGEN SAYININ TOPLAMI ŞEKLİNDE YAZILAMAZ!".format(k))
                        y = besgenSayilar.index(p)
                        print(" +     AYNI İKİ BEŞGEN SAYI ŞEKLİNDE YAZILABİLİR ->",end=" ")
                        print( " P({}) + P({}) = {} + {} = {}".format(y,y,p,p,k))
                        sayac +=1
                    else:
                        y = besgenSayilar.index(p)
                        z = besgenSayilar.index(m)
                        if(z>y): #Ekrana iki çıktı vermemesi için bir durumun ele alınması (P(4)+P(7) ve P(7)+P(4) gibi
                                                                                           # bir durumda birinin ekrana
                                                                                           # verilmesi)
                            print(" +     P({}) = P({}) + P({})".format(besgenSayi, y+1, z+1))
                            print(" +     {} = {} + {}".format(k,p,m))
                            sayac +=1
        if (sayac == 0): #Döngü boyunca "...toplamı şeklinde yazılamaz" çıktısı vermemesi için sayaç tanımlanıp koşula bağlanması
            print(" +     {} DEĞERİ İKİ ADET FARKLI BEŞGEN SAYININ TOPLAMI ŞEKLİNDE YAZILAMAZ!".format(k))

        print("\n")

    else:
        print("\n")
        print(" +     {} DEĞERİ 1000'DEN BÜYÜK OLDUĞU İÇİN PROGRAM HESAPLAYAMAMAKTADIR. LÜTFEN BEŞGEN DEĞERİ 1000'DEN KÜÇÜK OLAN SAYI GİRİNİZ!".format(k))
        print("\n")
