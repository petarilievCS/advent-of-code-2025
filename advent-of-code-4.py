import sys

def main():
    file_name = sys.argv[1]

    # Parse input
    map = []
    with open(file_name, "r") as file:
        for line in file:
            map_row = [char for char in line.strip()]
            map.append(map_row)

    result = 0
    number_of_rows = len(map)
    number_of_columns = len(map[0])

    def is_roll(r, c):
        if r < 0 or r >= number_of_rows or c < 0 or c >= number_of_columns:
            return False
        return map[r][c] == "@"
   
    
    to_remove = []
    while True:
        # Reset
        to_remove = []

        # Mark rolls for removal
        for r in range(number_of_rows):
            for c in range(number_of_columns):
                # Roll of paper
                if is_roll(r, c):
                    adjacent_rolls = 0
                    adjacent_rolls += is_roll(r - 1, c - 1)
                    adjacent_rolls += is_roll(r - 1, c)
                    adjacent_rolls += is_roll(r - 1, c + 1)
                    adjacent_rolls += is_roll(r, c - 1)
                    adjacent_rolls += is_roll(r, c + 1)
                    adjacent_rolls += is_roll(r + 1, c - 1)
                    adjacent_rolls += is_roll(r + 1, c)
                    adjacent_rolls += is_roll(r + 1, c + 1)

                    if adjacent_rolls < 4:
                        to_remove.append((r, c))
        
        # Remove rolls
        for (r, c) in to_remove:
            map[r][c] = "."

        # Increment result
        result += len(to_remove)

        # Nothing more to remove
        if len(to_remove) == 0:
            break

    print(result)            

if __name__ ==  "__main__":
    main()