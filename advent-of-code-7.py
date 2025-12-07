import sys

def main():
    # Step 1: Parse input
    file_name = sys.argv[1]
    input = []
    start_col = 0
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            input_row = []
            for i in range(len(line)):
                char = line[i]
                if char == "S":
                    star_col = i
                    input_row.append(1)
                elif char == ".":
                    input_row.append(0)
                else:
                    input_row.append("^")
            input.append(input_row)

    # Step 2: Perform dp
    for i, current_row in enumerate(input):
        if i == 0:
            continue
        
        prev_row = input[i - 1]
        for j in range(len(current_row)):
            # Special case
            if current_row[j] == "^":
                current_row[j - 1] += prev_row[j]
                current_row[j + 1] += prev_row[j]
                current_row[j] = 0
            else:
                current_row[j] += prev_row[j]

    return sum(input[-1])

if __name__ == "__main__":
    result = main()
    print(result)