#!/usr/bin/python3
""" This program imports functions from calculator_1.py module
    and does basic arithmetic operations"""

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check for correct usage
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract values and operator from command-line arguments
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    # Perform calculation based on operator
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print result
    print("{} {} {} = {}".format(a, op, b, result))
