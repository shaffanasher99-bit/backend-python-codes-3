# Example 1: Division

def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


# Example 2: List Index

def access_student():
    students = ["Ali", "Ahmed", "Hassan", "Usman"]

    try:
        index = int(input("Enter student index (0-3): "))
        print("Student:", students[index])

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Index is out of range.")


# Example 3: Dictionary

def find_student():
    students = {
        "Ali": 85,
        "Ahmed": 78,
        "Hassan": 92
    }

    try:
        name = input("Enter student name: ")
        marks = students[name]
        print(name, "got", marks, "marks.")

    except KeyError:
        print("Student not found in the dictionary.")


# Main program
if __name__ == "__main__":

    print("===== Example 1: Division =====")
    divide_numbers()

    print("\n===== Example 2: List Index =====")
    access_student()

    print("\n===== Example 3: Dictionary =====")
    find_student()