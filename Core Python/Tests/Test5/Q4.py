li= [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
di = {}
for num in li:
    if num in di:
        di[num] += 1
    else:
        di[num] = 1

print(di)