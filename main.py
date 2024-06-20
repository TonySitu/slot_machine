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

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    symbol_pool = []

    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            symbol_pool.append(symbol)

    columns = []
    for _ in range(cols):
        col = []
        current_symbols = symbol_pool[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            col.append(value)

        columns.append(col)

    return columns


def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row])


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


def check_winnings(matrix, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = matrix[0][line]
        for col in matrix:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def game(balance):
    lines = get_number_of_lines()
    bet = check_bet(balance, lines)

    total_bet = bet * lines
    balance -= total_bet

    print(f"You are betting #{bet} on {lines}. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings} on lines: ", *winning_lines)
    balance += winnings
    return balance


def main():
    balance = deposit()
    while True:
        spin = input("Press enter to spin (q to quit).")
        if spin == "q":
            break
        print(f"You left with ${game(balance)}")


if __name__ == "__main__":
    main()
