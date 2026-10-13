#!/usr/bin/env python3
"""
Simple Calculator
A basic calculator with addition, subtraction, multiplication, and division operations.
"""

def add(a: float, b: float) -> float:
    """Addition operation."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtraction operation."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplication operation."""
    return a * b

def divide(a: float, b: float) -> float:
    """Division operation."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator():
    """Main calculator function with interactive menu."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    print("=" * 40)
    print("  Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nOperations: + (add), - (subtract), * (multiply), / (divide)")
        print("Type 'quit' to exit")
        
        operator = input("\nEnter operator: ").strip()
        
        if operator.lower() == 'quit':
            print("Goodbye!")
            break
        
        if operator not in operations:
            print("Invalid operator! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter numeric values.")
            continue
        
        try:
            result = operations[operator](num1, num2)
            print(f"\nResult: {num1} {operator} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()