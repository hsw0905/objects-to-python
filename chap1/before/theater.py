from chap1.before.audience import Audience
from chap1.before.ticket_seller import TicketSeller


class Theater:
    def __init__(self, ticket_seller: TicketSeller) -> None:
        self._ticket_seller = ticket_seller

    def enter(self, audience: Audience) -> None:
        if audience.bag.has_invitation():
            ticket = self._ticket_seller.ticket_office.get_ticket()
            audience.bag.ticket = ticket
        else:
            ticket = self._ticket_seller.ticket_office.get_ticket()
            audience.bag.minus_amount(ticket.fee)
            self._ticket_seller.ticket_office.plus_amount(ticket.fee)
            audience.bag.ticket = ticket
