class Event:
    ...
    def meets_condition(self, event_data: dict) -> bool:
        return False

class LogoutEvent(Event):
    ...
    def meets_condition(self, event_data: dict, override: bool) -> bool:
        if override:
            return True
        return bool(event_data)
