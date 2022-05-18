def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1
        
while True:
    n = collatz(int(input("Type in a whole number or 'q' to quit.\n")))
    while n != 1:
        n = collatz(n)