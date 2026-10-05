#Summetion of multiple numbers

def add(*data):
    sum = 0
    for val in data:
        sum += val
    return sum

res = add(10,20,30,1,2,3,4,4,6,5,7)
print(res)