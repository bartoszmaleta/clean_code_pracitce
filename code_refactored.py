import math
import random

a = []
b = []
amount_of_numbers_in_a_list = 10
lower_bound_of_range = 1
high_bound_of_range = 99


def return_list_with_10_random_numbers():
    for i in range(amount_of_numbers_in_a_list):
        a.append(random.randint(lower_bound_of_range, high_bound_of_range))
    return a


def return_second_list_with_10_random_numbers():
    for i in range(amount_of_numbers_in_a_list):
        b.append(random.randint(lower_bound_of_range, high_bound_of_range))
    return b


list_with_10_numbers = return_list_with_10_random_numbers()

for i in range(amount_of_numbers_in_a_list):
    g = int(input("Enter an integer from 1 to 99: "))
    while list_with_10_numbers[i] != g:
        if g < list_with_10_numbers[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > list_with_10_numbers[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")


second_list_with_10_numbers = return_second_list_with_10_random_numbers()

for i in range(amount_of_numbers_in_a_list):
    g = int(input("Enter an integer from 1 to 49: "))
    while second_list_with_10_numbers[i] != g:
        if g < second_list_with_10_numbers[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > second_list_with_10_numbers[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")