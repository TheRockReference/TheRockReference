#include <iostream>
//la ligne suivante permet d'eviter d'avoir a ecrire std::cout ou std::cin
using namespace std ;
int main()
{   char op ;
    int n1, n2 ;
    //cout sert a ecrire des informations, c'est un flot de sortie
    cout << "operation souhaitee (+ ou *) ? " ;
    //cin sert 'a lire des informations, c'est un flot d'entree. Il saisie ce que l'utilisateur tape au clavier
    //dans ce cas-ci, il l'enregistre dans la variable op
    cin >> op ;
    cout << "donnez 2 nombres entiers : " ;
    cin >> n1 >> n2 ;
    if (op == '+') cout << "leur somme est : " <<n1+n2 << "\n" ;
        else cout << "leur produit est : " << n1*n2 << "\n" ;
}
