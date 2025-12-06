import sys
import math

def main():
    file_name, line_count = sys.argv[1], int(sys.argv[2])
    total = 0

    # Step 0: Parse input
    operands_line = []
    number_lines = []
    with open(file_name, "r") as file:
        for _ in range(line_count):
            number_lines.append(file.readline().strip("\n"))
        operands_line = file.readline()

    # Step 1: Find starting indices of columns
    starting_indices = []
    with open(file_name, "r") as file:
        for i in range(len(operands_line)):
            c = operands_line[i]
            if c != " ":
                starting_indices.append(i)

    # Add last index
    starting_indices.append(len(operands_line) + 1)

    # Step 2: 
    for i in range(len(starting_indices) - 1):
        idx, next_idx = starting_indices[i], starting_indices[i + 1]
        numbers = []
        
        # Process number lines
        for j in range(next_idx - 2, idx - 1, -1):
            number_str = ""
            for k in range(0, len(number_lines)):
                number_line = number_lines[k]
                number_str += number_line[j]
            number = int(number_str)
            numbers.append(number)

        # Calculate result
        operand = operands_line[idx]
        if operand == "+":
            result = sum(numbers)
        elif operand == "*":
            result = math.prod(numbers)
        total += result
       
    print(total)

if __name__ == "__main__":
    main()