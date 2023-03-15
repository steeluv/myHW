log = input()
symbols = "?=*^$№@_"
c = ""
for i in log:
    if i in symbols:
        c += i + " "
print(c)