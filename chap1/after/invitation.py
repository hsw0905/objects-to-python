from datetime import datetime


class Invitation:
    def __init__(self, when: datetime) -> None:
        self._when = when
