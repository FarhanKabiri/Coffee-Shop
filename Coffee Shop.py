
def size():         # Defining sizes of cups
    return {"small": 9, "medium": 12, "large": 15}

def cost():         # Defining costs of each cups
    return {"small": 1.75, "medium": 1.90, "large": 2.00}

def menu():               # Menu for user to choose from
    print("1: Enter 1 to order coffee.")
    print("2: Enter 2 to check the total money made up to this time.")
    print("3: Enter 3 to check the total amount of coffee sold up to this time.")
    print("4: Enter 4 to check the number of cups of coffee of each size sold.")
    print("5: Enter 5 to print the data.")
    print("9: Enter 9 to exit the program.")
def buy_coffee():  # Values
    sizes = size()
    costs = cost()
    total_cost = 0
    total_cups = {sizes["small"]: 0, sizes["medium"]: 0, sizes["large"]: 0}
    while True:
        print("1: Enter 1 to buy coffee in a small cup size (9 oz)")
        print("2: Enter 2 to buy coffee in a medium cup size (12 oz)")
        print("3: Enter 3 to buy coffee in a large cup size (15 oz)")
        print("9: Enter 9 to exit.")
        choice = input()
        if choice == '9':
            break
        elif choice == '1':
            cup_size = sizes["small"]
            cup_cost = costs["small"]
        elif choice == '2':
            cup_size = sizes["medium"]
            cup_cost = costs["medium"]
        elif choice == '3':
            cup_size = sizes["large"]
            cup_cost = costs["large"]
        else:
            print("Invalid Choice, Try Again")
            continue
        num_cups = int(input("Enter the number of cups: "))
        total_cups[cup_size] += num_cups
        total_cost += num_cups * cup_cost

    print("Please pay ${:.2f}".format(total_cost))
    return (total_cost, total_cups)



def check_total_money_made(total_cost): # calculate the total money made
    print("Total money made: ${}".format(total_cost))

def check_total_coffee_sold(total_cups): # the amount of coffe sold in oz
    total_amount = 0
    for size, count in total_cups.items():
        total_amount += size * count
    print("Total amount of coffee sold: {} oz".format(total_amount))


def check_number_of_cups_sold(total_cups): # different sizes of coffee cups sold
    print("Small cup count: {}".format(total_cups[size()["small"]]))
    print("Medium cup count: {}".format(total_cups[size()["medium"]]))
    print("Large cup count: {}".format(total_cups[size()["large"]]))


def data(total_cost, total_cups): # all the data included here
    check_total_money_made(total_cost)
    check_total_coffee_sold(total_cups)
    check_number_of_cups_sold(total_cups)

def main():
    total_cost = 0
    total_cups = {size()["small"]: 0, size()["medium"]: 0, size()["large"]: 0}
    while True:
        menu()
        choice = input()
        if choice == '9':
            break
        elif choice == '1':
            cost, cups = buy_coffee()
            total_cost += cost
            for cup_size, num_cups in cups.items():
                total_cups[cup_size] += num_cups

        elif choice == '2':
            check_total_money_made(total_cost)
        elif choice == '3':
            check_total_coffee_sold(total_cups)
        elif choice == '4':
            check_number_of_cups_sold(total_cups)
        elif choice == '5':
            data(total_cost, total_cups)
        elif choice == '9':
            break

main()
