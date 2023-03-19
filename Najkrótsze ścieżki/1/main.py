import sys

def dijkstra(n, array, start_vertex):
    vertices = []
    costs = []
    previous = []
    s = []

    # Inicjalizacja danych
    for i in range(n):
        vertices.append(i)
        costs.append(sys.maxsize)
        previous.append(-1)

    costs[start_vertex - 1] = 0

    # Główna pętla algorytmu
    while vertices:
        # Szukanie wierzchołka o najniższym koszcie
        u = min(vertices, key=lambda vertex: costs[vertex])
        #print(vertices)
        #print(costs)
        #print(u)

        # Przenoszenie wierzchołka do zbioru S
        s.append(u)
        vertices.remove(u)

        # Aktualizacja kosztów dojścia do sąsiednich wierzchołków
        for v, cost in enumerate(array[u]):
            if cost > 0 and v in vertices and costs[v] > costs[u] + cost:
                costs[v] = costs[u] + cost
                previous[v] = u

    # Zwracanie wyniku
    return costs, previous

# Wczytywanie danych
array = []
n = -1
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
        n += 1
    except EOFError:
        break
    except:
        print("BŁĄD")
        exit()

# Przetwarzanie
array_len = len(array)
start_vertex = array[array_len - 1][0]
array.pop(array_len - 1)

result = dijkstra(n, array, start_vertex)

for i in range(array_len - 1):
    print(i + 1,"=",result[0][i])
