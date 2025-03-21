#include <iostream>
using namespace std;

int main(){
    double altura, base, area;
    cout << "....Area Triangulo...." << endl;
    cout << "Ingrese la altura: ";
    cin >> altura;
    cout << "Ingrese la base: ";
    cin >> base;
    area = (altura*base)/2;
    system("cls");
    cout << "....Area...." << endl;
    cout << "Figura: Triangulo \nArea Calculada: " << area << endl;
    system("pause");
    return 0;
}