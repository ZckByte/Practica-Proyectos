#include <iostream>
using namespace std;
//Chatgpt
int main() {
    int puestos[10] = {0,0,0,0,0,0,0,0,0,0};
    int puestoSeleccionado;
    bool todosOcupados = false;
    cout << "....RUTABUS...." << endl; 
    cout << "Ruta: Cali a Pasto" << endl; 
    while (!todosOcupados) { 
        cout << "\nLos puestos libres son: " << endl;
        for (int i = 0; i < 10; i++) {
            if (puestos[i] == 0) {
                cout << "Puesto " << i << " (Libre)" << endl;
            }
        }
        cout << "Escoja su puesto: "; 
        cin >> puestoSeleccionado;
        if (puestoSeleccionado >= 0 && puestoSeleccionado < 10 && puestos[puestoSeleccionado] == 0) {
            puestos[puestoSeleccionado] = 1;
            cout << "Puesto " << puestoSeleccionado << " reservado." << endl;
        } else {
            cout << "Puesto ya ocupado." << endl;
        }
        todosOcupados = true; 
        for (int i = 0; i < 10; i++) {
            if (puestos[i] == 0) { 
                todosOcupados = false;
                break;
            }
        }
    }
    cout << "\nTodos los puestos estan ocupados. " << endl;
    return 0;
}