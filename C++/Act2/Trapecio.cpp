#include <iostream>
using namespace std;

int main(){
    double base_mayor, altura , base_menor, area;
    cout << "....Area Trapecio...." << endl;
    cout << "Ingrese la Base Mayor: ";
    cin >> base_mayor;
    cout << "Ingrese la Base Menor: ";
    cin >> base_menor;
    cout << "Ingrese la Altura: ";
    cin >> altura;
    area = ((base_mayor+base_menor)/2)*altura;
    system("cls");
    cout << "....Area...." << endl;
    cout << "Figura: Paralelogramo \nArea Calculada: " << area << endl;
    system("pause");
    return 0;
}