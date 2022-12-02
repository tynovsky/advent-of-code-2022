package main

import (
	"bufio"
	"fmt"
	"os"
	"io"
	"strconv"
)

func main() {
	var reader = bufio.NewReader(os.Stdin)

	mostCalories := 0
	currentCalories := 0
	for { 
		line, err := reader.ReadString('\n')
		// fmt.Print(line)
		if err == io.EOF {
			if currentCalories > mostCalories {
				mostCalories = currentCalories
			}
			break
		}
		if err != nil {
			panic(err)
		}
		if line == "\n" {
			if currentCalories > mostCalories {
				mostCalories = currentCalories
			}
			currentCalories = 0
			continue
		}

		calories, _ := strconv.Atoi(line[:len(line)-1])
		currentCalories = currentCalories + calories
		// fmt.Println(currentCalories)
	}
	fmt.Println(mostCalories)
}





