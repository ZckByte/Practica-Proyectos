#include <iostream>
#include <string>
#include <unistd.h>

using namespace std;
// Ejercicio 1: Reservación de asientos en un cine 🎬 (Ejercicio de chatgpt)
// Crea un programa que simule la reservación de asientos en una 
// sala de cine con 15 asientos (0 = libre, 1 = ocupado). El programa debe:
// - Mostrar los asientos disponibles. ✅
// - Permitir al usuario elegir un asiento.✅
// - Evitar seleccionar asientos ocupados.✅
// - Finalizar cuando todos los asientos estén ocupados.
// Extra: Permitir que un usuario reserve más de un asiento por compra.

bool esUno(int lista[], int array_size){
    for(int i = 1; i >= array_size; i++){
        if(lista[i] != 1){
            return false;
        }
    }
    return true;
}
int main(){
    cout << "....Reservacion Cine...." << endl;
    cout << "Asientos Libres: " << endl;
    int asiento_escogido;
    bool todos_ocupados = true;
    int suma = 0;
    int asientos[15] = {1,1,1,1,1,1,1,0,1,1,1,1,1,1,1};
    int len_asientos = sizeof(asientos)/ sizeof(asientos[0]); //sizeof(arr) devuelve el tamaño en bytes y sizeof(arr[0]) de un solo elemento
    
    //Verfica si el array asientos tiene un valor diferente a 0, si lo tiene es porque el asiento esta ocupado
    while (todos_ocupados)
    {
        for(int i = 0; i <= len_asientos; i++){
            if(asientos[i] == 0){
                cout << i << ". Libre" << endl; //Asiento libre
            }else{
                cout << i << ". Ocupado" << endl; // Asiento Ocupado
            }
        }
        cout << "Elija un asiento: ";
        cin >> asiento_escogido;
        if(asiento_escogido > len_asientos){
            cout << "Puesto Invalido." << endl;
            continue;
        }else{
            cout << "Reservador Correctamente. Llene todos los asientos" << endl;
        }
        for(int i = 1; i <= len_asientos; i++){
            if(i == asiento_escogido){
                asientos[i] = 1;
                break;
            }
        }
        for(int i = 0; i < len_asientos; i++){
            if(asientos[i] == 1){
                todos_ocupados = false;
            }

        }
    }
    cout << "se termino" << endl;
    return 0;
}