Zadanie 2 (4.5 pkt)

Średnicą grafu nazywamy największą odległość najkrótszych ścieżek, jaka występuje między wierzchołkami.

Napisz program, który dla danej ważonej macierzy sąsiedztwa wagami obliczy jego średnicę.

Dla prostoty zakładamy, że grafy są spójne i jego wagi są dodatnie.

Pod ocenę będą brane następujące elementy:

Testy (2.5 pkt)
Złożoność algorytmu (1 pkt)
Styl kodu (1 pkt)
Sample Input 1:

0 8 0 0 7
8 0 0 2 0
0 0 0 2 0
0 2 2 0 0
7 0 0 0 0
Sample Output 1:

19
Sample Input 2:

0 8 0 1
8 0 6 5
0 6 0 1
1 5 1 0
Sample Output 2:

6