class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""

class LoginEvent(Event):
    """A event representing a user that has just entered the system."""

class LogoutEvent(Event):
    """An event representing a user that has just left the system."""

class SystemMonitor:
    """Identify events that occurred in the system."""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if (self.event_data["before"]["session"] == 0 and self.event_data["after"]["session"] == 1):
            return LoginEvent(self.event_data)

        elif (self.event_data["before"]["session"] == 1 and self.event_data["after"]["session"] == 0):
            return LogoutEvent(self.event_data)
        return UnknownEvent(self.event_data)
