import logging
logging.basicConfig(level=logging.INFO, 
                    format=' %(asctime)s | <%(levelname)s> | %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

from measureunit.units import Length, WeightMass, Temperature

l1 = Length.km2m()
print(l1)

w1 = WeightMass.t2kg(2)
print(w1)

t1 = Temperature.C2F(2)
print(t1)