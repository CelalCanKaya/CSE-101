word = str(input("Bir kelime giriniz: "))
list = []
for x in word:
    list.append(x)

while list != []:

    a = list.pop(0)
    if list == []:
        b = a
    else:
        b = list.pop()

    if a!=b:
        print(word, "Kelimesinin Okunuşu ve Tersten Okunuşu Aynı Değil.")
        break

if list==[]:
    print(word, "Kelimesinin Okunuşu ve Tersten Okunuşu Aynı.")
