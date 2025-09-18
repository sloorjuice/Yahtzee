import pytest
from scorecard import Scorecard

def test_score_ones():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,1,2,3,4], "ones")
    assert score == 2

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,1,2,1,1], "ones")
    assert score == 4

    testing_sc = Scorecard()
    score = testing_sc.score_turn([5,5,5,5,5], "ones")
    assert score == 0

def test_score_twos():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([2,2,3,4,5], "twos")
    assert score == 4

    testing_sc = Scorecard()
    score = testing_sc.score_turn([2,2,2,2,2], "twos")
    assert score == 10

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,3,4,5,6], "twos")
    assert score == 0

def test_score_threes():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([3,3,3,4,5], "threes")
    assert score == 9

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,4,5,6], "threes")
    assert score == 0

def test_score_fours():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([4,4,4,4,5], "fours")
    assert score == 16

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,3,5,6], "fours")
    assert score == 0

def test_score_fives():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([5,5,5,5,5], "fives")
    assert score == 25

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,3,4,6], "fives")
    assert score == 0

def test_score_sixes():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([6,6,6,6,6], "sixes")
    assert score == 30

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,3,4,5], "sixes")
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