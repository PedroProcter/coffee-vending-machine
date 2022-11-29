from coffee_machine import CoffeeMachine



def test_return_not_coffee_grains_left():
    coffee_machine = CoffeeMachine(0)

    assert not coffee_machine.has_coffe_grains()

def test_return_less_coffee_grains_left():
    coffee_machine = CoffeeMachine(5)
    coffee_machine.get_coffee()

    assert (coffee_machine.length() == 4)