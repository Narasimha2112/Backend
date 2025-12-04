# Sets are Un-Ordered and Uniques Items..

#creating a set
s = {10, 20, 30, 40, 20}

#Duplicate 20 is removed automatically
print(s)

s.add(60)  #Add Element
s.remove(20) #Remove Element (Error if not present)
s.discard(50) #Remove Safely (no error)

print(s)
