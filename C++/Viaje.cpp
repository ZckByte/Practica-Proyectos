#include <iostream>
#include <string>
using namespace std;

int main()
{
    std::string seleccion;
    std::string vip;
    int dinero;
    //Cali a Bogotá, medellín,Pereira y Pasto
    cout << "== RUTAS ==" << endl;
    cout << "1. Cali a Bogotá $1000 \n2. Cali a Medellín $2000" << endl;
    cout << "3. Cali a Pereira $500 \n4. Cali a Pasto $1500" << endl;
    cout << "Asiento VIP $1000" << endl;
    cout << "Cantidad de dinero: $";
    cin >> dinero; //Input que se utilizara para mostrar las diferentes opciones dependiendo de la cantidad
    if (dinero > 1500){//Asiento vip, si se tiene más de 1500
        cout << "== VIP ==" << endl;
        cout << "1. Si\n2. No\nDesea agregar el asiento VIP ($"<<dinero << " - $1000) ?: ";
        cin >> vip;
        if ((vip == "1") || (vip == "si") || (vip == "Si")){
            dinero = dinero - 1000;//Le resta al dinero original el valor del vip
        }
    }
    //Condicionales del prompt dinero
    if(dinero < 500){
        cout << "No tienes suficiente dinero pasa viajar." << endl;
        return 0;
    }else if((dinero >= 500) && (dinero < 1000)){
        cout << "" << endl;    
        cout << "Dinero: $" << dinero << endl;
        cout << "Puedes viajar a:" << endl;
        cout << "1. Pereira" << endl;
    }else if(dinero < 1500){
       cout << "" << endl;
       cout << "Dinero: $" << dinero << endl;
       cout << "Puedes viajar a:" << endl;
       cout << "1. Pereira\n2. Bogota" << endl;
    }else if(dinero < 2000){
       cout << "" << endl;
       cout << "Dinero: $" << dinero << endl;
       cout << "Puedes viajar a:" << endl;
       cout << "1. Pereira\n2. Bogota\n3. Pasto" << endl;
    }else{
       cout << "" << endl;
       cout << "Dinero: $" << dinero << endl;
       cout << "Puedes viajar a:" << endl;
       cout << "1. Pereira\n2. Bogota\n3. Pasto\n4. Medellín" << endl;
    }
    cout << " " << endl;
    cout << "Hacia donde se dirige?: ";
    cin >> seleccion; //Selección de viaje 
    if (seleccion == "1") {
        seleccion = "Pereira";
        dinero = dinero - 500;
    } else if (seleccion == "2") {
        seleccion = "Bogotá";
        dinero = dinero - 1000; //Se resta el dinero de la ruta, al dinero original
    } else if (seleccion == "3") {
        seleccion = "Pasto";
        dinero = dinero - 1500;
    } else if (seleccion == "4") {
        seleccion = "Medellín";
        dinero = dinero - 2000;
    } else {
        seleccion = "Opción no válida";
        return 0;
    }
    cout << " " << endl;
    cout << "Disfrute de su viaje hacia " << seleccion << ", Su saldo restante es de: $" <<dinero << endl;
    return 0;
}