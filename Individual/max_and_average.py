def main():
    nr_list = get_numbers()
    max_ = max(nr_list)
    average_ =  sum(nr_list) / len(nr_list)
    print (f"The maximum number is: {max_}")
    print (f"The average is: {average_:.2f}")


def get_numbers():
    nr_list = []
    print("Enter a number or q to stop:")
    while True:
        nr_str = input()
        if nr_str == "q":
            break
        try:
            nr_list += [int(nr_str)]
        except ValueError:
            print("not a number - enter a number or press q if you want to stop")
            continue
    return nr_list


if __name__ == "__main__":
    main()


