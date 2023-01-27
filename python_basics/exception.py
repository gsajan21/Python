# accumulator = 0
# l = list()
# while True:
#     response = input('enter any number (quit=q): ')
#     if response == 'q': break
#     try:
#         l.append(response)
#     except Exception as e:
#         continue4

# print(sum(l))
# print(f'avg: {sum(l)/len(l)} high: {max(l)} low: {min(l)}' )


accumulator = count = 0
high, low = float('-inf'), float('inf')
while True:
    response = input('enter any number (quit: q): ')
    if response == 'q': break
    try:
         num = float(response)
    except Exception: continue
    high, low = max(high, num), min(low, num)
    accumulator += num
    count += 1
print('sum:', accumulator)
print('avg:', accumulator/count, 'high:', high, 'low:', low)


