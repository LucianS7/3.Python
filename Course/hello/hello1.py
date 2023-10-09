name =  (input("What's your name? "))

with open ("names.txt", "a") as file
    file.write(f"{name}\n")


#for name in sorted(names):
#    print (f"hello, {name}")
