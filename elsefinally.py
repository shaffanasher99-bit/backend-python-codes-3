# Example 1: Division

def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2

    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Division successful.")
        print("Result:", result)

    finally:
        print("Division operation completed.")


# Example 2: List Access

def access_list():
    numbers = [10, 20, 30, 40, 50]

    try:
        index = int(input("Enter an index (0-4): "))
        value = numbers[index]

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Index is out of range.")

    else:
        print("Value found successfully.")
        print("Value:", value)

    finally:
        print("List operation completed.")


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

    except KeyError:
        print("Student does not exist.")

    else:
        print("Student found successfully.")
        print("Name:", name)
        print("Marks:", marks)

    finally:
        print("Dictionary operation completed.")


# Main program
if __name__ == "__main__":

    print("===== Example 1 =====")
    divide_numbers()

    print("\n===== Example 2 =====")
    access_list()

    print("\n===== Example 3 =====")
    find_student()