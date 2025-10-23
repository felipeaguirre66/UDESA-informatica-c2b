import argparse

def calc(a, b, operation):
    if operation == 'sum':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation.")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("--a", type=float, required=True, help="First number")
    parser.add_argument("--b", type=float, required=True, help="Second number")
    parser.add_argument("--operation", type=str, required=True, choices=['sum', 'subtract', 'multiply', 'divide'], help="Operation to perform")
    args = parser.parse_args()
    result = calc(args.a, args.b, args.operation)
    print(f"The result of {args.operation}ing {args.a} and {args.b} is: {result}")