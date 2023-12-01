from chap1.after.bag import Bag
from chap1.after.ticket import Ticket


class Audience:
    def __init__(self, bag: Bag) -> None:
        self._bag = bag

    @property
    def bag(self) -> Bag:
        return self._bag

    def buy(self, ticket: Ticket) -> int:
        return self._bag.hold(ticket)

