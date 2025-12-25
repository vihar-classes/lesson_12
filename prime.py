lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"Prime numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
