import sys

def main():
    # Step 1: Parse input
    file_name = sys.argv[1]
    input = []
    with open(file_name, "r") as file:
        for line in file:
            input_row = [char for char in line.strip()]
            input.append(input_row)

    num_splits = [0]
    
    # Step 2: Define search
    def dfs(row, col):
        # Out of range 
        if row >= len(input) or col < 0 or col >= len(input[0]):
            return
        
        # Already processed
        current = input[row][col]
        if current == "|": 
            return
        
        # Empty space, move down
        if current == "S" or current == ".":
            input[row][col] = "|"
            dfs(row + 1, col)
        # Split
        elif current == "^":
            num_splits[0] += 1
            dfs(row, col + 1)
            dfs(row, col - 1)

    # Step 3: Find starting position
    for i in range(len(input[0])):
        if input[0][i] == "S":
            dfs(0, i)
    
    print(num_splits[0])

if __name__ == "__main__":
    main()