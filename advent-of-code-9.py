import sys

def main():
    RED = "#"
    GREEN = "X"
    EMPTY = "."

    # Step 0: Read input
    file_name = sys.argv[1]
    input = []
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            (x, y) = line.split(",")
            input.append((int(x), int(y)))

    # Step 1: Find map dimensions
    num_cols = max(x for x, _ in input) + 1
    num_rows = max(y for _, y in input) + 1

    # Construct empty map
    map = [[EMPTY] * num_cols for _ in range(num_rows)]

    # Add first red tile
    start_x, start_y = input[0]
    map[start_y][start_x] = RED

    def connect_tiles(tile_a, tile_b):
        col_a, row_a = tile_a
        col_b, row_b = tile_b

        if row_a == row_b:
            # Reverse if needed
            if col_b > col_a:
                col_b, col_a = col_a, col_b

            # Connect
            row = row_a
            for j in range(col_b + 1, col_a):
                map[row][j] = GREEN
        elif col_a == col_b:
            # Reverse if needed
            if row_b > row_a:
                row_b, row_a = row_a, row_b
            
            # Connect
            col = col_a
            for j in range(row_b + 1, row_a):
                map[j][col] = GREEN
        else:
            print("FATAL ERROR")

    def should_be_green(row, col):
        if row == 0 or col == 0:
            return False
        
        if map[row][col - 1] == EMPTY or map[row - 1][col] == EMPTY:
            return False
        
        return True

    def calculate_area(point_a, point_b):
        x_a, y_a = point_a
        x_b, y_b = point_b

        length = abs(x_a - x_b) + 1
        height = abs(y_a - y_b) + 1
        result = length * height
        return result
    
    def valid_square(point_a, point_b):
        col_a, row_a = point_a
        col_b, row_b = point_b

        start_col = min(col_a, col_b)
        start_row = min(row_a, row_b)
        end_col = max(col_a, col_b)
        end_row = max(row_a, row_b)

        # Check top / bottom edges
        for col in range(start_col, end_col + 1):
            if map[start_row][col] == EMPTY or map[end_row][col] == EMPTY:
                return False
        
        # Check side edges
        for row in range(start_row, end_row + 1):
            if map[row][start_col] == EMPTY or map[row][end_col] == EMPTY:
                return False
                
        return True

    def print_map():
        for row in map:
            print(row)

    # Add the rest of the red tiles
    for i in range(1, len(input)):
        col, row = input[i]        
        map[row][col] = RED
        connect_tiles(input[i], input[i - 1])
    
    # Connect last and first
    connect_tiles(input[0], input[-1])

    # Color inside green
    for row in map:
        # Find edges of green zones
        coloring = False
        for col in range(len(row) - 1):
            tile = row[col]
            if coloring:
                # Option 1: Stop coloring
                if row[col] != EMPTY and row[col + 1] == EMPTY:
                    coloring = False
                # Option 2: Color
                else:
                    row[col] = GREEN
            else:
                # Option 1: Start coloring
                if (row[col] == RED or row[col] == GREEN) and row[col + 1] == EMPTY:
                    coloring = True

    # Iterate over all possible red pairs
    max_area = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            point_a, point_b = input[i], input[j]
            area = calculate_area(point_a, point_b)
            if valid_square(point_a, point_b):
                max_area = max(area, max_area)
                print(f"Current answer: {max_area}")

    return max_area
    
if __name__ == "__main__":
    result = main()
    print(result)