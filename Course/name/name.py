import sys

if len(sys.argv) < 2:
    sys.exit("Two few arguments")
#elif len(sys.argv) >2:
#    sys.exit("Too many arguments")

for arg in sys.argv[1:-1]:
    print("Hello my name is", arg)