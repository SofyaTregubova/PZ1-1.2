def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Test the functions
if __name__ == "__main__":
    print("Testing math functions:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}") 
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"8 / 2 = {divide(8, 2)}")
    print(f"8 / 0 = {divide(8, 0)}")
