# for i in range(5):
#     continue
# print(i)

# for i in range(5):
#     break
# print(i)

sum = 0
while True:
    response = (input("enter any number (quit=q): "))
    if(response == 'q'):
        break
    sum += float(response)
    print('sum: ', sum)
    