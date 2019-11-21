def geussing_from_a_list(list_with_random_numbers):
    amount_of_numbers_in_a_list = 10
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


def geussing_from_b_list(list_with_random_numbers):
    amount_of_numbers_in_a_list = 10
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

