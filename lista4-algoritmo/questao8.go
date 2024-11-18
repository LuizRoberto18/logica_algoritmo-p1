package main

import "fmt"

func main() {

	for i := 1000; i <= 2000; i++ {
		if i%11 == 5 {

			fmt.Println(i)
		}
	}
}
