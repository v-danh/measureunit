from measureunit.units import Length
# import measureunit as msu
import logging

# msu.__version__

v = Length.km2m(1)
logging.info(f"The conversion value of 'km2m(1)' is {v}")