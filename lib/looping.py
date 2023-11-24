#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [num ** 2 for num in int_list]


def fizzbuzz_printer():
    for num in range(1, 101):
        fizzbuzz(num)

def fizzbuzz(num):
    # code goes here!
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    
fizzbuzz_printer()
