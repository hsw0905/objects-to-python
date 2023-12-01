from chap1.after.audience import Audience
from chap1.after.ticket import Ticket


class TicketOffice:
    def __init__(self, amount: int, tickets: list[Ticket]) -> None:
        self._amount = amount
        self._tickets = tickets

    def sell_ticket_to(self, audience: Audience) -> None:
        self._plus_amount(audience.buy(self._get_ticket()))

    def _get_ticket(self) -> Ticket:
        return self._tickets.pop(0)

    def _minus_amount(self, amount: int) -> None:
        self._amount -= amount

    def _plus_amount(self, amount: int) -> None:
        self._amount += amount
