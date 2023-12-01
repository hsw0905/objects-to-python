from chap1.after.audience import Audience
from chap1.after.ticket_office import TicketOffice


class TicketSeller:
    def __init__(self, ticket_office: TicketOffice) -> None:
        self._ticket_office = ticket_office

    @property
    def ticket_office(self) -> TicketOffice:
        return self._ticket_office

    def sell_to(self, audience: Audience) -> None:
        self._ticket_office.sell_ticket_to(audience)

