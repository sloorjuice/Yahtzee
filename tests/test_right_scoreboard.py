from scorecard import Scorecard

def test_full_house():
    test_sc = Scorecard()
    score = test_sc.score_full_house([1,2,3,4,5])
    assert score == 0
    assert test_sc.score == 0

    test_sc = Scorecard()
    score = test_sc.score_full_house([1,2,2,1,1])
    assert score == 25
    assert test_sc.score == 25

    test_sc = Scorecard()
    score = test_sc.score_full_house([1,1,2,2,1])
    assert score == 25
    assert test_sc.score == 25

    test_sc = Scorecard()
    score = test_sc.score_full_house([1,2,3,4,5])
    assert score == 0
    assert test_sc.score == 0

def test_score_after_full_house():
    test_sc = Scorecard()
    test_sc.score_full_house = 0

    score = test_sc.score_full_house([1,1,2,2,2])

    assert score == "Full house already used"

def test_large_straight():
    test_sc = Scorecard()
    round_score = test_sc.score_large_straight([1,2,3,4,5])
    assert round_score == 40
    assert test_sc.score == 40

    test_sc = Scorecard()
    round_score = test_sc.score_large_straight([6,3,2,5,4])
    assert round_score == 40
    assert test_sc.score == 40

    test_sc = Scorecard()
    round_score = test_sc.score_large_straight([2,2,2,1,1])
    assert round_score == 0
    assert test_sc.score == 0

    test_sc = Scorecard()
    test_sc.score = 30
    round_score = test_sc.score_large_straight([5,4,3,2,1])
    assert round_score == 40
    assert test_sc.score == 70