def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(number_plate):
    if is_valid_1(number_plate) and is_valid_2(number_plate) and is_valid_3(number_plate) and is_valid_4(number_plate):
        return True
    else:
        return False

def is_valid_1(number_plate_1):
    if number_plate_1[0:2].isalpha():
        return True
    else:
        return False

def is_valid_2(number_plate_2):
    if 2 <= len(number_plate_2) <= 6:
        return True
    else:
        return False

def is_valid_3(number_plate_3):
    if number_plate_3.isalpha():
        return True
    else:
        for i in range(len(number_plate_3)):
            if number_plate_3[i].isdigit():
                if number_plate_3[i] == "0":
                    return False
                elif number_plate_3[i:len(number_plate_3)].isdigit():
                    return True
                else:
                    return False

def is_valid_4(number_plate_4):
    if number_plate_4.isalnum():
        return True
    else:
        return False

        
if __name__ == "__main__":
    main()