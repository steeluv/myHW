def function(l1, l2, l3):
    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
        print(False)
    else:
        print(True)
function(l1 =int(input()), l2 = int(input()), l3 = int(input()))
