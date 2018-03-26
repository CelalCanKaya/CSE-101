number = int(input("Bir Sayı Giriniz: "))
list = []

for x in range(1, (number+1)):
    if number % x == 0:
        list.append(x)

print(number, "Sayısının Tam Bölenleri: ", list)
