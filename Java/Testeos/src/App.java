import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        double definitiva = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese cantidad: ");
        double cantidad = sc.nextDouble();
        sc.nextLine();
        System.out.println("Cantidad: ");
        double cantidad2 = sc.nextDouble();
        sc.nextLine();
        for (int i = 0; i <= cantidad; i++){
            definitiva += cantidad2;
            System.out.println(definitiva);
        }

        sc.close();
    }
}
