number = 1_000_000
if number % 2 == 0:
    number += 1
print('2')
while True:
    number += 4
    is_prime = True
    for c in range(2, number//2):
        if number % c == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
    