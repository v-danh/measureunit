from measureunit.units import Length, WeightMass, Temperature
import measureunit as msu
import logging

# print(msu.__version__)

try:
    length = Length.km2m(2)
    logging.info(f'The result of the length value: {length}')
    
    mass = WeightMass.kg2g(4)
    logging.info(f'The result of the mass value: {mass}')
    
    temp = Temperature.C2F(4)
    logging.info(f'The result of temp value: {temp}')
    
except (ValueError, TypeError) as e:
    logging.exception(f"An error occurred due to {e}")
except Exception as e:
    logging.exception(f"An unexpected error occurred due to {e}. Please try again!")