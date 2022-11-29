



class CoffeeMachine:
    """"""

    amount_of_coffe_grains: int = 0

    def __init__(self, amount_of_coffe_grains: int = 0):
        self.amount_of_coffe_grains = amount_of_coffe_grains

    def get_coffee(self):
        self.amount_of_coffe_grains -= 1

        return 1

    def has_coffe_grains(self):
        return False if self.amount_of_coffe_grains <= 0 else True

    def length(self):
        return self.amount_of_coffe_grains
