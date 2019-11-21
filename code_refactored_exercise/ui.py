# --------------------------
#      second try
# --------------------------


def geussing_number_from_list(list_with_random_numbers, range_of_game):
    amount_of_numbers_in_a_list = 10
    if range_of_game == 99:
        int_range = 99
    elif range_of_game == 49:
        int_range = 49

    for i in range(amount_of_numbers_in_a_list):
        ask_input = int(input(f"Enter an integer from 1 to {int_range}: "))
        while list_with_random_numbers[i] != ask_input:
            if ask_input < list_with_random_numbers[i]:
                print("guess is low")
                ask_input = int(input("Enter an integer from 1 to {}: ".format(int_range)))
            elif ask_input > list_with_random_numbers[i]:
                print("guess is high")
                ask_input = int(input("Enter an integer from 1 to {}: ".format(int_range)))
            else:
                break
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

