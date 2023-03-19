Zadanie 2 (2.5 pkt)

Zmodyfikujmy nieco nasz algorytm przeszukiwania w głąb następująco: 

Algorytm przeszukiwanie grafu w głąb (DFS):

Odwiedzamy wierzchołek 
�
v (zaznaczamy go jako odwiedzony) i wkładamy go na STOS
Dopóki STOS nie jest pusty wykonuj:
 Jeżeli 
�
v jest wierzchołkiem na wierzchu STOSU, to sprawdzamy czy istnieje wierzchołek sąsiedni z 
�
v (zgodnie z porządkiem bierzemy najmniejszy z sąsiadów), który nie był jeszcze odwiedzony.
Jeżeli uu jest takim wierzchołkiem, to odwiedzamy 
�
u i wkładamy go na stos.
Jeżeli takiego uu nie ma, to zdejmujemy 
�
v ze stosu.
Napisz program, który wczytuje od użytkownika macierz sąsiedztwa, następnie numer wierzchołka, i przeprowadza przeszukiwanie w głąb tego grafu według powyższej modyfikacji algorytmu. Wynikiem ma być kolejność odwiedzanych wierzchołków w tym grafie oraz informacja czy graf jest spójny czy nie.

W przypadku błędnych danych program ma wypisać komunikat: BŁĄD i ma zakończyć działanie.

Pod ocenę bierze się następujące elementy:

Testy (1.5 pkt)
Złożoność algorytmu (0.5 pkt)
Styl kodu (0.5 pkt)
Uwaga: Na stepiku nie otrzymuje się punkty za wykonanie tego zadania - punkty otrzyma się po pokazaniu kodu.

Sample Input 1:

1 3 4 6
2 5 6
3 1 5 7 8
4 1 5 7 8
5 2 3 4 7
6 1 2 7
7 3 4 5 6
8 3 4
1
Sample Output 1:

Porządek DFS: 1 3 5 2 6 7 4 8
Graf jest spójny
Sample Input 2:

1 2 8 9 10 13
2 1 4 5 9 10 11 12
3 4 5 9 15
4 2 3 7 12 14 16
5 2 3 7 9 10 15
6 7 8 9 10 13
7 4 5 6 8 10 12 16
8 1 6 7 9 10 11 12 13 14 15
9 1 2 3 5 6 8 11 12 13 14
10 1 2 5 6 7 8 11 15
11 2 8 9 10 13 14
12 2 4 7 8 9 13 15 16
13 1 6 8 9 11 12 14 15 16
14 4 8 9 11 13 15 16
15 3 5 8 10 12 13 14
16 4 7 12 13 14
1
Sample Output 2:

Porządek DFS: 1 2 4 3 5 7 6 8 9 11 10 15 12 13 14 16
Graf jest spójny
Sample Input 3:

1
2 6 7
3
4 6 8
5
6 2 4 7
7 2 6
8 4
1
Sample Output 3:

Graf jest niespójny