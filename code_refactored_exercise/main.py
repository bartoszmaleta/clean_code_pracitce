import guessing_game as guessing_game
import ui as ui


def main():
    list_with_10_random_numbers = guessing_game.getting_list_with_10_random_numbers("a")
    RANGE = 99
    ui.geussing_from_list(list_with_10_random_numbers, RANGE)
    
    list_with_10_random_numbers = guessing_game.getting_list_with_10_random_numbers("b")
    RANGE = 49
    ui.geussing_from_list(list_with_10_random_numbers, RANGE)


main()