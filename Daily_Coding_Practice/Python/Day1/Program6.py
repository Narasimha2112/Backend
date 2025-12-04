#Check if number is Prime or not

num = int(input("Enter a number: "))

if num < 2:
    print(f"Not a Prime Number....")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(f"Prime Number")
    else:
        print(f"Not a prime number")