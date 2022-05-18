import random, time, sys

wins = 0
losses = 0
ties = 0

while True:
    print(f"\nROCK, PAPER, SCISSORS\n{wins} Wins, {losses} Losses, {ties} Ties")
    n = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n")
    rand = random.randint(1, 3)
    if n == "r" and rand == 1:
        print("ROCK versus...")
        time.sleep(1)
        print("ROCK")
        time.sleep(1)
        print("It's a tie!")
        ties = ties + 1
    if n == "r" and rand == 2:
        print("ROCK versus...")
        time.sleep(1)
        print("PAPER")
        time.sleep(1)
        print("You lose!")
        losses = losses + 1
    if n == "r" and rand == 3:
        print("ROCK versus...")
        time.sleep(1)
        print("SCISSORS")
        time.sleep(1)
        print("You win!")
        wins = wins + 1
    if n == "p" and rand == 1:
        print("PAPER versus...")
        time.sleep(1)
        print("ROCK")
        time.sleep(1)
        print("You win!")
        wins = wins + 1
    if n == "p" and rand == 2:
        print("PAPER versus...")
        time.sleep(1)
        print("PAPER")
        time.sleep(1)
        print("It's a tie!")
        ties = ties + 1
    if n == "p" and rand == 3:
        print("PAPER versus...")
        time.sleep(1)
        print("SCISSORS")
        time.sleep(1)
        print("You lose!")
        losses = losses + 1
    if n == "s" and rand == 1:
        print("SCISSORS versus...")
        time.sleep(1)
        print("ROCK")
        time.sleep(1)
        print("You lose!")
        losses = losses + 1
    if n == "s" and rand == 2:
        print("SCISSORS versus...")
        time.sleep(1)
        print("PAPER")
        time.sleep(1)
        print("You win!")
        wins = wins + 1
    if n == "s" and rand == 3:
        print("SCISSORS versus...")
        time.sleep(1)
        print("SCISSORS")
        time.sleep(1)
        print("It's a tie!")
        ties = ties + 1
    if n == "q":
        print("Thanks for playing!")
        time.sleep(2)
        sys.exit()
    