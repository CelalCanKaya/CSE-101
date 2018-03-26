number = int(input("Enter a number: "))
list = []

for x in range(2, number):
    if number % x == 0:
        list.append(x)


if list == [] and number>=2:
    print(number, "Bir Asal Sayıdır.")
else:
    print(number, "Bir Asal Sayı Değildir.")
