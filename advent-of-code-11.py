import sys

# Find path svr -> out, such that it contains dac and fft

def main():
    # Parse arguments
    graph = {}
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            tokens = line.split()
            machine = tokens[0][:-1] # remove : at the end
            neighbors = tokens[1:]
            graph[machine] = neighbors
    
    def dfs(visited, current, goal):
        # Reached the end
        if current == goal:
            if "fft" in visited and "dac" in visited:
                return 1
            return 0
        
        # Already been here
        elif current in visited:
            return 0

        # Compute answer
        num_paths = 0
        visited.add(current)
        for neighbor in graph[current]:
            num_paths += dfs(visited, neighbor)
        visited.remove(current)
        
        return num_paths

    result = dfs(set(), "svr")
    print(result)

if __name__=="__main__":
    main()