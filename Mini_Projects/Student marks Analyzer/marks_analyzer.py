"""
Mini Project == Student Marks Analyzer

Input:
    -> List of marks
    -> Show highest, lowest, average, pass/fail count

"""

#List of marks
marks = [34, 52, 36, 58, 96, 57, 68, 81, 73, 48, 92, 25, 31]

#Highest Marks
highest = max(marks)

#Lowest Marks
lowest = min(marks)

#Average Marks
average = sum(marks) / len(marks)

#Pass Count (>=45)
pass_count = 0
for m in marks:
    if m >= 50:
        pass_count += 1


#Fail Count
fail_count = len(marks) - pass_count

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")