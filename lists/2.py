marks = [5,3,4,2]
mark = len(marks)
print(mark)
a = 0
for i in marks:
    if 3 <= i <= 5:
        a += 1
print(a/mark*100)