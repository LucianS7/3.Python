def main():
    food_list = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    price = float(0)
    while True:
        try:
            item = input("What would you like to order: ").lower().title()
            if item in food_list:
                price += float(food_list[item])
                print(f"Total ${price:.2f}")
            else:
                pass
        except EOFError:
            break
    print(f"\nTotal ${price:.2f}")

main ()