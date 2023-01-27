# for i in range(5,0,-1):
#     print('{:>10}'.format("* "*i))


for i in range(5):
    for j in range(5):
        if i > j: print(' ', end=' ')
        else: print('*', end=' ')
    print()