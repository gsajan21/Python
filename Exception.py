try:
    numbers = [2,4,5,63,5,7,0]
    print(numbers)
    print(numbers[10])
    print(numbers[1]/numbers[-1])
except ZeroDivisionError:
    print("Denomination cannot be 0.")
except IndexError:
    print("Index Out of Bound.")