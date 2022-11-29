from sugar_strips import SugarStrips



def test_return_not_sugar_strips_left():
    sugar_strips = SugarStrips(0)

    assert not sugar_strips.has_sugar_strip()

def test_return_less_sugar_trips_left():
    sugar_strips = SugarStrips(5)
    sugar_strips.get_sugar_strip()
    
    assert (sugar_strips.length() == 4)