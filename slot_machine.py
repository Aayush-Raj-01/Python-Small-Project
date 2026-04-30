balance = 0
MAX_LINE = 3
def deposit():
    while True:
        amount = input("Amount to be Deposit = $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount is invalid")
        else:
            print("Amount is invalid")
    return amount

def get_number_of_line():
     while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINE) + ")? = ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print("Amount is invalid")
        else:
            print("Amount is invalid")
    return lines


def main():
    print(f"Your balance is ${balance}\nDo you wanna play a game or deposit")
    amount = deposit()
main()

print(MAX_LINE)