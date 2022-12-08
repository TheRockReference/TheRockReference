#include <iostream>
using namespace std ;
int main ()
{  int n ; 
    cout << "donnez un entier : " ;
    cin >> n ;
    switch (n)
    {   case 0 : cout << "nul\n" ;
        break ;
        case 1 : cout << "un\n" ;
        break ;
        case 2 : cout << "deux\n" ;
        break ;
        case 99999999 : cout << "gros nombre\n" ;
        break ;
        default : cout << "autre nombre\n" ;
    }
    cout << "au revoir\n" ;
}
