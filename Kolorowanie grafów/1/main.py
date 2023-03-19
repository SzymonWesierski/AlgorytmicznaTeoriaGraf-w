def colorable(color_list, array):

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = color_list[array[i][j] - 1]

    for i in range(len(array)):
        if array[i][0] in array[i][1:]:
            return "Graf nie jest kolorowalny"
    return "Graf jest kolorowalny"


array = []
while 1:
    try:
        a = list(map(int, input().split()))
        array.append(a)
    except :
        break

list_len = len(array)
color_list = array[list_len - 1]
array.pop(list_len - 1)
array.pop(list_len - 2)

print(colorable(color_list, array))
