#Convert list to dictionary with index

names = ["raj", "raja", "rakes"]

result = {}

#Using Index and Value
for i in range(len(names)):
    result[i] = names[i] #key = index, value = name
    
print(result)
