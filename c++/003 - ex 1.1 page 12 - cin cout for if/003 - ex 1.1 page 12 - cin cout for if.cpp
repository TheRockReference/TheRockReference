#include <iostream>
#include <cmath>
using namespace std ;
int main()
{   int i ;
    float x ;
    float racx ;
    const int NFOIS = 5 ;
    cout << "Bonjour\n" ;
    cout << "Je vais vous calculer " << NFOIS << " racines carree\n" ;
    for (i=0 ; i<NFOIS ; i++)
    {    cout << "Donnez un nombre : ";
       cin >> x ;
        if (x < 0.0)
            cout << "Le nombre " << x << "ne possede pas de racine carre\n" ;
        else
        { racx = sqrt (x) ;
        cout << "Le nombre " << x << " a pour racine carree : " << racx << "\n" ;
        }
    }
    cout << "Traval termine - au revoir " ;
}
