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


def geussing_from_a_list(list_with_random_numbers):
    for i in range(amount_of_numbers_in_a_list):
        g = int(input("Enter an integer from 1 to 99: "))
        while list_with_random_numbers[i] != g:
            if g < list_with_random_numbers[i]:
                print("guess is low")
                g = int(input("Enter an integer from 1 to 99: "))
            elif g > list_with_random_numbers[i]:
                print("guess is high")
                g = int(input("Enter an integer from 1 to 99: "))
            else:
                break
        win_text = "you guessed it!"
        print(win_text)
        # return win_text


def geussing_from_b_list(list_with_random_numbers):
    for i in range(amount_of_numbers_in_a_list):
        g = int(input("Enter an integer from 1 to 49: "))
        while list_with_random_numbers[i] != g:
            if g < list_with_random_numbers[i]:
                print("guess is low")
                g = int(input("Enter an integer from 1 to 49: "))
            elif g > list_with_random_numbers[i]:
                print("guess is high")
                g = int(input("Enter an integer from 1 to 49: "))
            else:
                break
        win_text = "you guessed it!"
        print(win_text)
        # return win_text


list_with_10_numbers = return_list_with_10_random_numbers()
geussing_from_a_list(list_with_10_numbers)

second_list_with_10_numbers = return_second_list_with_10_random_numbers()
geussing_from_b_list(second_list_with_10_numbers)