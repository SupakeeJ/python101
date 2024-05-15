from pointsystem import point

def test_price_less100():
    assert point(95.96) == 0
    assert point(0) == 1