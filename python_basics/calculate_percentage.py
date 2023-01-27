marks={
    'Math': 80,
    'Science': 77,
    'Computer': 95
}

sum = 0
for i in marks.values():
    sum += i;
percentage = float ((sum/300) * 100)
print(percentage)

if percentage < 33:
    print("fail")
elif percentage < 60:
    print("2nd")
elif percentage < 80:
    print("1st")
else:
    print("dictinction")