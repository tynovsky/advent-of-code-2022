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

	mostCalories := [3]int{0, 0, 0}
	currentCalories := 0
	for { 
		line, err := reader.ReadString('\n')
		fmt.Println(line)
		fmt.Println(mostCalories)
		if err == io.EOF {
			for i := 0; i < 3; i++ {
				if currentCalories > mostCalories[i] {
					for j := i+1; j < 3; j++ {
						mostCalories[j] = mostCalories[j-1]
					}
					mostCalories[i] = currentCalories
					break
				}
			}
			break
		}
		if err != nil {
			panic(err)
		}
		if line == "\n" {
			for i := 0; i < 3; i++ {
				if currentCalories > mostCalories[i] {
					for j := 2; j > i; j-- {
						mostCalories[j] = mostCalories[j-1]
					}
					mostCalories[i] = currentCalories
					break
				}
			}
			currentCalories = 0
			continue
		}

		calories, _ := strconv.Atoi(line[:len(line)-1])
		currentCalories = currentCalories + calories
	}

	sum := 0
	for _, c := range(mostCalories) {
		sum = sum + c
	}
	fmt.Println(sum)
}





