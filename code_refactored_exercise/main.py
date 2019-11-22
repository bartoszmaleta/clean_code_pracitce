import guessing_game as guessing_game
import ui as ui


def main():
    RANGE = 99
    list_with_10_random_numbers = guessing_game.generate_list_with_10_random_numbers(RANGE)
    ui.geussing_number_from_list(list_with_10_random_numbers, RANGE)
    # ui.geussing_from_list(list_with_10_random_numbers, RANGE)     # first try

    RANGE = 49
    list_with_10_random_numbers = guessing_game.generate_list_with_10_random_numbers(RANGE)
    ui.geussing_number_from_list(list_with_10_random_numbers, RANGE)
    # ui.geussing_from_list(list_with_10_random_numbers, RANGE)     # first try


main()