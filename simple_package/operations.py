###
## simple_package - Module operations.py
## Basic online calculator
##
## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##

## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##


import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Error: Cannot take the square root of a negative number.")
    return math.sqrt(a)

def logarithm(a, base=10):
    if a <= 0 or base <= 0 or base == 1:
        raise ValueError("Error: Logarithm input (a) must be positive, and base must be positive and not 1.")
    return math.log(a, base)

def sine(a_degrees):
    return math.sin(math.radians(a_degrees))

def run_calculator():
    print("--- Simple Calculator Interface ---")
    print("Commands: add(a,b), subtract(a,b), multiply(a,b), divide(a,b),")
    print("          power(a,b), sqrt(a), log(a,base), sine(degrees)")
    print("Type 'exit' to quit.")

    COMMANDS = {
        'add': lambda args: add(*args),
        'subtract': lambda args: subtract(*args),
        'multiply': lambda args: multiply(*args),
        'divide': lambda args: divide(*args),
        'power': lambda args: power(*args),
        'sqrt': lambda args: square_root(*args),
        'log': lambda args: logarithm(*args),
        'sine': lambda args: sine(*args)
    }

    while True:
        try:
            user_input = input("\nEnter command (e.g., add(10,5)): ").strip().lower()

            if user_input == 'exit':
                print("Exiting calculator. Goodbye!")
                break

            function_name, arg_string = user_input.split('(', 1)
            
            arg_string = arg_string.rstrip(')')
            
            args = [float(arg.strip()) for arg in arg_string.split(',')]

            if function_name in COMMANDS:
                result = COMMANDS[function_name](args)
                print(f"Result: {result}")
            else:
                raise ValueError(f"Unknown command: {function_name}")

        except ValueError as e:
            print(f" Error: Invalid input or operation: {e}")
        except TypeError:
            print(" Error: Incorrect number of arguments provided for the function.")
        except Exception as e:
            print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_calculator()