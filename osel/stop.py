from osel.departure_arrival import Arrival, Departure

import lxml
import urllib

class StopNotInCacheException(Exception): pass

class StopFinderParser(object):
    pass

class Stop(object):
    STOPCACHE = {}

    @classmethod
    def cache_stop(cls, stop):
        """
        Adds a stop to the volatile cache
        """
        cls.STOPCACHE[stop.get_id()] = stop

    @staticmethod
    def find_stops(search_string):
        """
        Causes the library to search for a specific stop name
        returns a list of Stops that were present in the response
        from the EFA-server
        """
        pass # get shit from server -> urllib
        # uebergebe shit an parser
        # parser returnt adaequate objekte
    
    @classmethod
    def get_stop(cls, stop_id):
        """
        Returns a stop that matches the given id
        """
        if not cls.STOPCACHE.has_key(stop_id):
            raise StopNotInCacheException()
        return cls.STOPCACHE[stop_id]

    def __init__(self):
        """
        trivial
        """
        self._name = None
        self._type = None
        self._id = None
        self._lon = None
        self._lat = None
        self._object = None
        self._posttown = None

    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
    def set_name(self, name):
        self._name = name

    def set_id(self, stop_id):
        self._id = stop_id

    def get_departures(self, date):
        Departure.get_departures(self, date)

    def get_arrivals(self, date):
        Arrival.get_arrivals(self, date)
