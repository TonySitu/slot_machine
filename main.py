import random

MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for col in range(cols):
        for row in range(rows):
            value = random.choice(all_symbols)


def deposit():
    while True:
        amount = input("How much are you depositing? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be between ${MIN_LINES} - ${MAX_LINES}")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        bet = input("How much are you betting? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")

    return bet


def check_bet(balance, lines):
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet on that, you r current balance is ${balance}")
        else:
            return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = check_bet(balance, lines)

    total_bet = bet * lines
    print(f"You are betting #{bet} on {lines}. Total bet is equal to: ${total_bet}")


if __name__ == "__main__":
    main()
