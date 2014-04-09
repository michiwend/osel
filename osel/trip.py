import urllib
import lxml

from osel.line import Line
from osel.stop import Stop

class TripRequestParser(object):
    """
    parses the response of the triprequest via lxml
    """
    pass


class TripList(object):
    """
    Servers as a response for a call to
    Trip.get_trips()
    contains all trips resulting from the request
    """
    def __init__(self):
        self._trips = []
        self._session_id = 0
    
    def get_later(self):
        """
        Get later trips
        """
        pass

    def get_earlier(self):
        """
        get earlier trips
        """
        pass

class Trip(object):
    """
    Contains a complete trip between to stops
    this contains one or more partial trips
    """
    @staticmethod
    def get_trips(start_stop, end_stop, date):
        """
        Gets a bunch of trips from teh internetz
        """
        pass
    
    def __init__(self):
        self._parttrips = []
    
class PartialTrip(object):
    """
    Represents a Partial trip from one stop to
    another as a list of several stops. 8===D~~~
    """
    def __init__(self):
        self._stops = []
        self._line = None
        self._date = None
        self._start_stop = None
        self._end_stop = None

    def get_start_stop(self):
        return self._stops[0]

    def get_end_stop(self):
        return self._stops[len(self._stops)-1]
