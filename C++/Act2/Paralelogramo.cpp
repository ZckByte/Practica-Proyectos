#include <iostream>
using namespace std;

int main(){
    double altura, base, area;
    cout << "....Area Paralelogramo...." << endl;
    cout << "Ingrese la altura: ";
    cin >> altura;
    cout << "Ingrese la base: ";
    cin >> base;
    area = (altura*base);
    system("cls");
    cout << "....Area...." << endl;
    cout << "Figura: Paralelogramo\nArea Calculada: " << area << endl;
    system("pause");
    return 0;
}