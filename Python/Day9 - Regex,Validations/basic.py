import re

text = "My age is 22"

#re.search() → find first match
result = re.search(r"\d+", text)  # \d+ means one or more digits
print(result.group())


txt = "Numbers: 10, 20, 30"
#re.findall() → find all matches
print(re.findall(r"\d+", txt))


#re.split() → split using pattern
str = "apple,banana; mango|grapes"

print(re.split(r"[;,|]", str))



#re.sub() → replace pattern
sent = "I have 4 apples"

print(re.sub(r"\d","five", sent))

#Anchors
# ^pattern → starts with
# pattern$ → ends with
print(re.match(r"^Hello", "Hello World"))


#Full Matching Patterns
print(re.fullmatch(r"[A-Za-z]+", "Helloworld"))

