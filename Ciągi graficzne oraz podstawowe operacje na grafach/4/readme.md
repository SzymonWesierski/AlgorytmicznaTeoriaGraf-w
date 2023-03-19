Zadanie 4 (0.7 pkt)
Napisz program, który pobiera od użytkownika graf reprezentowany jako macierz sąsiedztwa, a następnie numer wierzchołka grafu (oznaczmy go jako �a).
Następnie program ma usunąć wierzchołek (wraz z incydentnymi krawędziami) z grafu. Wynikiem programu ma być wyświetlona macierz sąsiedztwa bez wymaganego wierzchołka.
W przypadku błędnego numeru wierzchołka program ma wypisać komunikat: BŁĄD i ma zakończyć działanie.
Program ma modyfikować istniejącą macierz sąsiedztwa (będzie to brane pod ocenę)!!!
Sample Input 1:
0 1
1 0
2
Sample Output 1:
0
Sample Input 2:
0 1 0 1 1 0 1 1
1 0 0 0 0 1 1 1
0 0 0 0 0 1 0 0
1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0
1 1 0 0 0 0 0 1
1 1 0 0 0 0 1 0
0
Sample Output 2:
BŁĄD

