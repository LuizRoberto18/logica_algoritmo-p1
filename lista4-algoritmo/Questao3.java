public class Questao3 {
    public static void main(String[] args) {
        int soma = 0;
        int contador = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 2 == 0) {
                soma += i;
                contador++;
            }
        }

        // Calcular a média
        double media = (double) soma / contador;

        System.out.println("A média dos números pares de 1 a 100 é: " + media);
    }
}
