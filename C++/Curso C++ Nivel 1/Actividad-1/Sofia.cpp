#include <iostream>
#include <string>
using namespace std; 

//Alan Alzate

int main(){
	int referencia,talla, costo, precio;
	string descripcion;
	char disponibilidad;
	cout << "ADMINISTRDOR DE VENTAS" << endl;
	cout << "Ingrese la referencia del zapato: " << endl;
	cin >> referencia;
	cin.ignore();
	cout << "Ingrese una descripcion del zapato: " << endl;
	getline(cin, descripcion);
	cout << "Ingrese la talla: " << endl;
	cin >> talla;
	cout << "Ingrese la letra si esta disponible o no para la venta S/N" << endl;
	cin >> disponibilidad;
	cout << "Ingrese el costo del zapato: " << endl;
	cin >> costo;
	cout << "Ingrese el precio de venta: " <<  endl;
	cin >> precio;
	system("cls");
	cout << "LOS DATOS REGISTRADOS SON LOS SIGUIENTES" << endl;
	cout << "\nREFERENCIA: " << referencia << endl;
	cout << "Descripcion: " << descripcion << endl;
	cout << "TALLA: " << talla << endl;
	cout << "DISPONIBILIDAD: " << disponibilidad << endl;
	cout << "COSTO: " << costo << endl;;
	cout << "PRECIO DE VENTA: " << precio << endl;
	cout << "\nGracias por la informacion" << endl;
	cout << "Alan Alzate"
	return 0;
}