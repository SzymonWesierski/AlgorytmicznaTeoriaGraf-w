def is_matching(array, edges):
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][1] == edges[j][0] or edges[i][1] == \
                    edges[j][1]:
                return False
    return True


array = []
while 1:
    try:
        a = list(map(int, input().split()))
        array.append(a)
    except:
        break

list_len = len(array)
edges = array[list_len - 2:]
array.pop(list_len - 1)
array.pop(list_len - 2)

if is_matching(array, edges):
    print("Jest to skojarzenie")
else:
    print("Nie jest to skojarzenie")