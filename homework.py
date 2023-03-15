'На вход подается строка, например: “ААААBBBCCF” напишите программу кодирующую эту строку по принципу: “4A3B2C1F'


a = input()
i = 0
count = 1
out = ''
while i < (len(a) - 1):
    if a[i] == a[i+1]:
        count += 1
    else:
        out = out + a[i] + str(count)
        count = 1
    i +=1
print(out+ a[i] + str(count))
