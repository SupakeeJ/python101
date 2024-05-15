from pointsystem import point

def test_price_equal100():
    assert point(100) == 1

def test_price_More100():
    assert point(1590) == 15