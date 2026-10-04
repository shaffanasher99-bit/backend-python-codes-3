# Example 1: ValueError with Custom Exception

def get_age():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")

        if age > 120:
            raise ValueError("Age cannot be greater than 120.")

        print("Your age is:", age)

    except ValueError as e:
        print("Error:", e)


# Example 2: ZeroDivisionError with Custom Exception

def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num1 < 0 or num2 < 0:
            raise ValueError("Numbers cannot be negative.")

        if num2 == 0:
            raise ZeroDivisionError("You created a division by zero.")

        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)


# Example 3: IndexError and KeyError with Custom Exceptions

def access_data():
    students = {
        "Ali": [80, 75, 90],
        "Ahmed": [85, 88, 92]
    }

    try:
        name = input("Enter student name: ")
        index = int(input("Enter mark index (0-2): "))

        if name not in students:
            raise KeyError("This student does not exist.")

        if index < 0 or index >= 3:
            raise IndexError("Index must be between 0 and 2.")

        marks = students[name]
        print("Marks:", marks[index])

    except KeyError as e:
        print("Error:", e)

    except IndexError as e:
        print("Error:", e)

    except ValueError:
        print("Error: Index must be a number.")


# Main program
if __name__ == "__main__":

    print("===== Example 1: ValueError =====")
    get_age()

    print("\n===== Example 2: Division =====")
    divide_numbers()

    print("\n===== Example 3: Student Data =====")
    access_data()