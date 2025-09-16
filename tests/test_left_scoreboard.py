import pytest
from scorecard import Scorecard

def test_score_ones():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,1,2,3,4], "ones")
    assert score == 2

    # A new instance for the second test is good practice
    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,1,2,1,1], "ones")
    assert score == 4

    testing_sc = Scorecard()
    score = testing_sc.score_turn([5,5,5,5,5], "ones")
    assert score == 0

def test_try_to_score_after_scoring():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,1,2,3,4], "ones")
    assert score == 2
    
    with pytest.raises(ValueError, match="Error: ones has already been scored!"):
        testing_sc.score_turn([1,1,2,1,1], "ones")

def test_score_ones_no_dice():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([], "ones")
    assert score == "Cannot score. Missing Dice."
    assert "ones" in testing_sc.used_categories