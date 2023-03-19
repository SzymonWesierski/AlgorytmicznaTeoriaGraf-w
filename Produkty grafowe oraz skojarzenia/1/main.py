def graphComplement(array, vertexNumber):
    newArray = []
    i = 1

    for v in array:
        result = ""
        result += str(i) + " "
        for n in range(1, vertexNumber + 1):
            if n not in v:
                result += str(n) + " "
        newArray.append(result[:-1])
        i += 1

    return newArray


array = []
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
    except:
        break

vertexNumber = len(array)

newArray = graphComplement(array, vertexNumber)

for row in newArray:
    print(row)

