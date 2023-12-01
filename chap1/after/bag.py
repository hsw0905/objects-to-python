from chap1.after.invitation import Invitation
from chap1.after.ticket import Ticket


class Bag:
    def __init__(self, amount: int, invitation: Invitation = None, ticket: Ticket = None) -> None:
        self._amount = amount
        self._invitation = invitation
        self._ticket = ticket

    @property
    def ticket(self) -> Ticket:
        return self._ticket

    @ticket.setter
    def ticket(self, ticket: Ticket) -> None:
        self._ticket = ticket

    def hold(self, ticket: Ticket) -> int:
        if self._has_invitation():
            self._ticket = ticket
            return 0
        else:
            self._ticket = ticket
            self._minus_amount(ticket.fee)
            return ticket.fee

    def _has_invitation(self) -> bool:
        return self._invitation is not None

    def _has_ticket(self) -> bool:
        return self._ticket is not None

    def _minus_amount(self, amount: int) -> None:
        self._amount -= amount

    def _plus_amount(self, amount: int) -> None:
        self._amount += amount
