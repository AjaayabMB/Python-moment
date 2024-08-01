# Write a Python function that takes two lists
# and returns a new list containing only the elements that are common to both lists.
def find_common_elements(list_1, list_2):
    a = len(list_1)
    b = len(list_2)
    common = []
    for i in range(0, a):
        for j in range(0, b):
            if (list_1[i] == list_2[j]):
                common.append(list_1[i])
    return common


list_1 = []
list_2 = []
x = int(input("Enter the number of entries for first list:"))
total_entries_1 = range(0, x)
for a in total_entries_1:
    entry_1 = int(input("Enter a number"))
    list_1.append(entry_1)
y = int(input("Enter the number of entries for second list:"))
total_entries_2 = range(0, y)
for a in total_entries_2:
    entry_2 = int(input("Enter a number"))
    list_2.append(entry_2)
print(find_common_elements(list_1, list_2))
