#1. pass
#for i in range(1, 10):
#   pass

#2. break
# for i in range(1, 10):
#     if(i == 3):
#         break
#     print(i)

#3. continue
# for i in range(1, 10):
#     if(i == 3):
#         continue
#    print(i)

#4. else using break
for i in range(1,10):
    if(i == 3):
        break
    print(i)
else:
    print('Else block executed')

#5. else using continue
for i in range(1,10):
    if(i == 3):
        continue
    print(i)
else:
    print('Else block executed')