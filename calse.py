import sys
import time
from sympy import sin, cos, tan, sec, csc, cot, pi, simplify, nsimplify

# typing animation
def a(text, delay=0.02):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# format sqrt symbol
def format_value(v):
    return str(v).replace("sqrt", "√")

# REAL CALCULATOR
def real():
    while True:
        a("\nEnter expression (example: 5+3*2) or type 'back'")
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
        a("\nEnter number to find square root (or type 'back')")
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
        a("\nEnter angle in degrees (example: 30,45,60) or type 'back'")
        inp = input("> ")

        if inp.lower() == "back":
            return

        try:
            angle = int(inp)

            r = angle * pi / 180

            sinv = simplify(sin(r))
            cosv = simplify(cos(r))
            tanv = simplify(tan(r))
            cscv = simplify(csc(r))
            secv = simplify(sec(r))
            cotv = simplify(cot(r))

            print("\nTrigonometric Ratios\n")

            print("sin  =", format_value(sinv))
            print("cos  =", format_value(cosv))
            print("tan  =", format_value(tanv))
            print("cosec=", format_value(cscv))
            print("sec  =", format_value(secv))
            print("cot  =", format_value(cotv))

        except:
            a("Invalid angle")

# MAIN MENU
def main():

    a("\n\tWELCOME TO PYTHON SCIENTIFIC CALCULATOR 🙏")

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
            a("Invalid option")

main()