# Write a Python function that converts a list of tuples into a dictionary,
# where the first element of each tuple is the key and the second element is the value.
def tu_dict(list):
    dicti={}
    for c in range(0,len(list)):
        for z in list[c]:
            dicti[list[c]]=z[1]
            # dicti[list[c]]=z[1] for z in list
    return dicti

list=[]
tup=()
temp=[]
x = int(input("Enter the number of entries in list:"))
for a in range(0, x):
    y=int(input("Enter the number of entries in tuple:"))
    for b in range(0,y):
        entry = input("Enter an element:")
        temp.append(entry)
    tup=tuple(temp)
    list.append(tup)
    temp=[]
print(tu_dict(list))