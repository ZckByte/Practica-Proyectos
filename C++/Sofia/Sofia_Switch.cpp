#include <iostream>
#include <string>
using namespace std; 

int main(){
	int referencia,talla, costo, precio_total, costo_total;
    int precio,cantidad, utilidad_total, utilidad_unidad, categoria;
	float porcen_util;
	string descripcion,tipo;
	char disponibilidad;
	cout << "ADMINISTRDOR DE VENTAS" << endl;
	cout << "Ingrese la referencia del zapato: ";
	cin >> referencia;
	cin.ignore();
	cout << "Ingrese una descripcion del zapato: ";
	getline(cin, descripcion);
	cout << "Ingrese la talla: ";
	cin >> talla;
	cout << "Ingrese la letra si esta disponible o no para la venta S/N: ";
	cin >> disponibilidad;
	cout << "Ingrese la cantidad de zapatos: ";
	cin >> cantidad;
	cout << "Ingrese el costo del zapato: ";
	cin >> costo;
	cout << "Ingrese el precio de venta: ";
	cin >> precio;
	precio_total = precio*cantidad;
	utilidad_unidad = precio - costo;
	utilidad_total = utilidad_unidad*cantidad;
	costo_total = costo*cantidad;
	//porcen_util = ((float)utilidad_unidad / costo) * 100;
    if (costo <= 30000){
        categoria = 1;
    }else if ((costo >= 30000) && (costo <= 60000)){  
        categoria = 2;
    }else{
        categoria = 3;
    }  
    switch (categoria)
    {
    case 1:
        tipo = "A";
        porcen_util = 50;
        break;
    case 2:
        tipo = "B";
        porcen_util = 40;
        break;
    case 3:
        tipo = "C";
        porcen_util = 30;
        break;
    default:
        break;
    }
	system("cls");
	cout << "LOS DATOS REGISTRADOS SON LOS SIGUIENTES" << endl;
	cout << "\nReferencia: " << referencia << endl;
	cout << "Descripcion: " << descripcion << endl;
    cout << "Tipo: " << tipo << endl;
	cout << "Talla: " << talla << endl;
	cout << "Disponibilidad: " << disponibilidad << endl;
	cout << "Costo por unidad: " << costo << endl;
	cout << "Costo Total: " << costo_total << endl;
	cout << "Precio Por unidad: " << precio << endl;
	cout << "Precio total de " << cantidad << " Unidades: " << precio_total << endl;
	cout << "Utilidad por Unidad: " << utilidad_unidad << endl;
	cout << "Utilidad Total: " << utilidad_total << endl;
	cout << "Porcentaje de Utilidad: " << porcen_util << endl; 
	cout << "\nGracias por la informacion" << endl;
	system("pause");
	return 0;
}