# List comprehension = short, clean way to create lists.

#Method 1 --> Normal way
nums = []
for i in range(1,6):
    nums.append(i)
    
print("Nums : ",nums)

"""------------------------------"""
#Method 2 --> Comprehension way
numbers = [i for i in range(1,7)]

print(f"Numbers : {numbers}")

"""------------------------------"""
#Method 3 --> with Condition
even_nums = [i for i in range(1,11) if i % 2 == 0]
print(f"Even Numbers : {even_nums}")

"""------------------------------"""
#Method 4 --> Create Squares
squares = [i*i for i in range(1,11)]
print(f"Squares : {squares}")

