Zadanie 1 (1 pkt)

Dopełnieniem grafu prostego  nazywamy graf , w którym dwa wierzchołki są sąsiednie wtedy i tylko wtedy, gdy nie są sąsiednie w grafie G.

Napisz program, który dla grafu podanego jako lista sąsiedztwa wypisze jego dopełnienie jako lista sąsiedztwa.

Sample Input 1:

1 2
2 1 3
3 2 4
4 3
Sample Output 1:

1 3 4
2 4
3 1
4 1 2
Sample Input 2:

1 2 3 4
2 1 3 4
3 1 2 4
4 1 2 3
Sample Output 2:

1
2
3
4