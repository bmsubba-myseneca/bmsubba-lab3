#!/usr/bin/env python3

# Author ID:bmsubba

# operate() function definition
def operate(num1, num2, operator):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

# Main Program
if __name__ == '__main__':
    # Example usage of the operate function
    print(operate(10, 5, 'add'))        
    print(operate(10, 5, 'subtract'))  
    print(operate(10, 5, 'multiply'))  
    print(operate(10, 5, 'divide'))    
