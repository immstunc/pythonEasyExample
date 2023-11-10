#listeye girilen  sayıların toplamını ortalamasını en küçük ve en büyük liste elemanını veren uygulama

listOfNumber = []
countOfNumber = int(input("Listeye kaç adet sayı ekleyeceksiniz? : "))
print("{} adet sayı listeye gireceksiniz.".format(countOfNumber))
sum = 0

for n in range(countOfNumber):
    number = int(input("{}. sayıyı girin : ".format(n+1)))
    listOfNumber.append(number)
    sum+=number

avarage = sum/countOfNumber
smallest = min(listOfNumber)
biggest = max(listOfNumber)

select = input("Görmek istediğiniz işlem sonucunu seçiniz:\n1.Girilen Sayıların Toplamı\n2.Girilen Sayıların Ortalaması\n3.Girilen Sayıların En Küçüğü\n4.Girilen Sayıların En Büyüğü\n")

if select == "1":
    print("Seçiminiz : {} İşlem Sonucu...".format(select))
    print("Toplama Sonucu = ",sum)
elif select == "2":
    print("Seçiminiz : {} İşlem Sonucu...".format(select))
    print("Girilen Sayıların Ortalaması = ",avarage)
elif select == "3":
    print("Seçiminiz : {} İşlem Sonucu...".format(select))
    print("Girilen Sayıların En Küçüğü = ", smallest)
elif select == "4":
    print("Seçiminiz : {} İşlem Sonucu...".format(select))
    print("Girilen Sayıların En Büyüğü  = ",biggest)
else: 
    print("Hatalı seçim yaptınız.")

