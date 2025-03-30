#include <iostream>
#include <string>
using namespace std;

int main(){
    int lista[5] = {0,1,1,0,0};
    int sizeLista = sizeof(lista)/ sizeof(lista[0]);
    
    for (int indice = 1; indice <= sizeLista; indice++)
    {
        cout << indice << ". "<< lista[indice] << endl;
    }
    
    return 0;
}