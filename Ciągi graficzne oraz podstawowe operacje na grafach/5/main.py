import math


def numberOfVertices(list):
    return len(list)

def numberOfEdges(list):
    edge = 0
    for i in list:
        edge += len(i) - 1
    return edge // 2

def sequenceOfDegrees(list):
    degrees = ""
    for i in list:
        edge = 0
        edge += len(i) - 1
        degrees += str(edge) + " "
    return degrees[:-1]

def averageDegree(list):
    degrees = sequenceOfDegrees(list).split()
    sum = 0
    for n in degrees:
        sum += int(n)
    result = sum / len(degrees)
    if result.is_integer():
        result = int(result)
    return result

def completeGraph(list):
    n = numberOfVertices(list)
    for i in list:
        if len(i) != n:
            return False
    return True

def cycle(list):
    if averageDegree(list) == 2:
        return True
    return False

def path(list):
    degrees = sequenceOfDegrees(list).split()
    if degrees[0]+degrees[len(degrees) - 1] == "11":
        for n in degrees[1:len(degrees) - 1]:
            if n != "2":
                return False
    else:
        return False
    return True

def tree(list):
    if numberOfVertices(list) - 1 == numberOfEdges(list) and "0" not in sequenceOfDegrees(list):
        return True
    return False

def hypercube(list):
    n = math.log(numberOfVertices(list), 2)
    if numberOfEdges(list) == n * 2 ** (n - 1) and n.is_integer():
        return True
    else:
        return False

list = []
boolen = True
while 1:
    try:
        a = input().split()
        if a == []:
            break
        list.append(a)
    except :
        break

print("Ilość wierzchołków:",numberOfVertices(list))
print("Ilość krawędzi:",numberOfEdges(list))
print("Stopnie wierzchołków:",sequenceOfDegrees(list))
print("Średni stopień:",averageDegree(list))

if completeGraph(list):
    print("Jest to graf pełny")
    boolen = False
if cycle(list):
    print("Jest to cykl")
    boolen = False
if path(list):
    print("Jest to ścieżka")
    boolen = False
if tree(list):
    print("Jest to drzewo")
    boolen = False
if hypercube(list):
    print("Jest to hiperkostka")
    boolen = False
if boolen:
    print("Graf nie należy do żadnej z podstawowych klas")
