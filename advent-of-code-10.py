import sys
import time

class Machine:
    def __init__(self, button_wirings, goal_joltages):
        self.buttons = button_wirings
        self.goal_joltages = goal_joltages
        self.joltages = [0] * len(goal_joltages)

    def is_started(self):
        return self.joltages == self.goal_joltages

    def adjust_joltage(self, button, amount):
        overcharged = False
        for toggle in button:
            self.joltages[toggle] += amount
            if self.joltages[toggle] > self.goal_joltages[toggle]:
                overcharged = True
        return overcharged

def dfs(machine, num_toggles):
    if num_toggles == 0:
        return machine.is_started()
    else:
        for button in machine.buttons:
            overcharged = machine.adjust_joltage(button, 1)
            if overcharged:
                machine.adjust_joltage(button, -1)
                return False
            else:
                if dfs(machine, num_toggles - 1):
                    return True
                machine.adjust_joltage(button, -1)
    return False

def main():
    # Parse input
    file_name = sys.argv[1]
    machines = []
    with open(file_name, "r") as file:
        # Each line is one machine
        for line in file:
            line = line.strip()
            tokens = line.split()

            # Buttons
            button_tokens = tokens[1:-1]
            button_wirings = []
            for button_token in button_tokens: # (1,3)
                button_token = button_token[1:-1] # 1,3
                button_wiring = button_token.split(",")
                button_wiring = [int(x) for x in button_wiring]
                button_wirings.append(button_wiring)

             # Joltages
            joltage_token = tokens[-1]
            joltages = [int(joltage_str) for joltage_str in joltage_token[1:-1].split(",")]
            
            machine = Machine(
                button_wirings=button_wirings,
                goal_joltages=joltages
            )
            machines.append(machine)

    total_result = 0
    for machine in machines:
        num_toggles = 1
        
        while True:
            print(f"Running with {num_toggles} toggles")
            if dfs(machine, num_toggles):
                break
            num_toggles += 1

        total_result += num_toggles

    return total_result

if __name__ == "__main__":
    start_time = time.time()           # start timer
    result = main()
    end_time = time.time()             # end timer
    print(f"Result: {result}")
    print(f"Elapsed time: {end_time - start_time:.4f} seconds")