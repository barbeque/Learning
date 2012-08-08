package main
import "fmt"

func main() {
	if v := 5; v < 10 {
		fmt.Printf("v=", v)
	}
	fmt.Printf("v doesn't exist in this scope anymore\n")
}