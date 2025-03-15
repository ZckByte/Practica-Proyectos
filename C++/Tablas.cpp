#include <iostream>
using namespace std;

int main(){
    int numero;
    cout << "\n1.Tabla del 1\n2.Tabla del 2\n"<<endl;
    cout << "Seleccione una tabla: ";
    cin >> numero;
    for (int i = 1; i <= 10; i++){
        cout << numero << "x" << i << "=" << numero*numero <<endl;
    }
    return 0;
}