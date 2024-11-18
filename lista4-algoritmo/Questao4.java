import java.util.Scanner;

public class Questao4 {
    public static void main(String[] args) {
        int x, y, soma = 0;

        Scanner scan = new Scanner(System.in);

        // Entrada dos números
        System.out.print("Digite o valor de x: ");
        x = scan.nextInt();

        System.out.print("Digite o valor de y: ");
        y = scan.nextInt();

        // Definir os limites do intervalo
        int menor = Math.min(x, y);
        int maior = Math.max(x, y);

        // Somar os números ímpares no intervalo (excluindo os limites)
        for (int i = menor + 1; i < maior; i++) {
            if (i % 2 == 1) {
                soma += i;
            }
        }

        // Exibir o resultado
        System.out.println("A soma dos números ímpares entre " + x + " e " + y + " é: " + soma);

        scan.close();
    }
}
