from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

LOG_FMT = '%(asctime)s (%(filename)s:%(lineno)d:%(process)s) | <%(levelname)s> %(message)s'

logging.basicConfig(level=logging.INFO,
                    format=LOG_FMT,
                    datefmt='%d/%m/%Y %H:%M:%S',
                    handlers=[logging.StreamHandler()])

class InputTypeError(TypeError):
    """Validating inappropriate input type"""
    pass

def validate_input(value, method_name):
    if not isinstance(value, (int, float)):
        raise InputTypeError(f"'{method_name}({value})' must be a numeric type (integer or float)")
    else:
        return True

@dataclass
class Length:
    """Converting the measurement units of Length"""
    
    __slots__ = ['kilometer', 'hectometer', 'decameter', 'meter',
                 'decimeter', 'centimeter', 'milimeter', 'inch']
    
    kilometer:  int | float
    hectometer: int | float
    decameter:  int | float
    meter:      int | float
    decimeter:  int | float
    centimeter: int | float
    milimeter:  int | float
    inch:       int | float
    
    @staticmethod
    def km2m(kilometer: int | float) -> int | float:
        """
        Kilometer (km) to meter (m)
        """
        meter = kilometer * 1000
        validate_input(kilometer, 'km2m')
        return meter
    
    @staticmethod
    def m2km(meter: int | float) -> int | float:
        """
        Meter (m) to kilometer (km)
        """
        kilometer = meter / 1000
        validate_input(meter, 'm2km')
        return kilometer
    
    @staticmethod
    def km2hm(kilometer: int | float) -> int | float:
        """
        Kilometer (km) to hectometer (hm)
        """
        hectometer = kilometer * 10
        validate_input(kilometer, 'km2hm')
        return hectometer
    
    @staticmethod
    def hm2km(hectometer: int | float) -> int | float:
        """
        Hectometer (hm) to kilometer (km)
        """
        kilometer = hectometer / 10
        validate_input(hectometer, 'hm2km')
        return kilometer
    
    @staticmethod
    def km2dam(kilometer: int | float) -> int | float:
        """
        Kilometer (km) to decameter (dam)
        """
        decameter = kilometer * 100
        validate_input(kilometer, 'km2dam')
        return decameter
    
    @staticmethod
    def dam2km(decameter: int | float) -> int | float:
        """
        Decameter (dam) to kilometer (km)
        """
        kilometer = decameter / 100
        validate_input(decameter, 'dam2km')
        return kilometer
    
    @staticmethod
    def hm2m(hectometer: int | float) -> int | float:
        """
        Hectometer (hm) to meter (m)
        """
        meter = hectometer * 100
        validate_input(hectometer, 'hm2m')
        return meter
    
    @staticmethod
    def m2hm(meter: int | float) -> int | float:
        """
        Meter (m) to hectometer (hm)
        """
        hectometer = meter / 100
        validate_input(meter, 'm2hm')
        return hectometer
    
    @staticmethod
    def dam2m(decameter: int | float) -> int | float:
        """
        Dacameter (dam) to meter (m)
        """
        meter = decameter * 10
        validate_input(decameter, 'dam2m')
        return meter
    
    @staticmethod
    def m2dam(meter: int | float) -> int | float:
        """
        Meter (m) to decameter (dam)
        """
        decameter = meter / 10
        validate_input(meter, 'm2dam')
        return decameter
    
    @staticmethod
    def m2dm(meter: int | float) -> int | float:
        """
        Meter (m) to decimeter (dm)
        """
        decimeter = meter * 10
        validate_input(meter, 'm2dm')
        return decimeter
    
    @staticmethod
    def dm2m(decimeter: int | float) -> int | float:
        """
        Decimeter (dm) to meter (m)
        """
        meter = decimeter / 10
        validate_input(decimeter, 'dm2m')
        return meter
    
    @staticmethod
    def m2cm(meter: int | float) -> int | float:
        """
        Meter (m) to centimeter (cm)
        """
        centimeter = meter * 10
        validate_input(meter, 'm2cm')
        return centimeter
    
    @staticmethod
    def cm2m(centimeter: int | float) -> int | float:
        """
        Centimeter (cm) to meter (m)
        """
        meter = centimeter / 10
        validate_input(centimeter, 'cm2m')
        return meter
    
    @staticmethod
    def m2mm(meter: int | float) -> int | float:
        """
        Meter (m) to milimeter (mm)
        """
        milimeter = meter * 1000
        validate_input(meter, 'm2mm')
        return milimeter
    
    @staticmethod
    def mm2m(milimeter: int | float) -> int | float:
        """
        Milimeter (mm) to meter (m)
        """
        meter = milimeter / 100
        validate_input(milimeter, 'mm2m')
        return meter
    
    @staticmethod
    def in2cm(inch: int | float) -> int | float:
        """
        Inch (in) to centimeter (cm)
        """
        centimeter = inch * 2.54
        validate_input(inch, 'in2cm')
        return centimeter
    
    @staticmethod
    def cm2in(centimeter: int | float) -> int | float:
        """
        Centimeter (cm) to inch (in)
        """
        inch = centimeter * 0.393701
        validate_input(centimeter, 'cm2in')
        return inch
    
