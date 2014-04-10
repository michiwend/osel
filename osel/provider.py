

class Provider(object):
    '''
    represents a public transport provider
    '''
    def __init__(self, region, network, network_name, api_base):
        self._region        = region
        self._network       = network
        self._network_name  = network_name
        self._api_base      = api_base

    def get_region():
        return self._region
    
    def get_api_base():
        return self._api_base

    def get_network():
        return self._network

    def get_network_name():
        return self._network_name



class AVV(Provider):
    def __init__(self):
        super().__init__(
                region       = 'Augsburg',
                network      = 'AVV',
                network_name = 'Augsburger Verkehrsverbund GmbH',
                api_base     = 'http://efa.avv-augsburg.de/avv/'
                )
    return


class MVV(Provider):
    def __init__(self):
        super().__init__(
                region       = 'München'
                network      = 'MVV'
                network_name = 'Münchner Verkehrs- und Tarifverbund GmbH'
                api_base     = 'http://efa.mvv-muenchen.de/mobile/'
                )

