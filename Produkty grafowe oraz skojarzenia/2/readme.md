Zadanie 2 (1 pkt)

Kwadratem grafu  nazywamy graf , taki, że dla wierzchołków  krawędź  wtedy i tylko wtedy, gdy graf G zawiera ścieżkę między u i v złożoną z co najwyżej dwóch krawędzi.

Napisz program, który dla grafu podanego jako lista sąsiedztwa, wypisze jego kwadrat. 

Bierzemy tu pod uwagę grafy nieskierowane jak i skierowane.

Wskazówka: Najprostszej zrobić następującą operację na macierzach. Jeśli macierz sąsiedztwa oznaczymy jako A, to kwadrat grafu

Sample Input 1:

1 2
2 1 3
3 2 4
4 3
Sample Output 1:

1 2 3
2 1 3 4
3 1 2 4
4 2 3
Sample Input 2:

1 2
2 3
3 4
4
Sample Output 2:

1 2 3
2 3 4
3 4
4