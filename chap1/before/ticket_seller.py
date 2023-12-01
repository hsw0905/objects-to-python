from chap1.before.ticket_office import TicketOffice


class TicketSeller:
    def __init__(self, ticket_office: TicketOffice) -> None:
        self._ticket_office = ticket_office

    @property
    def ticket_office(self) -> TicketOffice:
        return self._ticket_office
