from scorecard import Scorecard

def test_full_house():
    # Test valid full houses
    test_sc = Scorecard()
    score = test_sc.score_full_house([1,1,1,2,2])  # Three 1s, two 2s
    assert score == 25
    
    test_sc = Scorecard()
    score = test_sc.score_full_house([3,3,5,5,5])  # Two 3s, three 5s
    assert score == 25
    
    # Test invalid full houses
    test_sc = Scorecard()
    score = test_sc.score_full_house([1,2,3,4,5])  # Straight, not full house
    assert score == 0
    
    test_sc = Scorecard()
    score = test_sc.score_full_house([1,1,1,1,2])  # Four of a kind, not full house
    assert score == 0
    
    test_sc = Scorecard()
    score = test_sc.score_full_house([1,2,3,4,6])  # No pairs
    assert score == 0

def test_full_house_already_used():
    test_sc = Scorecard()
    test_sc.used_full_house = True  # Mark as already used
    
    score = test_sc.score_full_house([1,1,1,2,2])
    assert score == 0  # Should return 0 when already used

def test_large_straight():
    # Test valid large straights
    test_sc = Scorecard()
    score = test_sc.score_large_straight([1,2,3,4,5])
    assert score == 40
    
    test_sc = Scorecard()
    score = test_sc.score_large_straight([2,3,4,5,6])
    assert score == 40
    
    # Test with different order (should still work)
    test_sc = Scorecard()
    score = test_sc.score_large_straight([5,4,3,2,1])
    assert score == 40
    
    # Test invalid straights
    test_sc = Scorecard()
    score = test_sc.score_large_straight([1,2,3,4,6])  # Missing 5
    assert score == 0
    
    test_sc = Scorecard()
    score = test_sc.score_large_straight([1,1,2,3,4])  # Has duplicate
    assert score == 0

def test_large_straight_already_used():
    test_sc = Scorecard()
    test_sc.used_large_straight = True
    
    score = test_sc.score_large_straight([1,2,3,4,5])
    assert score == 0

def test_small_straight():
    # Test valid small straights
    test_sc = Scorecard()
    score = test_sc.score_small_straight([1,2,3,4,6])  # Contains 1,2,3,4
    assert score == 30
    
    test_sc = Scorecard()
    score = test_sc.score_small_straight([2,3,4,5,1])  # Contains 2,3,4,5
    assert score == 30
    
    test_sc = Scorecard()
    score = test_sc.score_small_straight([3,4,5,6,2])  # Contains 3,4,5,6
    assert score == 30
    
    # Test with duplicates (should still work)
    test_sc = Scorecard()
    score = test_sc.score_small_straight([1,2,2,3,4])  # Contains 1,2,3,4 with extra 2
    assert score == 30
    
    # Test invalid small straights
    test_sc = Scorecard()
    score = test_sc.score_small_straight([1,1,1,1,1])  # All same
    assert score == 0
    
    test_sc = Scorecard()
    score = test_sc.score_small_straight([1,3,5,6,2])  # No consecutive run of 4
    assert score == 0

def test_small_straight_already_used():
    test_sc = Scorecard()
    test_sc.used_small_straight = True
    
    score = test_sc.score_small_straight([1,2,3,4,5])
    assert score == 0