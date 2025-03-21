#include <iostream>
using namespace std;

int main(){
    double diag_mayor, diag_menor, area;
    cout << "....Area Rombo...." << endl;
    cout << "Ingrese la Diagonal Mayor: ";
    cin >> diag_mayor;
    cout << "Ingrese la Diagonal Menor: ";
    cin >> diag_menor;
    area = (diag_mayor*diag_menor)/2;
    system("cls");
    cout << "....Area...." << endl;
    cout << "Figura: Rombo \nArea Calculada: " << area << endl;
    system("pause");
    return 0;
}