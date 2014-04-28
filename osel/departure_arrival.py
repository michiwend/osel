from osel.line import Line
#from osel.stop import Stop
import datetime


class DMRequestParser(object):
    def __init__(self):
        pass


class DepartureArrival(object):
    """
    Represents an arrival or a departure
    """
    def __init__(self):
        self._date = None
        self._line = None

class DepartureArrivalList(object):
    """
    Serves as a result for a call to
    get_arrivals or get_departures.
    Contains shit
    """
    def __init__(self):
        self.dep_arr = []

    def get_latest(self):
        pass

    def get_earliest(self):
        pass

    def get_later(self, hours=3):
        """
        returns departures / arrivals from n hours later than
        the last search request
        """
        pass

    def get_earlier(self, hours=3):
        """
        returns departures / arrivals from n hours earlier than
        the last search request
        """
        pass

class Arrival(DepartureArrival):
    @staticmethod
    def get_arrivals(stop, data):
        """
        Get arrivals
        """
        pass

    def __init__(self):
        DepartureArrival.__init__(self)

class Departure(DepartureArrival):
    @staticmethod
    def get_departures(stop, date):
        """
        Get departures
        """
        pass

    def __init__(self):
        DepartureArrival.__init__(self)
