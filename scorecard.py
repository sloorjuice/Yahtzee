from __future__ import annotations
from typing import TYPE_CHECKING, Sequence

# After you collect points verify that they are actually added to the total points
# After you collect points for a cateogry that cateogry shouldnt let you add points to your total points
# Make sure user cant roll after their are out of rolls for their turn
# Make sure users can roll properly

if TYPE_CHECKING:
    from die import Die

class Scorecard:
    def __init__(self):
        self.score = 0
        self.used_ones = False

    def score_turn(self, dice: list[int], num: int) -> int:
        round_score = 0

        if num == 1:
            self.used_ones == True
        elif num == 2:
            self.used_twos == True
        elif num == 3:
            self.used_threes == True
        elif num == 4:
            self.used_fours == True
        elif num == 5:
            self.used_fives == True
        elif num == 6:
            self.used_sixes == True

        for die in dice:
            if die == num:
                round_score += num
        #print(f"Ones Round Score: {round_score}")

        self.score += round_score
        self.ones = round_score
        return round_score

    def score_full_house(self, dice: list[Die]):
        round_score = 0
        values = [die.value for die in dice]
        values.sort()

        if values[0] == values[1] and values[2] == values[3] and values[3] == values[4]:
            round_score = 25
        elif values[0] == values[1] and values[1] == values[2] and values[3] == values[4]:
            round_score = 25
        else:
            round_score = 0

        return round_score
