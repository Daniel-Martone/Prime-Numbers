number = 1_000_000 # Sets the starting number
if number % 2 == 0:
    number += 1 
while True:
    number += 2
    is_prime = True
    for c in range(2, number//2):
        if number % c == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
