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

def test_score_twos():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([2,2,1,3,4], "twos")
    assert score == 4

    testing_sc = Scorecard()
    score = testing_sc.score_turn([2,2,2,2,2], "twos")
    assert score == 10

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,3,4,5,6], "twos")
    assert score == 0

def test_score_threes():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([3,3,3,1,2], "threes")
    assert score == 9

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,4,5,6], "threes")
    assert score == 0

def test_score_fours():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([4,4,1,2,3], "fours")
    assert score == 8

    testing_sc = Scorecard()
    score = testing_sc.score_turn([4,4,4,4,1], "fours")
    assert score == 16

def test_score_fives():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([5,5,5,1,2], "fives")
    assert score == 15

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,3,4,6], "fives")
    assert score == 0

def test_score_sixes():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([6,6,1,2,3], "sixes")
    assert score == 12

    testing_sc = Scorecard()
    score = testing_sc.score_turn([6,6,6,6,6], "sixes")
    assert score == 30

    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,3,4,5], "sixes")
    assert score == 0

def test_mixed_categories():
    testing_sc = Scorecard()
    
    # Test multiple different categories
    score1 = testing_sc.score_turn([1,1,2,3,4], "ones")
    assert score1 == 2
    
    score2 = testing_sc.score_turn([2,2,2,1,3], "twos")
    assert score2 == 6
    
    score3 = testing_sc.score_turn([3,3,3,3,1], "threes")
    assert score3 == 12

def test_invalid_category():
    testing_sc = Scorecard()
    score = testing_sc.score_turn([1,2,3,4,5], "invalid")
    assert score == 0

def test_multiple_category_reuse():
    testing_sc = Scorecard()
    
    # Use ones
    testing_sc.score_turn([1,1,2,3,4], "ones")
    
    # Use twos  
    testing_sc.score_turn([2,2,2,1,3], "twos")
    
    # Try to reuse ones - should raise error
    with pytest.raises(ValueError, match="Error: ones has already been scored!"):
        testing_sc.score_turn([1,1,1,1,1], "ones")
    
    # Try to reuse twos - should raise error
    with pytest.raises(ValueError, match="Error: twos has already been scored!"):
        testing_sc.score_turn([2,2,2,2,2], "twos")