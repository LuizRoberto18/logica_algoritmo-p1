import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int pares = 0, impares = 0, positivos = 0, negativos = 0;

        System.out.println("Digite 5 valores inteiros:");

        for (int i = 1; i <= 5; i++) {
            System.out.print("Valor " + i + ": ");
            int a = scanner.nextInt();

            // Verificar se é par ou ímpar
            if (a % 2 == 0) {
                pares++;
            } else {
                impares++;
            }

            // Verificar se é positivo ou negativo
            if (a > 0) {
                positivos++;
            } else if (a < 0) {
                negativos++;
            }
        }

        // Exibir resultados
        System.out.println("\nResultados:");
        System.out.println("Quantidade de números pares: " + pares);
        System.out.println("Quantidade de números ímpares: " + impares);
        System.out.println("Quantidade de números positivos: " + positivos);
        System.out.println("Quantidade de números negativos: " + negativos);

        scanner.close();
    }
}
