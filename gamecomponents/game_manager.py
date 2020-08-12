import random


class GameManager:
    def __init__(self):
        self.__player = "Player1"
        self.__num = random.randint(1, 100)
        self.__guess = 0.1
        self.__hint_counter = 0
        self.__num_is_prime = False
        self.__bonus_hints = {}

    def set_player_profile(self, profile):
        self.__player = profile

    def actual_number(self):
        return self.__num

    def exit_game(self):
        return self.__guess == 0

    def new_guess(self, guess):
        self.__guess = guess

    def is_correct_guess(self):
        return self.__guess == self.__num

    def guess_is_greater(self):
        return self.__guess > self.__num

    def hint_count(self):
        return self.__hint_counter

    def increment_hint(self):
        self.__hint_counter += 1

    def save_bonus_hints(self, hints):
        self.__bonus_hints = hints

    def has_bonus_hints(self):
        return len(self.__bonus_hints) > self.__hint_counter

    def bonus_hints(self):
        return self.__bonus_hints

    def get_bonus_hint(self):
        return self.__bonus_hints[self.__hint_counter]

    def get_all_bonus_hints(self):
        return map(str,
                   list(self.__bonus_hints.values()))

    def get_num_is_prime(self):
        return self.__num_is_prime

    def set_num_is_prime(self):
        self.__num_is_prime = True
