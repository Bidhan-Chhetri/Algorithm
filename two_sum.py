list1 = []
list2 = []

for i in range(3):
    l1 = int(input("Enter the list one : "))
    list1.append(l1)
    l2 = int(input("Enter the list two : "))
    list2.append(l2)
print(f"it is list one {list1} and it is list two {list2}")
for j in range(3):
        print(f"{list1[j] + list2[j]}")
