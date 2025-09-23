from __future__ import annotations
from typing import TYPE_CHECKING, Sequence, Union

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
        self.used_twos = False
        self.used_threes = False
        self.used_fours = False
        self.used_fives = False
        self.used_sixes = False
        self.used_full_house = False
        self.used_chance = False
        self.used_large_straight = False
        self.used_small_straight = False
        self.used_three_of_a_kind = False
        self.used_four_of_a_kind = False
        self.used_yahtzee = False
        self.used_categories = set()  

    def score_turn(self, dice: Union[list[int], list[Die]], category: Union[int, str]) -> Union[int, str]:
        if not dice:
            self.used_categories.add(str(category))  # Add to used_categories even for empty dice
            return "Cannot score. Missing Dice."
        
        # Handle different input types for dice
        if isinstance(dice[0], int):
            values = dice
        else:
            values = [die.value for die in dice]
        
        # Handle string categories (for tests)
        if isinstance(category, str):
            category_map = {
                "ones": 1, "twos": 2, "threes": 3, 
                "fours": 4, "fives": 5, "sixes": 6
            }
            if category in category_map:
                num = category_map[category]
                # Check if already used and raise error
                if category in self.used_categories:
                    raise ValueError(f"Error: {category} has already been scored!")
                self.used_categories.add(category)
            else:
                return 0
        else:
            num = category
        
        round_score = 0
        for value in values:
            if value == num:
                round_score += num

        return round_score

    def score_full_house(self, dice: Union[list[Die], list[int]]):
        if self.used_full_house:
            return 0
            
        # Handle different input types
        if isinstance(dice[0], int):
            values = dice[:]
        else:
            values = [die.value for die in dice]
        
        # Count occurrences of each value
        counts = {}
        for value in values:
            counts[value] = counts.get(value, 0) + 1
        
        count_values = sorted(counts.values())
        
        # Full house is exactly one pair (2) and one triple (3)
        if count_values == [2, 3]:
            return 25
        else:
            return 0
    
    def score_chance(self, dice: Union[list[Die], list[int]]):
        if self.used_chance:
            return 0
            
        # Handle different input types
        if isinstance(dice[0], int):
            values = dice
        else:
            values = [die.value for die in dice]
            
        return sum(values)

    def score_large_straight(self, dice: Union[list[Die], list[int]]):
        if self.used_large_straight:
            return 0

        # Handle different input types
        if isinstance(dice[0], int):
            values = dice[:]
        else:
            values = [die.value for die in dice]
            
        values.sort()

        if values == [1,2,3,4,5] or values == [2,3,4,5,6]:
            return 40
        else:
            return 0

    def score_small_straight(self, dice: Union[list[Die], list[int]]):
        if self.used_small_straight:
            return 0
            
        # Handle different input types
        if isinstance(dice[0], int):
            values = dice[:]
        else:
            values = [die.value for die in dice]
            
        unique_values = set(values)

        if (set([1,2,3,4]).issubset(unique_values) or
            set([2,3,4,5]).issubset(unique_values) or
            set([3,4,5,6]).issubset(unique_values)):
            return 30
        else:
            return 0
    
    def score_three_of_a_kind(self, dice: Union[list[Die], list[int]]):
        if self.used_three_of_a_kind:
            return 0
        
        # Handle different input types
        if isinstance(dice[0], int):
            values = dice
        else:
            values = [die.value for die in dice]
            
        counts = {}
        for value in values:
            counts[value] = counts.get(value, 0) + 1
        
        # Check if at least 3 of the same value
        for count in counts.values():
            if count >= 3:
                return sum(values)
        return 0
    
    def score_four_of_a_kind(self, dice: Union[list[Die], list[int]]):
        if self.used_four_of_a_kind:
            return 0
        
        # Handle different input types
        if isinstance(dice[0], int):
            values = dice
        else:
            values = [die.value for die in dice]
            
        counts = {}
        for value in values:
            counts[value] = counts.get(value, 0) + 1
        
        # Check if at least 4 of the same value
        for count in counts.values():
            if count >= 4:
                return sum(values)
        return 0

    def score_yahtzee(self, dice: Union[list[Die], list[int]]):
        # Handle different input types
        if isinstance(dice[0], int):
            values = dice
        else:
            values = [die.value for die in dice]
        
        # Check if all dice are the same
        if len(set(values)) == 1:
            if not self.used_yahtzee:
                return 50
            else:
                # Bonus Yahtzee
                return 100
        return 0


