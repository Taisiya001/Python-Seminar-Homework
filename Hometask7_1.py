one_number = int(input())
second_number = input()
numbers = second_number.split()
numbers.reverse()
while one_number != 0:
    n = numbers[0]
    print((n + " "), end="")
    numbers.pop(0)
    one_number = len(numbers)
1