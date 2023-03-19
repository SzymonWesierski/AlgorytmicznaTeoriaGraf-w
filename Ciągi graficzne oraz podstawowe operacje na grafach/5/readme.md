Zadanie 2 (3 pkt)
Napisz program, który pobierze od użytkownika macierz sąsiedztwa grafu G (wierzchołki numerujemy od jedynki), a następnie wyświetli następujące informacje (każda informacja w osobnej linii):
•	Ilość wierzchołków
•	Ilość krawędzi
•	Ciąg stopni (nieposortowane)
•	Średni stopień grafu
•	Informacja czy graf należy do podstawowych klas grafów w kolejności:
•	Graf pełny - W tym przypadku program ma wypisać komunikat: Jest to graf pełny
•	Cykl - W tym przypadku program ma wypisać komunikat: Jest to cykl
•	Ścieżka - W tym przypadku program ma wypisać komunikat: Jest to ścieżka
•	Drzewo - W tym przypadku program ma wypisać komunikat: Jest to drzewo
•	Hiperkostka - W tym przypadku program ma wypisać komunikat: Jest to hiperkostka
•	W przypadku braku klas program ma wypisać komunikat: Graf nie należy do żadnej z podstawowej klas
Sprawdzamy w podanej powyżej kolejności i wypisujemy każdy poprawny wynik. Zakładamy dla prostoty, że grafy są spójne, ale dopuszczamy wierzchołki izolowane.
Pod ocenę będą brane następujące elementy:
•	(2.5 pkt) - Działanie programu
•	(0.5 pkt) - Styl kodu.

Uwaga: Na stepiku nie otrzymuje się punkty za wykonanie tego zadania - punkty otrzyma się po pokazaniu kodu.
Sample Input 1:
1 6 9 10
2 4 5 9
3 6
4 2 8
5 2 7 8 9
6 1 3 7 10
7 5 6 9
8 4 5
9 1 2 5 7
10 1 6
Sample Output 1:
Ilość wierzchołków: 10
Ilość krawędzi: 14
Stopnie wierzchołków: 3 3 1 2 4 4 3 2 4 2
Średni stopień: 2.8
Graf nie należy do żadnej z podstawowych klas
Sample Input 2:
1 2 3 4
2 1 3 4
3 1 2 4
4 1 2 3
Sample Output 2:
Ilość wierzchołków: 4
Ilość krawędzi: 6
Stopnie wierzchołków: 3 3 3 3
Średni stopień: 3
Jest to graf pełny
Sample Input 3:
1 2 3
2 1 4 5
3 1 6 7
4 2 8
5 2
6 3
7 3
8 4
Sample Output 3:
Ilość wierzchołków: 8
Ilość krawędzi: 7
Stopnie wierzchołków: 2 3 3 2 1 1 1 1
Średni stopień: 1.75
Jest to drzewo
Sample Input 4:
1 2
2 1 3
3 2 4
4 3 5
5 4 6
6 5 7
7 6 8
8 7
Sample Output 4:
Ilość wierzchołków: 8
Ilość krawędzi: 7
Stopnie wierzchołków: 1 2 2 2 2 2 2 1
Średni stopień: 1.75
Jest to ścieżka
Jest to drzewo
Sample Input 5:
1 3 4
2 3 4
3 1 2
4 1 2
Sample Output 5:
Ilość wierzchołków: 4
Ilość krawędzi: 4
Stopnie wierzchołków: 2 2 2 2
Średni stopień: 2
Jest to cykl
Jest to hiperkostka
