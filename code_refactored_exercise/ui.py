# --------------------------
#      second try
# --------------------------


def geussing_number_from_list(list_with_random_numbers, high_range_of_game):
    # amount_of_numbers_in_a_list = 10
    int_range_low = 1

    for number in list_with_random_numbers:
        ask_input = 0
        while number != ask_input:
            ask_input = int(input(f"Enter an integer from {int_range_low} to {high_range_of_game}: "))
            if ask_input < number:
                print("guess is low")
            elif ask_input > number:
                print("guess is high")
        win_text = "you guessed it!"
        print(win_text)


# --------------------------
#      first try
# --------------------------

# def geussing_from_a_list(list_with_random_numbers):
#     amount_of_numbers_in_a_list = 10
#     for i in range(amount_of_numbers_in_a_list):
#         ask_input = int(input("Enter an integer from 1 to 99: "))
#         while list_with_random_numbers[i] != ask_input:
#             if ask_input < list_with_random_numbers[i]:
#                 print("guess is low")
#                 ask_input = int(input("Enter an integer from 1 to 99: "))
#             elif ask_input > list_with_random_numbers[i]:
#                 print("guess is high")
#                 ask_input = int(input("Enter an integer from 1 to 99: "))
#             else:
#                 break
#         win_text = "you guessed it!"
#         print(win_text)


# def geussing_from_b_list(list_with_random_numbers):
#     amount_of_numbers_in_a_list = 10
#     for i in range(amount_of_numbers_in_a_list):
#         ask_input = int(input("Enter an integer from 1 to 49: "))
#         while list_with_random_numbers[i] != ask_input:
#             if ask_input < list_with_random_numbers[i]:
#                 print("guess is low")
#                 ask_input = int(input("Enter an integer from 1 to 49: "))
#             elif ask_input > list_with_random_numbers[i]:
#                 print("guess is high")
#                 ask_input = int(input("Enter an integer from 1 to 49: "))
#             else:
#                 break
#         win_text = "you guessed it!"
#         print(win_text)


# def geussing_from_list(list_with_random_numbers, range):
#     if range == 99:
#         geussing_from_a_list(list_with_random_numbers)
#     elif range == 49:
#         geussing_from_b_list(list_with_random_numbers)

