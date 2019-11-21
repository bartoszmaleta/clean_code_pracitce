import guessing_game as guessing_game
import ui as ui


def main():
    list_with_10_random_numbers = guessing_game.getting_list_with_10_random_numbers("a")
    ui.geussing_from_a_list(list_with_10_random_numbers)

    list_with_10_random_numbers = guessing_game.getting_list_with_10_random_numbers("b")
    ui.geussing_from_b_list(list_with_10_random_numbers)


main()