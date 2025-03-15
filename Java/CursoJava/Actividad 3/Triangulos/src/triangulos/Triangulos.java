package triangulos;
import java.util.Scanner;
public class Triangulos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String tipo = "";
        double cosA,cosB,cosC,area,s = 0;
        double angA,angB,angC = 0;       
        //Triangulo equilatero = Todas medidas iguales
        //Triangulo isóceles = que tiene al menos dos lados de igual longitud
        //Tringulo escaleno = todos sus lados y ángulos son diferentes

        System.out.println("....Equilatero, Isoceles, Escaleno....");
        System.out.println("Ingrese las medida del triangulo: ");
        System.err.print("a: ");
        int a = Integer.parseInt(sc.nextLine());
        System.err.print("b: ");
        int b = Integer.parseInt(sc.nextLine());
        System.err.print("c: ");
        int c = Integer.parseInt(sc.nextLine());

        //If para ver que tipo de triangulo es
            //Equilatero
        if((a == b) && (b == c) && (c == a)){
            System.out.println("El triangulo es EQUILATERO");
            tipo = "equilatero";
        }
            //Isóceles 
        else if((a == b) && (b == a) || (c == b) && (b == c) || (a == c) && (c == a)){
            System.out.println(("El triangulo es iSOCELES"));
            tipo = "isoceles";
            //Escaleno
        }else if((a != b) && (b != c) && (c != b)){
            System.out.println("EL triangulo es ESCALENO");
            tipo = "escaleno";
        }
        //Switch para medidas de angulos
        System.out.println("\n1. A\n2. B\n3. C\nQue angulo desea conocer?: ");
        int coseno = Integer.parseInt(sc.nextLine());

        if(tipo == "equilatero"){//En un triangulo equilatero todos los angulos miden 180°
            switch (coseno) {
                case 1,2,3:
                    s = (a + b + c) / 2; //Formula Herón
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("Cada ángulo de un triangulo equilatero mide 60°, tiene un area de " + area);
                    break;
            }
        }else if(tipo == "isoceles"){
            switch (coseno) {
                case 1:
                    cosA = (Math.pow(b, 2) + Math.pow(c, 2) - Math.pow(a, 2)) / (2 * b * c); //Formula de cosenos
                    angA = Math.round(Math.toDegrees(Math.acos(cosA))); //Se convierte en angulo, y se redondea
                    s = (a + b + c) / 2;
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("El angulo A de este triangulo " + tipo + " es " + angA +"°, con un area de " + area);
                    break;
                case 2:
                    cosB = (Math.pow(a, 2) + Math.pow(c, 2) - Math.pow(b, 2)) / (2 * a * c);
                    angB = Math.round(Math.toDegrees(Math.acos(cosB)));
                    s = (a + b + c) / 2;
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("El angulo B de este triangulo " + tipo + " es " + angB +"°, con un area de " + area);
                    break;
                case 3:
                    cosC = (Math.pow(a, 2) + Math.pow(b, 2) - Math.pow(c, 2)) / (2 * a * b); 
                    angC = Math.round(Math.toDegrees(Math.acos(cosC)));
                    s = (a + b + c) / 2;
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("El angulo C de este triangulo " + tipo + " es " + angC +"°, con un area de " + area);
            }
        }else if (tipo == "escaleno") {
            switch (coseno) {
                case 1:
                    cosA = (Math.pow(b, 2) + Math.pow(c, 2) - Math.pow(a, 2)) / (2 * b * c);
                    angA = Math.round(Math.toDegrees(Math.acos(cosA)));
                    s = (a + b + c) / 2;
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("El angulo A de este triangulo " + tipo + " es " + angA +"°, con un area de " + area);
                    break;
                case 2:
                    cosB = (Math.pow(a, 2) + Math.pow(c, 2) - Math.pow(b, 2)) / (2 * a * c);
                    angB = Math.round(Math.toDegrees(Math.acos(cosB)));
                    s = (a + b + c) / 2;
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("El angulo B de este triangulo " + tipo + " es " + angB +"°, con un area de " + area);
                    break;
                case 3:
                    cosC = (Math.pow(a, 2) + Math.pow(b, 2) - Math.pow(c, 2)) / (2 * a * b); 
                    angC = Math.round(Math.toDegrees(Math.acos(cosC)));
                    s = (a + b + c) / 2;
                    area = Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)));
                    System.out.println("El angulo C de este triangulo " + tipo + " es " + angC +"°, con un area de " + area);
            }
        }
        sc.close();
    }

    
}
