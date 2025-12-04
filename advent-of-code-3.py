import sys


# TODO: Use pointers instead of copying strings

def main():
    file_name, total_batteries = sys.argv[1], int(sys.argv[2])
    banks = []

    with open(file_name, "r") as file:
        for line in file:
            bank = line.strip()
            banks.append(bank)

    result = 0

    for bank in banks:
        max_voltage_string = bank[:total_batteries]
        max_voltage = int(max_voltage_string)

        # Iteration
        for position in range(total_batteries, len(bank)):
            iteration_max_voltage = 0
            battery = bank[position]

            for max_voltage_position in range(0, len(max_voltage_string)):
                first_part = max_voltage_string[0:max_voltage_position]
                second_part = max_voltage_string[max_voltage_position + 1:]
                voltage_string = first_part + second_part + battery
                voltage = int(voltage_string)
                iteration_max_voltage = max(voltage, iteration_max_voltage)

            if iteration_max_voltage > max_voltage:
                max_voltage_string = str(iteration_max_voltage)
                max_voltage = iteration_max_voltage

        result += max_voltage

    print(result)

if __name__ == "__main__":
    main()