import sys


# TODO: Use pointers instead of copying strings

def main():
    file_name, total_batteries = sys.argv[1], int(sys.argv[2])
    banks = []

    with open(file_name, "r") as file:
        for line in file:
            bank = line.strip()
            banks.append(bank)

    def find_max_voltage(bank, current_batteries):
        dp = {}
        if len(current_batteries) == total_batteries:
            return int(current_batteries)
        
        if current_batteries in dp:
            return dp[current_batteries]

        current_number_of_batteries = len(current_batteries)
        missing_number_of_batteries = total_batteries - current_number_of_batteries
        # end = len(bank)
        end = len(bank) - missing_number_of_batteries + 1
        
        max_voltage = 0
        for position in range(end):
            digit = bank[position]
            voltage = find_max_voltage(bank[position + 1:], current_batteries + digit)
            max_voltage = max(voltage, max_voltage)

        dp[current_batteries] = max_voltage
        return max_voltage

    result = 0
    for bank in banks:
        result += find_max_voltage(bank, "")

    print(result)

if __name__ == "__main__":
    main()