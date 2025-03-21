#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

int main(){
    double radio;
    double pi = M_PI;
    float area;
    cout << "....Area Circulo...." << endl;
    cout << "Ingrese el radio: ";
    cin >> radio;
    area = pi*pow(radio,2);
    system("cls");
    cout << "....Area...." << endl;
    cout << "Figura: Circulo \nArea Calculada: " << area << endl;
    system("pause");
    return 0;
}