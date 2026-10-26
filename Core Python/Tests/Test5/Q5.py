li1 = []
n = int(input("Enter No. of elements:"))

for i in range(n):
    x = int(input("Enter element: "))
    li1.append(x)
li2 = []
n = int(input("Enter No. of elements:"))
for i in range(n):
    x = int(input("Enter element: "))
    li2.append(x)
print('li1:',li1)
print('li2:',li2)

union = []
for num in li1:
    if num not in union:
        union.append(num)
for num in li2:
    if num not in union:
        union.append(num)
print("Union of two lists:", union)