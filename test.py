import numpy as np
import os,sys

print(os.getcwd())
#sys.path.insert(0, os.getcwd())
import carbon, carbon_bus, carbon_car, carbon_flight

busco2 = carbon_bus.CarbonBus()
co2_bus = busco2.calculate_co2(50,'hauling-ass')
print(co2_bus)

flight1 = carbon_flight.CarbonFlight()
co2_flight = flight1.calculate_co2_from_airports(iata_orig = 'LHR', iata_dest = 'SOF', pax_class = 'business-class', trip_type = 'shit')
print(co2_flight)

carco2 = carbon_car.CarbonCar()
co2_car = carco2.calculate_co2(50,fuel_type='petrol',pax_in_car = 1,trip_type = 'weed')
print(co2_car)
