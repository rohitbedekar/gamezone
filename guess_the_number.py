from gamecomponents.scoreboard import Scoreboard, Range
from gamecomponents.game_manager import GameManager
from gamecomponents.game_engine import GameEngine


class GuessTheNumber:
    def __init__(self):
        self.__engine = GameEngine()

    def play_game(self, player_name):
        self.__manager = GameManager()
        self.__scoreboard = Scoreboard()
        self.__scoreboard.activate_scoreboard(source=player_name + ".txt")
        self.__manager.set_player_profile(profile=player_name)
        self.__run_game_loop()

    def __run_game_loop(self):
        print("Rules:\n1. Guess number between 1 and 100\n2. Press 0 to exit")

        while not self.__manager.is_correct_guess() and not self.__manager.exit_game():
            self.__manager.new_guess(int(input("Guess the number: ")))

            if self.__manager.exit_game():
                print("Exiting the game...")
                break
            elif self.__manager.is_correct_guess():
                self.__save_scores()
            else:
                self.__additional_hints()

                if self.__engine.is_prime(self.__manager.bonus_hints()) and not self.__manager.get_num_is_prime():
                    self.__manager.set_num_is_prime()

                self.__manager.increment_hint()

                self.__update_score()

    def __additional_hints(self):
        if self.__manager.guess_is_greater():
            print("Guess lower")
        else:
            print("Guess higher")

        if not self.__manager.get_num_is_prime():
            self.__manager.save_bonus_hints(
                self.__engine.get_divisors(
                    self.__manager.actual_number()))

            if self.__manager.hint_count() > 0:
                if self.__manager.has_bonus_hints():
                    print("It is divisible by " + str(
                        self.__manager.get_bonus_hint()))
                else:
                    print(f"All hints: The number is divisible by {', '.join(self.__manager.get_all_bonus_hints())}")
        else:
            print("It is a prime number")

    def __update_score(self):
        if self.__scoreboard.current_score() > 10:
            self.__scoreboard.update_score(
                self.__scoreboard.current_score() - 10)

    def __save_scores(self):
        print(f"Correct! You scored {self.__scoreboard.current_score()} points")
        self.__scoreboard.show_stats(previous_range=Range.LAST5)
        self.__scoreboard.record_score()


game = GuessTheNumber()
game.play_game(player_name='Player1')
