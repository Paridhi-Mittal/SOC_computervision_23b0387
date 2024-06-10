num = int(input("Enter a number: "))
max_prime = 1

if num == 2:
    max_prime = 2
elif num == 4:
    max_prime = 4
else:
    for i in range(2, num):
        x = num % i
        if x == 0:
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                max_prime = i

print(max_prime)
            