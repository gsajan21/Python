word = "racecar"
reversed_word = reversed(word)


print('palindrome:', word == word[::-1])
print('palindrome: ', 'Yes it is' if word == word[::-1] else 'No')
    