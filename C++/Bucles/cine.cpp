#include <iostream>
#include <string>
#include <unistd.h>

using namespace std;
// Ejercicio 1: Reservación de asientos en un cine 🎬 
// Crea un programa que simule la reservación de asientos en una 
// sala de cine con 15 asientos (0 = libre, 1 = ocupado). El programa debe:
// - Mostrar los asientos disponibles. ✅
// - Permitir al usuario elegir un asiento.✅
// - Evitar seleccionar asientos ocupados.✅
// - Finalizar cuando todos los asientos estén ocupados. ✅
// Extra: Permitir que un usuario reserve más de un asiento por compra.
int main(){
    int asiento_escogido;; //El asiento que luego va a escoger el usuario
    int cantidad = 1; //cantidad de asientos que va a ocupar, 1 por defecto
    int libres = 15; //Luego se resta para saber cuantos asientos libres quedan
    int suma = 0; //Se utiliza para la cantidad de vueltas que dio el programa
    int asientos[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; //se incia en 16 porque sino en donde muestra los asientos libres el ultimo queda ocupado
    int len_asientos = sizeof(asientos)/ sizeof(asientos[0]); //sizeof(arr) devuelve el tamaño en bytes y sizeof(arr[0]) de un solo elemento
    
    //Verfica si el array asientos tiene un valor diferente a 0, si lo tiene es porque el asiento esta ocupado
    while (true) //Se ejecutara hasta que haya un break
    {
        cout << "....Reservacion Cine...." << endl;
        cout << "Asientos Libres: " << endl;
        for(int i = 1; i <= 15; i++){ //se itera hasta 15
            if(asientos[i] == 0){ //Si el indice en el que esta, el contenido es 0, esta libre
                cout << i << ". Libre" << endl; //Asiento libre
            }
            if(asientos[i] == 1){ //Si el indice en el que esta, el contenido es 1, esta ocupado
                cout << i << ". Ocupado" << endl; // Asiento Ocupado
            }
        }
        cout << "Cantidad de asientos a reservar: ";
        cin >> cantidad;
        if(cantidad < 1 || cantidad > 15 || cantidad > libres ){ //Si es menor a 1, mayor a 15, mayor a los asientos libres
            cout << "Numero Invalido." << endl; //Es una operacion invalida
            sleep(2);
            system("cls");
            continue; //vuelve a la linea 27
        }
        for (int i = 0; i < cantidad; i++) //Se repite la cantidad de asientos que se desee reservar
        {
            cout << "Elija un asiento: ";
            cin >> asiento_escogido;
            if(asiento_escogido > 15 || asiento_escogido < 1 || asientos[asiento_escogido] == 1){ //Si el asientos escogido es menor a 1, mayor a 15 o el lugar ya esta ocupado(1)
                cout << "Puesto Invalido." << endl; //El puesto es invalido
                sleep(2);
                system("cls");
                continue;//Vuelve a la linea 27
            }else{
                cout << "Reservador Correctamente. Llene todos los asientos." << endl;
                suma += 1; //La suma es un verificador para saber si se reservaron todos los asientos
                            //Lo hago con una suma porque despues de las anteriores verificaciones
                            //el unico camino es que todos los parametros esten bien ingresados
                sleep(1); //Un delay de la consola (tiempo de espera)
                for(int i = 1; i <= 15; i++){ //Se repite 15 veces
                    if(i == asiento_escogido){//Aca como i se incrementa en cada vuelta, hasta que "i" sea
                                            //igual al asiento escogido, como son 15, se itera hasta 15.
                                            //cuando llegue al asiento escogido
                        asientos[i] = 1;//Se remplazara el contenido por 1(ocupado)
                        break;//Se rompre el bucle
                    }
                }
            }
            if(suma == 15){ //Si la cantidad de asientos ocupados es 15, se termina el programa
                cout << "Se han llenado todos los asientos, disfrute de su viaje!" << endl;
                sleep(3);
                break;
            }
            libres -= 1; //Esto indica que se realizo una vuelta al bucle, por lo que, se ocuparon 1 asiento o 2
            //ya que se ejecuta una vuelta a la vez
        }
        system("cls"); //Borra la consola 
    }
    return 0;
}