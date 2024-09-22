from zlipy.domain.events.events import Event
from zlipy.domain.events.interfaces import IEvent


class EventFactory:
    @staticmethod
    def create(json_data: dict) -> IEvent:
        name = json_data.get("event")

        if name is None:
            raise ValueError("Event name is required")

        del json_data["event"]

        return Event(name, json_data)
