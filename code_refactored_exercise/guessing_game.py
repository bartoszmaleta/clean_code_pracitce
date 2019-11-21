import random


def return_list_with_10_random_numbers():
    amount_of_numbers_in_a_list = 10
    lower_bound_of_range = 1
    high_bound_of_range = 99
    a = []
    for i in range(amount_of_numbers_in_a_list):
        a.append(random.randint(lower_bound_of_range, high_bound_of_range))
    return a


def return_second_list_with_10_random_numbers():
    amount_of_numbers_in_a_list = 10
    lower_bound_of_range = 1
    high_bound_of_range = 49
    b = []
    for i in range(amount_of_numbers_in_a_list):
        b.append(random.randint(lower_bound_of_range, high_bound_of_range))
    return b


def getting_list_with_10_random_numbers(choice_of_list):
    amount_of_numbers_in_a_list = 10
    lower_bound_of_range = 1
    high_bound_of_range_a_list = 99
    high_bound_of_range_b_list = 49
    b = []
    a = []
    if choice_of_list == "a":
        for i in range(amount_of_numbers_in_a_list):
            b.append(random.randint(lower_bound_of_range, high_bound_of_range_a_list))
        return b
    elif choice_of_list == "b":
        for i in range(amount_of_numbers_in_a_list):
            a.append(random.randint(lower_bound_of_range, high_bound_of_range_b_list))
        return a