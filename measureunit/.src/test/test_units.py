import logging
# logging.basicConfig(level=logging.INFO, 
#                     format=' %(asctime)s | <%(levelname)s> %(message)s',
#                     datefmt='%d/%m/%Y %H:%M:%S')
# import pytest
from measureunit.units import Length, WeightMass, Temperature

def test_km2m() -> None:
    result = Length.km2m(2)
    logging.info(f'The result of value {result}')
    assert result == 2000
    
def test_t2kg() -> None:
    result = WeightMass.t2kg(2)
    logging.info(f'The result of value {result}')
    assert result == 2000
    
def test_C2F() -> None:
    result = Temperature.C2F(2)
    logging.info(f'The result of value {result}')
    assert result == 35.6
    
if __name__ == '__main__':
    
    try:
        test_km2m()
        test_t2kg()
        test_C2F()
        
    except TypeError as e:
        logging.error(f"Caught an exception due to {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred due to {e}. Please try again!")