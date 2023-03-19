Skojarzeniem w grafie 
G nazywamy zbiór krawędzi, który jest niezależny. Oznacza to, że dla każdych dwóch krawędzi 
  nie mają one wspólnego wierzchołka.

Zadanie 4 (1 pkt)

Napisz program, który wczyta graf za pomocą listy sąsiedztwa, następnie wczyta listę krawędzi (po wcześniejszym klawiszu enter). Wynikiem programu ma być informacja czy dana lista krawędzi tworzy skojarzenie w  grafie 
�
G

Sample Input 1:

1 2
2 1 3
3 2 4
4 3 5
5 4

4 5
2 3
Sample Output 1:

Jest to skojarzenie
Sample Input 2:

1 2
2 1 3
3 2 4
4 3 5
5 4

4 5
3 4
Sample Output 2:

Nie jest to skojarzenie