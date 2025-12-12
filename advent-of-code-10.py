import sys
import time

from z3 import Int, Sum, Optimize

class Machine:
    def __init__(self, button_wirings, goal_joltages):
        self.buttons = button_wirings
        self.goal_joltages = goal_joltages
        self.joltages = [0] * len(goal_joltages)

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
        optimizer = Optimize()
        N = len(machine.buttons)

        # [y0, y1 ... yN]
        # Each yi represents the number of times the ith button has been pressed
        button_presses = [Int(f"y{i}") for i in range(N)]
        
        # {indicator : button}
        # Each pair represents an indicator mapped to a list of buttons that increase its
        # joltage when pressed
        indicator_to_button = {}
        
        # Initialize indicator_to_button
        for i in range(len(machine.joltages)):
            indicator_to_button[i] = []

        # Add buttons to indicators
        for button, button_indicators in enumerate(machine.buttons):
            for indicator in button_indicators:
                indicator_to_button[indicator].append(button)

        # All yi >= 0
        for y in button_presses:
            optimizer.add(y >= 0)
        
        for indicator, joltage in enumerate(machine.goal_joltages):
            # Create a constraint for each joltage
            optimizer.add(Sum([button_presses[i] for i in indicator_to_button[indicator]]) == joltage)
        
        # Find the minimum sum
        handle = optimizer.minimize(Sum(button_presses))
        optimizer.check()
        model = optimizer.model()

        total = 0
        for button in button_presses:
            # print(model[button].as_long())
            presses = model[button].as_long()
            total += presses

        total_result += total

    return total_result


if __name__ == "__main__":
    start_time = time.time()           # start timer
    result = main()
    end_time = time.time()             # end timer
    print(f"Result: {result}")
    print(f"Elapsed time: {end_time - start_time:.4f} seconds")