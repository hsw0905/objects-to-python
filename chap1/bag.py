from chap1.invitation import Invitation
from chap1.ticket import Ticket


class Bag:
    def __init__(self, amount: int, invitation: Invitation = None, ticket: Ticket = None) -> None:
        self._amount = amount
        self._invitation = invitation
        self._ticket = ticket

    def has_invitation(self) -> bool:
        return self._invitation is not None

    def has_ticket(self) -> bool:
        return self._ticket is not None

    def minus_amount(self, amount: int) -> None:
        self._amount -= amount

    def plus_amount(self, amount: int) -> None:
        self._amount += amount

    @property
    def ticket(self) -> Ticket:
        return self._ticket

    @ticket.setter
    def ticket(self, ticket: Ticket) -> None:
        self._ticket = ticket
