list1 = ["car", "bike", "motorbike", "train"]
list2 = []
'''
for vehicle in list1:
    for empty in vehicle:
        list2.append(empty)

print(list2)
'''

for vehicle in list1:
    for empty in vehicle:
        #not allowing duplicates to store in list2
        if empty not in list2:
            list2.append(empty)

print(list2)
