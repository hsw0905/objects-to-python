from chap1.after.audience import Audience
from chap1.after.ticket_seller import TicketSeller


class Theater:
    def __init__(self, ticket_seller: TicketSeller) -> None:
        self._ticket_seller = ticket_seller

    def enter(self, audience: Audience) -> None:
        self._ticket_seller.sell_to(audience)
