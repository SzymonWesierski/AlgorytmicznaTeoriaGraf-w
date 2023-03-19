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


for el in edge_list:
    result = ""
    el = [el[0]] + sorted(el[1:])
    for edge in el:
        temp = "({v1}, {v2}) "
        result += temp.format(v1 = edge[0],v2 = edge[1])
    print(result[:-1])
