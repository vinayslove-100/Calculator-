import sys
import time
from sympy import sin, cos, tan, sec, csc, cot, pi, simplify

# typing animation
def a(text, delay=0.02):
    text = str(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# convert sqrt → √
def format_value(x):
    return str(simplify(x)).replace("sqrt", "√")

# REAL CALCULATOR
def real():
    while True:
        a("\nEnter expression (example: 5+3*2) or type 'back': ")
        expr = input("> ")

        if expr.lower() == "back":
            return

        try:
            result = eval(expr)
            a(f"Result = {result}")
        except:
            a("Invalid expression")

# ROOT FINDER
def root():
    while True:
        a("\nEnter number to find square root (or type 'back'): ")
        n = input("> ")

        if n.lower() == "back":
            return

        try:
            n = float(n)
            result = n ** 0.5
            a(f"√{n} = {result}")
        except:
            a("Invalid number")

# TRIGONOMETRY
def tri():
    while True:
        a("\nEnter angle in degrees (or type 'back'): ")
        inp = input("> ")

        if inp.lower() == "back":
            return

        try:
            angle = float(inp)
            r = angle * pi / 180

            print("\nTrigonometric Values\n")

            print("sin  =", format_value(sin(r)))
            print("cos  =", format_value(cos(r)))
            print("tan  =", format_value(tan(r)))
            print("cosec=", format_value(csc(r)))
            print("sec  =", format_value(sec(r)))
            print("cot  =", format_value(cot(r)))

        except:
            a("Invalid angle")

# MAIN PROGRAM
def main():

    a("\n\tWELCOME TO PYTHON SCIENTIFIC CALCULATOR 🙏\n")

    while True:

        print("""
1. Real Calculator
2. Root Finder
3. Trigonometry
4. Exit
""")

        a("Choose operation (1-4): ")
        choice = input("> ")

        if choice == "1":
            real()

        elif choice == "2":
            root()

        elif choice == "3":
            tri()

        elif choice == "4":
            a("\nGoodbye 👋")
            break

        else:
            a("Invalid choice")

# run program
main()