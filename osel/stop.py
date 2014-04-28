from osel.departure_arrival import Arrival, Departure
from osel.provider import EFAProvider

from lxml import etree
from urllib.request import urlopen
from urllib.parse import urlencode


class StopNotInCacheException(Exception): pass


class StopFinderParser(object):
    def __init__(self, efa_provider):
        self._provider = efa_provider


class Stop(object):
    STOPCACHE = {}

    @classmethod
    def cache_stop(cls, stop):
        """
        Adds a stop to the volatile cache
        """
        cls.STOPCACHE[stop.get_id()] = stop

    @staticmethod
    def find_stops(provider, search_string, max_results):
        """
        Causes the library to search for a specific stop name. Returns a list of
        stops that were present in the response from the EFA-server.
        """
        sf_params = {
            'language'              : 'de',
            'outputFormat'          : 'XML',
            'useLocalityMainStop'   : 'true',
            'locationServerActive'  : '1',
            'type_sf'               : 'any',
            'anyMaxSizeHitList'     : max_results,
            'name_sf'               : search_string
        }

        stop_list = []

        try:
            response = urlopen(
                            provider.get_api_base() + provider.get_sf_endpoint()
                            + '?' + urlencode(sf_params)
                        )
            tree = etree.parse(response)
            sf_root = tree.find('itdStopFinderRequest')
            #print(etree.tostring(sf_root, pretty_print=True))

            if etree.iselement(sf_root): # ToDo: check if odvNameElem is a child of sf_root
                for xml_stop in sf_root.iter('odvNameElem'):
                    stop_list.append(Stop(
                                        xml_stop.text,
                                        xml_stop.attrib['id'],
                                        xml_stop.attrib['anyType'],
                                        xml_stop.attrib['x'],
                                        xml_stop.attrib['y'],
                                        xml_stop.attrib['locality'],
                                        xml_stop.attrib['objectName'],
                                        xml_stop.attrib['buildingName'],
                                        xml_stop.attrib['buildingNumber'],
                                        xml_stop.attrib['postCode'],
                                        xml_stop.attrib['streetName'],
                                        xml_stop.attrib['posttown'],
                                        xml_stop.attrib['value']
                                    ))
            else:
                raise Exception('No valid stop finder response')

        except IOError as e:
            print(e)

        except KeyError as e:
            print('seems like an empty stop finder response: ' + str(e))

        except etree.XMLSyntaxError as e:
            print(e)

        except Exception as e:
            print(e)

        return stop_list


    @classmethod
    def get_stop(cls, stop_id):
        """
        Returns a stop that matches the given id
        """
        if not cls.STOPCACHE.has_key(stop_id):
            raise StopNotInCacheException()
        return cls.STOPCACHE[stop_id]

    def __init__(self, name, stop_id, stop_type, lat=0, lon=0, locality='',
                    object_name='', building_name='', building_number='',
                    post_code='', street_name='', posttown='', value=''):
        """
        trivials
        """
        self._name = name
        #self._listIndex="0"
        #self._selected="0"
        #self._matchQuality="885"
        self._lat = lat
        self._lon = lon
        #self._mapName="NAV4"
        self._id = stop_id
        #self._omc="9772200"
        #self._placeID="10"
        self._type = stop_type
        #self._anyTypeSort="1"
        self._locality = locality
        self._objectName = object_name
        self._buildingName = building_name
        self._buildingNumber = building_number
        self._postCode = post_code
        self._streetName = street_name
        #self._nameKey=
        self._posttown = posttown
        self._value = value


    def set_name(self, name):
        self._name = name

    def set_id(self, stop_id):
        self._id = stop_id

    def get_departures(self, date):
        Departure.get_departures(self, date)

    def get_arrivals(self, date):
        Arrival.get_arrivals(self, date)

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type
