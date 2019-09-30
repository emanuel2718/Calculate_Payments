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
            print("Please enter a valid positive number between 1 and 6.")
            print(input("Press Enter to continue..."))
            return -1 # Invalid option
    else:
        print("Please enter a valid positive number between 1 and 6.")
        print(input("Press Enter to continue..."))
        return -1 # Invalid option



# Calculate the payment of an employee
#def calculate_payment(hours, rate):










def evaluate_request(option):
    filename = input("Enter the file to be evaluated: ")
    if test_file(filename):
        fhandler = open(filename, 'r') # Open the file
        find_employee_info(option)

    else:
        print("Illegal file name. Input file was not found")
        print(input("Press Enter to continue: "))
        return -1

    if (option == 1):
        print("A file", filename, "containing the payment functions has been created.")

    elif (option == 2):
        print("The employee with the maximum number of work hours is: ")

    elif (option == 3):
        print("The employee with the minimum number of work hours is: ")

    elif (option == 4):
        print("The employee with the maximum rate is: ")

    elif (option == 5):
        print("The employee with the minimum rate is: ")

    else:
        if (option == 6):
            print("Thanks for using the payment calculation program")
            exit()




def find_employee_info(fhandler, option):
    newfile = open("employess_payment.txt", 'w')
    for line in fhandler:
        if not line.startwith("time"):





if __name__ == "__main__":
    main()



