



class Cup:
    """"""

    content: bool = False

    def set_content(self, content: bool) -> None:
        self.content = content

    def has_content(self) -> bool:
        return self.content

class PileOfCups:
    """"""

    pile: list[Cup] = []

    def __init__(self, amount_of_cups: int = 0):
        self.pile = [Cup() for cup in range(amount_of_cups)]

    def get_cup(self) -> Cup:
        return self.pile.pop()

    def has_cups(self) -> bool:
        return False if len(self.pile) <= 0 else True

    def length(self) -> int:
        return len(self.pile)