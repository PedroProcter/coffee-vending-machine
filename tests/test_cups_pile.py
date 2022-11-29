from cups_pile import PileOfCups, Cup



def test_return_not_cups_left():
    pile_of_cups = PileOfCups(0)

    assert not pile_of_cups.has_cups()

def test_return_small_cup():
    pile_of_small_cups = PileOfCups(5)

    assert (type(pile_of_small_cups.get_cup()) == Cup)

def test_return_medium_cup():
    pile_of_medium_cups = PileOfCups(5)
    
    assert (type(pile_of_medium_cups.get_cup()) == Cup)

def test_return_big_cup():
    pile_of_big_cups = PileOfCups(5)

    assert (type(pile_of_big_cups.get_cup()) == Cup)

def test_return_less_cups_left():
    pile_of_cups = PileOfCups(5)
    pile_of_cups.get_cup()

    assert (pile_of_cups.length() == 4)