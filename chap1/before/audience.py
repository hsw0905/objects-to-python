from chap1.before.bag import Bag


class Audience:
    def __init__(self, bag: Bag) -> None:
        self._bag = bag

    @property
    def bag(self) -> Bag:
        return self._bag
