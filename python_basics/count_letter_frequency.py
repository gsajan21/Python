# import string

given_str = "the quick brown fox jumps over the lazy dog"
# print(string.__file__)
# print(*string.ascii_lowercase)
# count = [0] * 26
# print(count)
# for i in given_str:

# u=input('enter a sentence: ')
# a=u.replace(" ","").lower()
# s=0
# x=['abcdefghijklmnopqrstuvwxyz']
# for j in x:
#     for j in a:
#         s=a.count(j)
#         print(j , s)

alpha = [0] * 26
for c in given_str:
    if c.isalpha() is True:
        i = ord(c) - ord('a')
        alpha[i] +=1

import string
print(*string.ascii_lowercase)
print(*alpha)

