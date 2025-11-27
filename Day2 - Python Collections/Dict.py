#Dictionaries == Key - Value Pairs

#Creating Dictionary

student = {
    'name' : 'Venkat',
    'age' : 21,
    'marks' :85
}

#Accessing values
print(student['name'])
print(student.get("marks")) #Better: Avoids KeyError
print(student.get("usn")) #usn key is not their so it gives output NONE...

#Adding new key-value
student["city"] = "Hyderabad"

#Updating Value
student["age"] = 23

#Removing Key
student.pop("marks")

#Prints a Dictionary
print(student)