# Write a Python program that finds the maximum and minimum values in a list of numbers.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
sum = 0
temp = 0
min = 0
max = 0
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
    if (min > entry):
        min = entry
    if (max < entry):
        max = entry
print(min, "is the minmum")
print(max, "is the maximum")
