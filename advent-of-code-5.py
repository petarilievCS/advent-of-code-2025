import sys
import copy

def main():
    file_name = sys.argv[1]

    # Parse input
    fresh_ingredient_id_ranges = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                break

            range_string = line.split("-")
            tuple_range = (int(range_string[0]), int(range_string[1]))
            fresh_ingredient_id_ranges.append(tuple_range)

    # Returns true if itnerval_a and interval_b overlap
    def overlap(interval_a, interval_b):
        # interval_a is after interval_b
        if interval_a[0] > interval_b[1]:
            return False
        
        # interval_a is before interval_b
        if interval[1] < interval_b[0]:
            return False
        
        return True
    
    def merge_intervals(interval_a, interval_b):
        merged_interval = [
            min(interval_a[0], interval_b[0]),
            max(interval_a[1], interval_b[1])
        ]
        return merged_interval

    # Setup
    previous_intervals = []
    new_intervals = []
    fresh_ingredient_id_ranges.sort()

    # Create intervals
    for i in range(len(fresh_ingredient_id_ranges)):
        new_interval = fresh_ingredient_id_ranges[i]
        new_intervals.clear()

        for interval in previous_intervals:
            if overlap(new_interval, interval):
                new_interval = merge_intervals(interval, new_interval)
            else:
                new_intervals.append(interval)

        new_intervals.append(new_interval)
        print(new_intervals)
        previous_intervals = copy.copy(new_intervals)

    result = 0
    for interval in previous_intervals:
        start, end = interval
        result += (end - start) + 1

    print(result)
    
if __name__ == "__main__":
    main()