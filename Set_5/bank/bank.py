def main():
     user_input = input ("Greeting: ")
     match value(user_input):
          case 0:
               print ("$0")
          case 20:
               print("$20")
          case _:
               print ("$100")

def value(greeting):
     greeting = greeting.lower().strip()
     if greeting[0:5] == "hello":
          return 0
     elif greeting[0] == "h":
          return 20
     else:
          return 100


if __name__ == "__main__":
     main()