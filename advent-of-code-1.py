import sys

def main():
    file_name = sys.argv[1]

    input = []

    # Parse input
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            (direction, number) = line[0], int(line[1:])
            input.append((direction, number))

    # Process input
    current_position = 50
    result = 0

    for (direction, number) in input:
        pos_before = current_position

        result += number // 100
        number = number % 100

        # Perform turn
        if direction == "R":
            current_position += number
        elif direction == "L":
            current_position -= number

        if pos_before < 100 and current_position > 100:
            result += 1
        if pos_before > 0 and current_position < 0:
            result += 1

        # Adjust position
        if current_position >= 100:
            current_position %= 100

        elif current_position < 0:
            current_position += 100
            current_position %= 100

        if current_position == 0:
            result += 1

    print(result)
    
if __name__ == "__main__":
    main()