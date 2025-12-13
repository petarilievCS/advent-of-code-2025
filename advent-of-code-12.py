import sys

class Region:
    def __init__(self, width, length, shapes):
        self.width = width
        self.length = length
        self.shapes = shapes

def main():
    file_name = sys.argv[1]
    regions = []
    with open(file_name, "r") as file:
        # Skip boxes
        for _ in range(30):
            next(file)
        
        for line in file:
            line = line.strip()
            tokens = line.split()

            size_token = tokens[0][:-1] # remove : at the end
            width, length = [int(x) for x in size_token.split("x")]
            shapes = [int(x) for x in tokens[1:]]
            region = Region(width, length, shapes)
            regions.append(region)

    result = 0
    SHAPE_AREA = 9
    for region in regions:
        area = region.width * region.length
        total_shape_area = 0
        for shape in region.shapes:
            shapes_area = shape * SHAPE_AREA
            total_shape_area += shapes_area
        
        if total_shape_area <= area:
            result += 1
    
    print(result)

if __name__=="__main__":
    main()