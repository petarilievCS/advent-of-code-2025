import sys

class Machine:
    def __init__(self, goal_indicators, button_wirings):
        self.goal_indicators = goal_indicators
        self.indicators = [False] * len(goal_indicators)
        self.buttons = button_wirings

    def is_started(self):
        return self.goal_indicators == self.indicators
    
    def toggle(self, button):
        for toggle in button:
            self.indicators[toggle] = not self.indicators[toggle]

def dfs(machine, num_toggles):
    if num_toggles == 0:
        return machine.is_started()
    else:
        for button in machine.buttons:
            machine.toggle(button)
            if dfs(machine, num_toggles - 1):
                return True
            machine.toggle(button)
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

            # Indicator lights
            indicator_token = tokens[0] # [.##.]
            indicator_token = indicator_token[1:-1] # .##.
            goal_indicators = list(indicator_token)
            for i in range(len(goal_indicators)):
                if goal_indicators[i] == "#":
                    goal_indicators[i] = True
                else:
                    goal_indicators[i] = False

            # Buttons
            button_tokens = tokens[1:-1]
            button_wirings = []
            for button_token in button_tokens: # (1,3)
                button_token = button_token[1:-1] # 1,3
                button_wiring = button_token.split(",")
                button_wiring = [int(x) for x in button_wiring]
                button_wirings.append(button_wiring)

             # Joltages
            # TODO: Implement in Part 2

            machine = Machine(
                goal_indicators=goal_indicators, 
                button_wirings=button_wirings
            )
            machines.append(machine)

    total_result = 0
    for machine in machines:
        num_toggles = 1
        
        while True:
            if dfs(machine, num_toggles):
                break
            num_toggles += 1

        total_result += num_toggles

    return total_result

if __name__ == "__main__":
    print(main())