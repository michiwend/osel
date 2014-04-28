#!/usr/bin/env python

from osel.provider import *
from osel.stop import Stop


my_provider = AVV()
results = Stop.find_stops(my_provider, 'wer', 20)

if len(results):
    for stop in results:
        print(stop.get_name() + ' : ' + stop.get_id() + ' : ' + stop.get_type())
else:
    print('empty response')