@dataclass
class WeightMass:
    """Converting the measurement units of Weight and Mass"""
    
    __slots__ = ['tonne', 'kilogram', 'hectogram', 'dekagram',
                 'gram', 'pound', 'ounce', 'u']
    
    tonne:      int | float
    kilogram:   int | float
    hectogram:  int | float
    dekagram:   int | float
    gram:       int | float
    pound:      int | float
    ounce:      int | float
    u:          int | float
    
    @staticmethod
    def t2kg(tonne: int | float) -> int | float:
        """
        Ton (t) to kilogram (kg)
        """
        kilogram = tonne * 1000
        validate_input(tonne, 't2kg')
        return kilogram
    
    @staticmethod
    def kg2t(kilogram: int | float) -> int | float:
        """
        Kilogram (kg) to ton (t)
        """
        tonne = kilogram / 1000
        validate_input(kilogram, 'kg2t')
        return tonne
    
    @staticmethod
    def kg2g(kilogram: int | float) -> int | float:
        """
        Kilogram (kg) to gram (g)
        """
        gram = kilogram * 1000
        validate_input(kilogram, 'kg2g')
        return gram
    
    @staticmethod
    def g2kg(gram: int | float) -> int | float:
        """
        Gram (g) to kilogram (kg)
        """
        kilogram = gram / 1000
        validate_input(gram, 'g2kg')
        return kilogram
    
    @staticmethod
    def kg2hg(kilogram: int | float) -> int | float:
        """
        Kilogram (kg) to hectogram (hg)
        """
        hectogram = kilogram * 10
        validate_input(kilogram, 'kg2hg')
        return hectogram
    
    @staticmethod
    def hg2kg(hectogram: int | float) -> int | float:
        """
        Hectogram (hg) to kilogram (kg)
        """
        kilogram = hectogram / 10
        validate_input(hectogram, 'hg2kg')
        return kilogram
    
    @staticmethod
    def kg2dag(kilogram: int | float) -> int | float:
        """
        Kilogram (kg) to dekagram (dag)
        """
        dekagram = kilogram * 100
        validate_input(kilogram, 'kg2dag')
        return dekagram
    
    @staticmethod
    def dag2kg(dekagram: int | float) -> int | float:
        """
        Dekagram (dag) to kilogram (kg)
        """
        kilogram = dekagram / 100
        validate_input(dekagram, 'dag2kg')
        return kilogram
    
    @staticmethod
    def hg2g(hectogram: int | float) -> int | float:
        """
        Hectogram (hg) to gram (g)
        """
        gram = hectogram * 100
        validate_input(hectogram, 'hg2g')
        return gram
    
    @staticmethod
    def g2hg(gram: int | float) -> int | float:
        """
        Gram (g) to hectogram (hg)
        """
        hectogram = gram / 100
        validate_input(gram, 'g2hg')
        return hectogram
    
    @staticmethod
    def dag2g(dekagram: int | float) -> int | float:
        """
        Dekagram (dag) to gram (g)
        """
        gram = dekagram * 10
        validate_input(dekagram, 'dag2g')
        return gram
    
    @staticmethod
    def g2dag(gram: int | float) -> int | float:
        """
        Gram (g) to dekagram (dag)
        """
        dekagram = gram / 10
        validate_input(gram, 'g2dag')
        return dekagram
    
    @staticmethod
    def lb2oz(pound: int | float) -> int | float:
        """
        Pound (lb) to ounce (oz)
        """
        ounce = pound * 16
        validate_input(pound, 'lb2oz')
        return ounce
    
    @staticmethod
    def oz2lb(ounce: int | float) -> int | float:
        """
        Ounce (oz) to pound (lb)
        """
        pound = ounce * 0.0625
        validate_input(ounce, 'oz2lb')
        return pound
    
    @staticmethod
    def u2kg(u: int | float) -> int | float:
        """
        Atomic mass unit (u) to kilogram (kg)
        """
        kilogram = u * 1.6605402E-27
        validate_input(u, 'u2kg')
        return kilogram
    
    @staticmethod
    def kg2u(kilogram: int | float) -> int | float:
        """
        Kilogram (kg) to atomic mass unit (u)
        """
        u = kilogram / 1.6605402E-27
        validate_input(kilogram, 'kg2u')
        return u

@dataclass   
class Temperature:
    """Converting the measurement units of Temperature"""
    
    __slots__ = ['Celsius', 'Fahrenheit', 'Kelvin']
    Celsius:    int | float
    Fahrenheit: int | float
    Kelvin:     int | float
    
    @staticmethod
    def C2F(celsius: int | float) -> int | float:
        """
        Celsius (°C) to Fahrenheit (°F)
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    @staticmethod
    def F2C(fahrenheit: int | float) -> int | float:
        """
        Fahrenheit (°F) to Celsius (°C)
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
    @staticmethod
    def C2K(celsius: int | float) -> int | float:
        """
        Celsius (°C) to Kelvin (K)
        """
        kelvin = celsius + 273.15
        return kelvin
    
    @staticmethod
    def K2C(kelvin: int | float) -> int | float:
        """
        Kelvin (K) to Celsius (°C)
        """
        celsius = kelvin - 273.15
        return celsius
    
    @staticmethod
    def F2K(fahrenheit: int | float) -> int | float:
        """
        Fahrenheit (°F) to Kelvin (K)
        """
        kelvin = ((fahrenheit - 32) * 5/9) + 273.15
        return kelvin
    
    @staticmethod
    def K2F(kelvin: int | float) -> int | float:
        """
        Kelvin (K) to Fahrenheit (°F)
        """
        fahrenheit = ((kelvin - 273.15) * 9/5) + 32
        return fahrenheit
    

def main() -> None:
    try:
        length = Length.km2m('')
        logging.info(f'The result of the length value: {length}')
        
        mass = WeightMass.kg2g(4)
        logging.info(f'The result of the mass value: {mass}')
        
        temp = Temperature.C2F(4)
        logging.info(f'The result of temp value: {temp}')
    
    except (ValueError, TypeError) as e:
        logging.exception(f"An error occurred due to {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred due to {e}. Please try again!")
            
if __name__ == '__main__':
    main()