package main

import "fmt"

func main() {
	var num int
	fmt.Print("Digite um número: ")
	fmt.Scan(&num)

	if num <= 0 {
		fmt.Println("O número deve ser maior que zero.")
		return
	}

	// Calcula a soma dos divisores
	somaDivisores := 0
	for i := 1; i <= num/2; i++ {
		if num%i == 0 {
			somaDivisores += i
		}
	}

	// Verifica se o número é perfeito
	if somaDivisores == num {
		fmt.Printf("%d é um número perfeito!\n", num)
	} else {
		fmt.Printf("%d não é um número perfeito.\n", num)
	}
}
