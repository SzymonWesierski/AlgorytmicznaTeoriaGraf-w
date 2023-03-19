Zadanie 3 (0.5 pkt)
Napisz program, który dodaje wierzchołek wraz z krawędziami do grafu nieskierowanego reprezentowany jako macierz sąsiedztwa.
Program wczytuje macierz sąsiedztwa a następnie pobiera wiersz macierzy z nowym wierzchołkiem. Wynikiem programu jest macierz sąsiedztwa z dodanym wierzchołkiem. Zakładamy, że dodajemy wierzchołek zawsze na końcu macierzy.
Sample Input 1:
0 1 1 0 0
1 0 0 0 0
1 0 0 1 1
0 0 1 0 1
0 0 1 1 0
1 1 0 0 1 0
Sample Output 1:
0 1 1 0 0 1
1 0 0 0 0 1
1 0 0 1 1 0
0 0 1 0 1 0
0 0 1 1 0 1
1 1 0 0 1 0
Sample Input 2:
0 1 1 0 1 0 1 1 0 1
1 0 1 0 0 1 1 1 1 0
1 1 0 1 1 1 1 1 1 0
0 0 1 0 0 1 0 0 1 1
1 0 1 0 0 1 0 1 0 1
0 1 1 1 1 0 1 1 1 1
1 1 1 0 0 1 0 0 1 1
1 1 1 0 1 1 0 0 1 0
0 1 1 1 0 1 1 1 0 1
1 0 0 1 1 1 1 0 1 0
1 0 0 0 0 0 0 0 0 0 0
Sample Output 2:
0 1 1 0 1 0 1 1 0 1 1
1 0 1 0 0 1 1 1 1 0 0
1 1 0 1 1 1 1 1 1 0 0
0 0 1 0 0 1 0 0 1 1 0
1 0 1 0 0 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0
1 1 1 0 0 1 0 0 1 1 0
1 1 1 0 1 1 0 0 1 0 0
0 1 1 1 0 1 1 1 0 1 0
1 0 0 1 1 1 1 0 1 0 0
1 0 0 0 0 0 0 0 0 0 0
