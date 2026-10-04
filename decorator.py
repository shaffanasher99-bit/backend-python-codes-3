# Example 1: Basic Decorator

def welcome_decorator(function):
    def wrapper():
        print("----- Starting Function -----")
        function()
        print("----- Function Completed -----")

    return wrapper


@welcome_decorator
def welcome():
    print("Welcome to Python!")


# Example 2: Decorator with Arguments

def message_decorator(function):
    def wrapper(name):
        print("Processing user...")
        function(name)
        print("User processed successfully.")

    return wrapper


@message_decorator
def greet(name):
    print("Hello", name)


# Example 3: Decorator for Calculation

def calculation_decorator(function):
    def wrapper(a, b):
        print("Calculating...")
        result = function(a, b)
        print("Calculation completed.")
        print("Result:", result)

    return wrapper


@calculation_decorator
def multiply(a, b):
    return a * b


# Main program
if __name__ == "__main__":

    print("===== Example 1 =====")
    welcome()

    print("\n===== Example 2 =====")
    greet("Ahmed")

    print("\n===== Example 3 =====")
    multiply(10, 5)