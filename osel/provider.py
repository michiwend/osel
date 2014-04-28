class EFAProvider(object):
    '''
    represents a public transport provider
    '''
    def __init__(self, region, network, network_name, api_base):
        self._region        = region
        self._network       = network
        self._network_name  = network_name
        self._api_base      = api_base

    def get_region(self):
        return self._region

    def get_api_base(self):
        return self._api_base

    def get_network(self):
        return self._network

    def get_network_name(self):
        return self._network_name




class AVV(EFAProvider):
    def __init__(self):
        super().__init__(
                region       = 'Augsburg',
                network      = 'AVV',
                network_name = 'Augsburger Verkehrsverbund GmbH',
                api_base     = 'http://efa.avv-augsburg.de/avv/'
                )


class MVV(EFAProvider):
    def __init__(self):
        super().__init__(
                region       = 'München'
                network      = 'MVV'
                network_name = 'Münchner Verkehrs- und Tarifverbund GmbH'
                api_base     = 'http://efa.mvv-muenchen.de/mobile/'
                )
