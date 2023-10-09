def main():
    userinput = int(input('Please type mass in kg: '))
    c = 300000000
    E = userinput * square (c)
    print(E,'J')

def square(n):
    return n * n

main()