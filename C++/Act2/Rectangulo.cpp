#include <iostream>
using namespace std;

int main(){
    double altura, base, area;
    cout << "....Area Rectangulo...." << endl;
    cout << "Ingrese la altura: ";
    cin >> altura;
    cout << "Ingrese la base: ";
    cin >> base;
    area = altura*base;
    system("cls");
    cout << "....Area Rectangulo" << endl;
    cout << "Figura: Rectangulo \nArea Calculada: " << area << endl;
    system("pause");
    return 0;
}