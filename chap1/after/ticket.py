class Ticket:
    def __init__(self, fee: int) -> None:
        self._fee = fee

    @property
    def fee(self) -> int:
        return self._fee
