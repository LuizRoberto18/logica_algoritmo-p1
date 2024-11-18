public class Questao2 {
    public static void main(String[] args) {
        int soma = 1;
        for (int i = 1; i < 100; i++) {
            if (i % 2 == 0) {
                soma += i;
            }
        }

        System.out.println("a soma dos pares é:" + soma);
    }
}
