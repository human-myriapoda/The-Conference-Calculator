# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import os,sys
sys.path.insert(0, os.getcwd())
import carbon, carbon_bus, carbon_car, carbon_flight

a = 5
vec = np.array([5, 5])

list_a = [1, 2, 3]
list_b = [4, 5, 6]

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print(list_a + list_b)
print(array_a + array_b)

busco2 = carbon_bus.CarbonBus()
co2 = busco2.calculate_co2(50.,'hauling-ass')

flight1 = carbon_flight.CarbonFlight()
co2_flight = flight1.calculate_co2_from_airports(iata_orig = 'LHR', iata_dest = 'SOF', pax_class = 'business-class', trip_type = 'shit')