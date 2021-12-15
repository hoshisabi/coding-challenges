menu_arr = [("Gang Gai", 10.00), ("Pad Thai", 8.75), ("Pad Cashew", 9.50), ("Pad Prik", 10.25),
            ("Peanut Curry", 10.25), ("Curry Noodle", 11.25)]


def print_menu():
    print("%-6s %-15s  %-8s" % ("Dish No.", "Dish Name", "Price"))
    print("%-6s %-15s  %-8s" % ("--------", "---------", "-----"))
    for i in range(len(menu_arr)):
        print("%6d:  %-15s  $%5.2f" % (i + 1, menu_arr[i][0], menu_arr[i][1]))


def get_senior_discount(item):
    senior = input("Are you 65 years old or older (Y or N)?")
    if senior and senior.upper()[0] == "Y":
        return item * 0.1
    else:
        return 0


def display_bill(order, total_senior_discount):
    total_of_all_items = 0.00
    total_taxes = 0.00
    for price in order:
        total_of_all_items += price[1]

    # apply taxes
    total_taxes = total_of_all_items * 0.06

    # calculate overall total
    total = total_of_all_items + total_taxes - total_senior_discount

    print("Bill Information")
    print("---------------------------------------------------")

    i = 0
    for item in order:
        i += 1
        print("%2d %-15s %5.2f" % (i, item[0], item[1]))
    print("---------------------------------------------------")
    print("%25s: %6.2f" % ("Total of all items", total_of_all_items))
    print("%25s: %6.2f" % ("Total senior discounts", total_senior_discount))
    print("%25s: %6.2f" % ("Taxes", total_taxes))


def main():
    order = []
    senior_discount = 0
    done = False

    while not done:
        print_menu()
        choice: int = (int(input("Enter the item number you want (1-6):")))
        if 1 <= choice <= 6:
            item = menu_arr[choice - 1]
            order += [item]
            senior_discount += get_senior_discount(item[1])
        else:
            print("Invalid item choice. Enter valid item number (1-6): ")
            continue

        another = input("Would you like to order another item (Y or N)?")
        if another and another.upper()[0] == "N":
            done = True

    display_bill(order, senior_discount)


main()
