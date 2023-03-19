Zadanie 3 (2 pkt)

Grafem krawędziowym  grafu prostego  nazywamy graf, którego wierzchołki stoją we wzajemnie jednoznacznej odpowiedniości z krawędziami grafu G i taki, że jego wierzchołki są sąsiednie wtedy i tylko wtedy, gdy odpowiadające im krawędzie grafu są sąsiednie.

Napisz program, który dla grafu podanego jako lista sąsiedztwa, wypisze jego graf krawędziowy. 

Aby wykonać poprawnie to zadanie zakładamy, że lista sąsiedztwa grafu krawędziowego składa się z par wierzchołków o następującym formacie:

(1, 2) (2, 3)
(2, 3) (1, 2) (3, 4)
(3, 4) (2, 3)
Powyższa lista oznacza, że wierzchołek (krawędź (1,2)) jest połączony z wierzchołkiem (krawędzią (2,3)), itd.

Należy posortować tę listę po kluczach (pierwszej wartości)!!!

Sample Input 1:

1 2
2 1 3
3 2 4
4 3
Sample Output 1:

(1, 2) (2, 3)
(2, 3) (1, 2) (3, 4)
(3, 4) (2, 3)
Sample Input 2:

1 2
2 3
3 4
4
Sample Output 2:

(1, 2) (2, 3)
(2, 3) (3, 4)
(3, 4)