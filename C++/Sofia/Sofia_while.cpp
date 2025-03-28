#include <iostream>
#include <string>
using namespace std; 

int main(){
	int talla, costo, referencia;
	string descripcion, registrar;
    int conta = 0;
    string otro = "OTRO";
	string un_otro;
    while (true)
    {
		if(conta == 0){
        	cout << "Desea registrar un zapato s/n: " ;   
		}else{
        	cout << "Desea registrar OTRO zapato s/n: " ;
		}
        cin >> un_otro;
        cout << "" << endl; 
        if(un_otro == "n"){
        	break;
		}
        cout << "Ingrese la referencia del zapato: ";
        cin >> referencia;
        cin.ignore();
        cout << "Ingrese una descripcion del zapato: ";
        getline(cin, descripcion);
        cout << "Ingrese la talla: ";
        cin >> talla;
        cout << "Ingrese el costo del zapato: ";
        cin >> costo;
        conta = 1;
        cout << "" << endl; 
    }
	cout << "\nGracias por la informacion" << endl;
	return 0;
}