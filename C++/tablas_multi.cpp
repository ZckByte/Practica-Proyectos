#include <iostream>
#include <string>
using namespace std;

int tablas(int num){
    int i, resultado;
    for (i = 1;i <= 10;i++)
    {
        resultado = num * i;
        cout << num << "x" << i << ": " << resultado << endl;
    }
    
}

int main(){
    int tabla;
    string seguir;
    while (true)
    {
        cout << "Seleccione la tabla de multiplicacion: ";
        cin >> tabla;
        tablas(tabla);
        cout << "Desea seguir? S/N: ";
        cin >> seguir;
        if ((seguir == "s") || (seguir == "S")){
            system("cls");
            continue;
        }else{
            cout << "!Gracias Por Usar!" << endl;
            break;
        }
    }
}