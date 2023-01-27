# count = 0
# for i in range(10,100):
#     c = str(i)
#     if int(c[0]) < int(c[1]):
#         count+=1
#         print(i, end=' ')
# print(count)

numbers = []
count = 0
for i in range(10, 100):
    tens, ones = divmod(i, 10)
    if tens < ones:
        count += 1
        numbers.append(i)

print(numbers)
print(count)

# tuple
tup = (1, 2, 5, 3)
print(tup)