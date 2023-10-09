def main():
    math = input("Please type the arithmetic expression you want to calculate: ").strip()
    x, y, z = math.split(" ")
    math_interpreter(x,y,z)

def math_interpreter(a,b,c):
    a = float(a)
    c = float(c)
    match b:
        case "+":
           print(f"{a+c:.1f}")
        case "-":
            print(f"{a-c:.1f}")
        case "*":
            print(f"{a*c:.1f}")
        case "/":
            if c != 0:
                print(f"{a/c:.1f}")
            else:
                print("can't divide by 0")
        case _:
            print ("the operator is not supported")

main()