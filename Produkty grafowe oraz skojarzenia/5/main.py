def edgeList(array):
    edge_list = []
    edge_graph = []

    # krawędzie grafu
    for el in array:
        vertex = el[0]
        for v in el[1:]:
            edge = sorted([vertex, v])
            if edge not in edge_list:
                edge_list.append(edge)


    # wyznaczanie sąsiadów
    for j, el in enumerate(edge_list):
        edge_graph.append([])
        edge_graph[j].append([el[0], el[1]])
        for v in el:
            for i in array[v - 1][1:]:
                temp = sorted([v, i])
                if temp != el:
                    edge_graph[j].append(temp)

    return edge_graph


def completeAssociation(edge_list,result):
    for i in edge_list:
        edge = i[0]
        if i[0] not in result:
            result.append(edge)
        for j in i[1:]:
            if j in result:
                ed = i
                result.remove(edge)
                break

    return result


array = []
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
    except:
        break

edge_list = edgeList(array)
result = []

for i in edge_list:
    result_array = [i[0]]
    result.append(completeAssociation(edge_list,result_array))

max = 0
for i in result:
    if max < len(i):
        max = len(i)
num = len(edge_list) // 2
if max >= num and num % 2 == 0:
    print("Istnieje skojarzenie doskonałe")
else:
    print("Nie istnieje skojarzenie doskonałe")
