# Lists are Ordered and Mutable

#Creating a list of numbers

numbers = [10, 20, 30, 40, 50]

#Accessing elements using index
print(numbers[0]) #First Element (10)
print(numbers[1]) #Second Element (20)
print(numbers[-1]) #Last Element (50)

# list Methods

nums = [11, 12, 13, 14]

nums.append(4) #Adds element at end
nums.insert(1,10) #Inserts 10 at index 1
nums.pop() #Removes last element
nums.remove(12) #Removes the value 2
nums.sort() #Sorts list in Ascending Order

print(nums)

# List Slicing

print(numbers[1:4]) #From index 1 to 3 -> [20,30,40]
print(numbers[:3]) #From start to index 2
print(numbers[2:]) #From index 2 to end