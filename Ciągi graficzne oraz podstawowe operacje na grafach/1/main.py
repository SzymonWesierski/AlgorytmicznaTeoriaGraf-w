list = input().split()
sum = 0
check = 0
j = 0

for i in range(0, len(list)):
    list[i] = int(list[i])
    sum = sum + list[i]
    if (list[i] < 0):
        check = 1;

if (sum % 2 != 0):
    check = 1
else:
    while ((list[0] != 0) and check == 0):
        for i in range(0, len(list)):
            if (list[i] != 0):
                j = j + 1
        if (list[0] >= j):
            check = 1
        else:
            for i in range(1, list[0] + 1):
                list[i] = list[i] - 1
            list[0] = 0
        list.sort()
        list.reverse()

    for i in range(0, len(list)):
        if (list[i] < 0):
            check = 1

if (check == 0):
    print("TAK")
else:
    print("NIE")

