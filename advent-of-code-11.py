import sys

def main():
    # Parse arguments
    graph = {}
    graph["out"] = []
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            tokens = line.split()
            machine = tokens[0][:-1] # remove : at the end
            neighbors = tokens[1:]
            graph[machine] = neighbors
    
    def dfs(current, goal, cache):
        # Reached the end
        if current == goal:
            return 1
        
        if current in cache:
            return cache[current]

        # Compute answer
        num_paths = 0
        for neighbor in graph[current]:
            num_paths += dfs(neighbor, goal, cache)
        
        cache[current] = num_paths
        return num_paths

    svr_fft = dfs("svr", "fft", {})
    fft_dac = dfs("fft", "dac", {})
    dac_out = dfs("dac", "out", {})
    part_1 = svr_fft * fft_dac * dac_out

    svr_dac = dfs("svr", "dac", {})
    dac_fft = dfs("dac", "fft", {})
    fft_out = dfs("fft", "out", {})
    part_2 = svr_dac * dac_fft * fft_out

    result = part_1 + part_2
    print(result)

if __name__=="__main__":
    main()