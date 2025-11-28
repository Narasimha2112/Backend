# Recursive function: sum of numbers 1 to N

def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)

print(total(6))