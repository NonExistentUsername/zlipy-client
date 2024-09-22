from zlipy.domain.events.interfaces import IEvent


class Event(IEvent):
    def __init__(self, name: str, data: dict):
        self._name = name
        self._data = data

    @property
    def name(self) -> str:
        return self._name

    @property
    def data(self) -> dict:
        return self._data
