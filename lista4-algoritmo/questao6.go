package main

import "fmt"

func main() {

	for i := 0; i <= 200; i++ {
		if i%5 == 0 {
			fmt.Println(i)
		}
	}
}
