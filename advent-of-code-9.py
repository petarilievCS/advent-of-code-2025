import sys

def main():
    # Part 1: parse input
    file_name = sys.argv[1]
    red_tile_locations = []
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            (x, y) = line.split(",")
            red_tile_locations.append((int(x), int(y)))

    def find_area(square_a, square_b):
        xa, ya = square_a
        xb, yb = square_b

        length = abs(xa - xb) + 1
        height = abs(ya - yb) + 1
        return length * height
    
    # Part 2: find max square
    max_area = 0
    for i in range(len(red_tile_locations)):
        for j in range(i+1, len(red_tile_locations)):
            square_a, square_b = red_tile_locations[i], red_tile_locations[j]
            area = find_area(square_a, square_b)
            max_area = max(area, max_area)

    return max_area

if __name__ == "__main__":
    result = main()
    print(result)