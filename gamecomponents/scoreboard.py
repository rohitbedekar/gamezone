import os
from enum import IntEnum


class Range(IntEnum):
    ALL = 0
    LAST5 = -5


class Scoreboard:
    def __init__(self, start_score=100):
        self.__score = start_score
        self.__source = None
        self.__previous_scores_list = []
        self.__previous_scores_loaded = False
        self.__best_score = 0
        self.__start_game = False
        self.__end_game = False

    def activate_scoreboard(self, source):
        self.__source = source

    def best_score(self):
        if self.__previous_scores_loaded:
            self.__best_score = max(self.__previous_scores_list)
            return self.__best_score

    # Async conversion required to reduce delay
    def previous_scores(self):
        if os.path.exists(self.__source):
            with open(self.__source, 'r') as score_file:
                for line in score_file:
                    self.__previous_scores_list.append(line.strip())
            self.__previous_scores_list = list(map(int, self.__previous_scores_list))
            return self.__previous_scores_list
        else:
            return []

    def __has_previous_scores(self):
        if not self.__previous_scores_loaded:
            if len(self.previous_scores()) > 0:
                self.__previous_scores_loaded = True
                return self.__previous_scores_loaded

    def total_score(self):
        return sum(self.__previous_scores_list) + self.__score

    def current_score(self):
        self.__start_game = True
        return self.__score

    def update_score(self, score):
        if self.__start_game and score != self.__score:
            self.__score = score

    def record_score(self):
        if self.__start_game:
            with open(self.__source, 'a') as score_file:
                print(self.__score, file=score_file)

    def show_stats(self, previous_range=Range.ALL):
        if self.__has_previous_scores():
            previous_scores_str_list = ', '.join(
                list(map(str, self.__previous_scores_list[int(previous_range):])))
            print("Previous scores: " + previous_scores_str_list)
            print("Previous best: " + str(self.best_score()))
            print("Total score: " + str(self.total_score()))
