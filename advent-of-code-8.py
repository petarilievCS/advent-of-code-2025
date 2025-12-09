import math
import sys

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.sizes = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.sizes[root_x] < self.sizes[root_y]:
                root_x, root_y = root_y, root_x
            self.parents[root_y] = root_x
            self.sizes[root_x] += self.sizes[root_y]

            # We have one big circuit
            if self.sizes[root_x] == self.n:
                return True
            
        return False

def main():
    # Part 1: parse input
    input = []
    file_name = sys.argv[1]
    
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            coordinates = tuple([int(s) for s in line.split(",")])
            input.append(coordinates)

    def calculate_distance(point_a, point_b):
        (x1, y1, z1) = point_a
        (x2, y2, z2) = point_b
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return distance
    
    # Part 2: calculate distances
    points_to_distance = {}
    for a, point_a in enumerate(input):
        for b in range(a + 1, len(input)):
            point_b = input[b]
            distance = calculate_distance(point_a, point_b)
            points_to_distance[(a, b)] = distance
    
    distance_to_points = []
    for points, distance in points_to_distance.items():
        distance_to_points.append((distance, points))
    distance_to_points.sort()

    point_pairs = [points for _, points in distance_to_points]

    # Part 3: Create union find
    N = len(input)
    uf = UnionFind(N)

    # Part 4: Merge close points
    for (point_a, point_b) in point_pairs:
        # Check if merging x and y produces final circuit
        if uf.union(point_a, point_b):
            coordinates_a, coordinates_b = input[point_a], input[point_b]
            return coordinates_a[0] * coordinates_b[0]

if __name__ == "__main__":
    result = main()
    print(result)