import random

    
def generate_list_with_10_random_numbers(higher_range):
    random_numbers = []
    lower_range = 1
    amount_of_numbers_in_a_list = 10

    for i in range(amount_of_numbers_in_a_list):
        random_numbers.append(random.randint(lower_range, higher_range))
    return random_numbers