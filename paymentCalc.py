#!/usr/bin/python

def main():
    done = False
    while not done:
        print_menu()
        user_option = input("Enter option: ")
        option_information = choose_option(user_option)
        if option_information != -1:
            # Valid option
            if option_information == 6:
                done = True
                print("\n")
                print("Thank you for using Payment_Calculator-Cli. Come back soon. \n")
            else:
                evaluate_request(option_information)
        else:
            print("Please enter a valid positive number between 1 and 6.\n")
            exit()


def test_file(filename):
    try:
        fhandler = open(filename, 'r')
        fhandler.close()
        return True
    except FileNotFoundError:
        return False
        #exit()


# Print the menu to the user
def print_menu():
    print("\n")
    print("Welcome to Payment Calculator-CLI. Please, choose an option:")
    print("1. Employees payment (Create employees_payment.txt file)")
    print("2. Employee name with maximum number of work hours")
    print("3. Employees name with minimum number of work hours")
    print("4. Employee name with maximum rate")
    print("5. Employee name with minimum rate")
    print("6. Exit")


# Verify the validity of the option chosen
# Option must be a number between 1 and 6 inclusive
def choose_option(option):
    if option.isdigit():
        numeric_option = int(option)
        # Check if option is in range
        if numeric_option >= 1 and numeric_option <= 6:
            return numeric_option
        else:
            return -1 # Invalid option
    else:
        return -1 # Invalid option


# Calculate the payment of an employee
def calculate_payment(hours, rate):
    if hours <= 40 or hours > 50: # Regular pay
        return hours * rate
    else:
        return (40 * rate) + ((hours - 40) * (rate * 1.5)) # Calculate overtime


# Evaluate if the file to be looked at exist or not.
def evaluate_request(option):
    filename = input("Enter the file to be evaluated: ")
    if test_file(filename):
        fhandler = open(filename, 'r') # Open the file
        find_employee_info(filename, fhandler, option)

    else:
        print("Illegal file name. Input file was not found")
        print(input("Press Enter to continue: "))
        return -1

def find_name(line):
    return line.split(",")[0]

def find_hours(line):
    return line.split(",")[1]

def find_rate(line):
    return line.split(",")[2]


def create_hours_dict(filename, fhandler):
    hours_dict = {}
    for line in fhandler:
        if not line.startswith("time"):
            hours_dict[find_name(line)] = find_hours(line)
        else:
            continue
    return hours_dict

def create_rate_dict(filename, fhandler):
    rate_dict = {}
    for line in fhandler:
        if not line.startswith("time"):
            rate_dict[find_name(line)] = find_rate(line).split("\n")[0]
        else:
            continue
    return rate_dict

# Avoid to have to write the print everytime
def press_enter():
    print(input("Press Enter to continue"))


def find_employee_info(filename, fhandler, option):
    if option == 1:
        newfile = open("employees_payment.txt", 'w')
        for line in fhandler:
            if not line.startswith("time"):
                newfile.write(find_name(line).ljust(20) + "$" + str(calculate_payment(float(find_hours(line)), float(find_rate(line)))) + "\n")
            else:
                continue
        print("A file named employees_payment.txt, containing the payment functions has been created.")
        press_enter()
        newfile.close()
        fhandler.close()

    # Find the name of the employee with the highest number of hours
    elif option == 2:
        hours_dict = create_hours_dict(filename, fhandler)
        sorted_dict = sorted((value, key) for (key, value) in hours_dict.items())
        print("The employee with the max number of hours is: " + str(sorted_dict[-1][1]) + " | Expected: Elon Musk" + '\n')
        press_enter()

    # Find the name of the employee with the lowest number of hours
    elif option == 3:
        hours_dict = create_hours_dict(filename, fhandler)
        sorted_dict = sorted((value, key) for (key, value) in hours_dict.items())
        print("The employee with the min number of hours is: " + str(sorted_dict[0][1]) + " | Expected: Benjamin Franklin" + '\n')
        press_enter()

    # Find the name of the employee with the highest rate
    elif option == 4:
        rate_dict = create_rate_dict(filename, fhandler)
        sorted_dict = sorted((value, key) for (key, value) in rate_dict.items())
        print("The employee with the max rate is: " + str(sorted_dict[-1][1]) + " | Expected: Thomas Edison" + '\n')
        press_enter()

    # Find the name of the employee with the highest rate
    elif option == 5:
        rate_dict = create_rate_dict(filename, fhandler)
        sorted_dict = sorted((value, key) for (key, value) in rate_dict.items())
        print("The employee with the min rate is: " + str(sorted_dict[0][1]) + " | Expected: Nikola Tesla" + '\n')
        press_enter()

    # Exit the program
    elif (option == 6):
        print("Thanks for using the payment calculation program")
        exit()

if __name__ == "__main__":
    main()
