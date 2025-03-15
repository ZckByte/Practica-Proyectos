import java.util.Scanner;
import java.util.ArrayList;

public class Promedio {
    public static void main(String[] args) throws Exception {
        ArrayList<Double> lista = new ArrayList<>(); 
        Scanner sc = new Scanner(System.in);
        int contEst = 0;
        double matematicas = 0;
        double definitiva = 0;
        int seleccion = 0;
        String asignatura = ""; //Para qué en la aplicación se puedan agregar mas materias 
        //Recibir la infomacion de las notas de los estudiantes, para tres materias
        System.out.println(("\n....Promedio...."));
        System.out.print("Cantidad de estudiantes: ");
        int canEst = sc.nextInt(); //Cantidad de estudiantes
        sc.nextLine();
        System.out.print("1. Matematicas\n2. Español\n3. Ingles\nQue materia desea saber el promedio: ");
        seleccion = sc.nextInt();
        sc.nextLine();
        switch (seleccion) {
            case 1:
                //Promedio de matematicas con bucle for
                asignatura = "matematicas";     //Aca se redefine asignatura para usarlo en el print final
                System.out.println("Matematicas: ");
                for (int i = 1; i <= canEst; i++){
                    System.out.print(("Promedio de Estudiante #"+i+":"));
                    matematicas = sc.nextDouble();
                    lista.add(matematicas); //Se agrega a la lista vacia
                }
                for (double notas : lista){
                    definitiva += notas; //Se recorre la lista y se suma a la variable definitiva
                }
                definitiva = definitiva / canEst; //Para sacar el promedio, se divide la suma por la cantidad de estudiantes
                break;
            case 2:
                asignatura = "español";
                //Promedio de Español con while
                System.out.println("Español: ");
                while (true) {
                    if(contEst == canEst){  //Correra hasta que llegue a la cantidad de estudiantes
                        break;              
                    }
                    System.out.print("Promedio de Estudiante #"+ (contEst+1) + ": ");
                    double español = sc.nextDouble();
                    definitiva += español;
                    contEst = contEst + 1; //Para contar cada recorrido de codigo
                }
                definitiva = definitiva / canEst;
                break;
            case 3:
                contEst = 1;   //Se redefine porque la variable esta inicializada en 0, se ejecutaria un vez mas, si no se refediniera
                asignatura = "ingles";      
                System.out.println("Ingles: ");
                do {
                    System.out.print("Promedio de Estudiante #"+ (contEst)+ ": ");
                    double ingles = sc.nextDouble();
                    definitiva += ingles;
                    contEst++;
                } while (contEst <= canEst); //correra hasta se igual o mayyor a la cantidad
                    definitiva = definitiva / canEst;
                    break;
                }
        String formato = String.format("%.2f", definitiva); //Se utiliza String.Format porque con Math.Round() lo redondea hacia el numero mas cercano
        System.out.println("El promedio de  "+ asignatura +" de los " + canEst +" estudiantes, es de : " + formato);
        sc.close();
    }
}
