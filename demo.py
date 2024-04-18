# This Python file contains intentional errors for CodeQL scanning

def divide(a, b):
    """Function to divide two numbers"""
    return a / b  # Error: Division by zero if b is 0

def factorial(n):
    """Function to calculate the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Error: Potential stack overflow for large values of n



def main():
    """Main function"""
    print("Enter two numbers to divide:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = divide(num1, num2)
    print("Result of division:", result)
    def average(l):
        return sum(l) / len(l)
    print(average([1.0, 2.0]))  # Prints "1.5".
    print (average([1, 2]))      # Prints "1", which is incorrect.

    print("Enter a number to calculate its factorial:")
    num = int(input("Enter the number: "))
    fact = factorial(num)
    print("Factorial of", num, "is", fact)

if __name__ == "__main__":
    main()
