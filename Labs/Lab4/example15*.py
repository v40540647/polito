from random import randint


def is_power_of(number, base):

    if number < 2:
        return False
    else:
        while number > 1:
            if number % base == 0:
                number //= base
            else:
                return False
        else:
            return True


def computer_move(stupid_mode, pile_size):
    marbles_removed = 0
    if stupid_mode:
        if int(pile_size/2) >= 1:
            marbles_removed = randint(1, int(pile_size/2))
        else:
            marbles_removed = 1
    else:
        i = int(pile_size/2)
        while not is_power_of(i, 2):
            if i > 1:
                i -= 1
            else:
                i = 2
        else:
            marbles_removed = i-1

    return marbles_removed


def check_winner(pile_size, last_player):
    if pile_size <= 0:
        winner = not last_player
        return winner
    return None


# Generate a random integer between 10 and 100 to denote the initial size of the pile.
pile_size = randint(10, 100)

# Generate a random integer between 0 and 1 to decide whether the computer(0) or the human(1) takes the first turn.
COMPUTER = 0
HUMAN = 1
starter = randint(COMPUTER, HUMAN)

# Generate a random integer between 0 and 1 to decide whether the computer plays smart(0, False) or stupid(1, True).
stupid = 1 #randint(0, 1)
if stupid:
    print("The computer is stupid")
else:
    print("The computer is smart")

if starter == COMPUTER:
    print("COMPUTER TURN")
    removed = computer_move(stupid, pile_size)
    pile_size -= removed

winner = None

while pile_size > 0:
    removed = 0
    print("YOUR TURN")
    while (removed > int(pile_size/2) and pile_size > 1) or removed < 1:
        # this way the users can't select a value greater than the pile size/2 or skip the turn
        removed = int(input(f"pile has {pile_size} marbles, remove: "))

    pile_size -= removed
    winner = check_winner(pile_size, HUMAN)

    if winner is None:
        print("COMPUTER TURN")
        removed = computer_move(stupid, pile_size)
        pile_size -= removed
        winner = check_winner(pile_size, COMPUTER)


if winner == COMPUTER:
    print("The COMPUTER won")
elif winner == HUMAN:
    print("The HUMAN won")
else:
    print("ERROR")
