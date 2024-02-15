#!/usr/bin/python3

for i in range(1, 101):
    if i % 15 == 0:
        print(f"FizzBuzz", end=" ")
    elif i % 3 == 0:
        print(f"Fizz", end=" ")
    elif i % 5 == 0:
        print(f"Buzz", end=" ")
    else:
        print(i, end=" ")
    if i == 100:
        print()