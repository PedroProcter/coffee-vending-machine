



class SugarStrips:
    """"""

    amount_of_strips: int = 0

    def __init__(self, amount_of_strips: int = 0):
        self.amount_of_strips = amount_of_strips

    def get_sugar_strip(self):
        self.amount_of_strips -= 1
        return 1

    def has_sugar_strip(self):
        
        return (self.amount_of_strips <= 0)

    def length(self):
        return self.amount_of_strips
