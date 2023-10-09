def main():
    text = input ("Please input the name of the variable in camelCase: ")
    snake_case(text)

def snake_case(txt):
    for i in txt:
        if i.islower():
            print(i , end="")
        else:
            print(f"_{i.lower()}", end="")
    print()

main()