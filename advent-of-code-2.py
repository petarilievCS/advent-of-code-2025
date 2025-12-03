import sys

def is_invalid_ID(id):
    id_string = str(id)
    length = len(id_string)

    for number_of_parts in range(2, length + 1): # (2, 11)    
        if length % number_of_parts != 0: 
            continue
        
        part_length = length // number_of_parts
        parts = []

        for position in range(0, number_of_parts):
            part = id_string[position * part_length : (position + 1) * part_length]
            parts.append(part)
        
        if len(set(parts)) == 1:
            return True
        
    return False

def main():
    file_name = sys.argv[1]

    ranges = []
    with open(file_name, "r") as file:
        input_string = file.readline().strip()
        range_strings = input_string.split(",")
        ranges = [range_string.split("-") for range_string in range_strings]
        ranges = [(int(range[0]), int(range[1])) for range in ranges]
        
    result = 0
    for start, end in ranges:
        for id in range(start, end + 1):
            if is_invalid_ID(id):
                result += id

    print(result)
    return result

if __name__ == "__main__":
    main()