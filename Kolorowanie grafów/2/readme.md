Zadanie 2 (7 pkt)

Napisz program, który dla grafu podanego jako lista sąsiedztwa, wypisze kolorowanie wierzchołków przeprowadzone za pomocą algorytmu LF (largest first). Ponadto program ma wypisać liczbę chromatyczną otrzymaną w wyniku tego pokolorowania.

Zakładamy, że wybieramy niepokolorowany wierzchołek o najwyższym stopniu i najwyższym labelu. Oznacza to, że jeśli wierzchołek 2 ma stopień 4 oraz wierzchołek 3 ma stopień 4 to wybieramy najpierw wierzchołek 3.

Natomiast podczas przeszukiwania sąsiadów zaczynamy zawsze od sąsiada z najmniejszym labelem.

Sample Input 1:

1 2
2 1 3
3 2 4
4 3 5
5 4 6
6 5
Sample Output 1:

Pokolorowanie wierzchołków: 1 2 1 2 1 2
Liczba chromatyczna == 2
Sample Input 2:

1 2 3 4
2 1 3 5
3 1 2 4 5
4 1 3 6 7
5 2 3 6 7
6 4 5
7 4 5
Sample Output 2:

Pokolorowanie wierzchołków: 4 3 2 1 1 2 2
Liczba chromatyczna == 4