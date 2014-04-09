import lxml
import urllib

from tramsalat.line import Line

class Movements(object):
    """
    Represents an arrival or a reparture
    """
    def __init__(self):
        self._date = None
        self._line = None

class MovementList(object):
    """
    Serves ass a result for a call to
    get_arrivals or get_departures.
    Contains shit
    """
    def __init__(self):
        self.movements = []
    
    def get_latest_movement(self):
        pass

    def get_earliest_movement(self):
        pass

    def get_later(self, hours=3):
        """
        returns movements until n hours later than
        the last search request
        """
        pass
    
    def get_earlier(self, hours=3):
        """
        returns movements from n hours earlier than the
        last search request
        """
        pass

class Arrival(Movements):
    @staticmethod
    def get_arrivals(stop, data):
        """
        Get arrivals
        """
        pass

    def __init__(self):
        Movements.__init__(self)

class Departure(object):
    @staticmethod
    def get_departures(stop, date):
        """
        Get departures
        """
        pass

    def __init__(self):
        Movements.__init__(self)
