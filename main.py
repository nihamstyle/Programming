import hrm
import authentication


def display_menu():
    print("\nHRM Application Menu")
    print("1. View Personal Information")
    print("2. Update Personal Information")
    print("3. Submit Leave Request")
    print("4. View Company Policies")
    print("5. View Work Schedule")
    print("0. Exit")


def main():
    print("Welcome to the HRM Application!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authentication.sign_in(username, password):
        while True:
            display_menu()
            choice = int(input("Choose an option (0 to exit): "))

            if choice == 1:
                print(f"Your personal information:")
                print(hrm.Employee(1, "John Doe", "Manager", "Sales", "1st January 2022", "Active").get_personal_info())

            elif choice == 2:
                print("Update personal information")

            elif choice == 3:
                print("Submit leave request")

            elif choice == 4:
                print("View company policies")

            elif choice == 5:
                print("View work schedule")

            elif choice == 0:
                print("Goodbye!")
                break

    else:
        print("Invalid username or password. Please try again.")


if __name__ == "__main__":
    main()
