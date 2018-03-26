name = input("İsminizi Giriniz: ")
age = input("Yaşınızı Giriniz: ")
year = 2017

fark = 100-int(age)

if fark>0:
    print(name, "100 Yaşına Geldiğinde", year+fark, "Yılında Olacaksın.")

else:
    print(name, "100 Yaşındayken", year+fark, "Yılındaydın.")

