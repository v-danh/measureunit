import logging
logging.basicConfig(level=logging.INFO, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')


class Length:
    """
        Converting the measurement units of Length
    """
    kilometer: float
    hectometer: float
    decameter: float
    meter: float
    decimeter: float
    centimeter: float
    milimeter: float
    inch: float
    
    def km2m(kilometer: float):
        """
            Kilometer (km) to meter (m)
        """
        if isinstance(kilometer, (int, float)):
            meter = kilometer * 1000
            logging.info(meter)
        else:
            raise ValueError("The value must be an integer. Please try again!")

    def m2km(meter: float):
        """
            Meter (m) to kilometer (km)
        """
        if isinstance(meter, (int, float)):
            kilometer = meter / 1000
            logging.info(kilometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')

    def km2hm(kilometer: float):
        """
            Kilometer (km) to hectometer (hm)
        """
        if isinstance(kilometer, (int, float)):
            hectometer = kilometer * 10
            logging.info(hectometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def hm2km(hectometer: float):
        """
            Hectometer (hm) to kilometer (km)
        """
        if isinstance(hectometer, (int, float)):
            kilometer = hectometer / 10
            logging.info(kilometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
    
    def km2dam(kilometer: float):
        """
            Kilometer (km) to decameter (dam)
        """
        if isinstance(kilometer, (int, float)):
            decameter = kilometer * 100
            logging.info(decameter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
    
    def dam2km(decameter: float):
        """
            Decameter (dam) to kilometer (km)
        """
        if isinstance(decameter, (int, float)):
            kilometer = decameter / 100
            logging.info(kilometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
    
    def hm2m(hectometer: float):
        """
            Hectometer (hm) to meter (m)
        """
        if isinstance(hectometer, (int, float)):
            meter = hectometer * 100
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def m2hm(meter: float):
        """
            Meter (m) to hectometer (hm)
        """
        if isinstance(meter, (int, float)):
            hectometer = meter / 100
            logging.info(hectometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def dam2m(decameter: float):
        """
            Dacameter (dam) to meter (m)
        """
        if isinstance(decameter, (int, float)):
            meter = decameter * 10
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def m2dam(meter: float):
        """
            Meter (m) to decameter (dam)
        """
        if isinstance(meter, (int, float)):
            decameter = meter / 10
            logging.info(decameter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def m2dm(meter: float):
        """
            Meter (m) to decimeter (dm)
        """
        if isinstance(meter, (int, float)):
            decimeter = meter * 10
            logging.info(decimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def dm2m(decimeter: float):
        """
            Decimeter (dm) to meter (m)
        """
        if isinstance(decimeter, (int, float)):
            meter = decimeter / 10
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def m2cm(meter: float):
        """
            Meter (m) to centimeter (cm)
        """
        if isinstance(meter, (int, float)):
            centimeter = meter * 10
            logging.info(centimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def cm2m(centimeter: float):
        """
            Centimeter (cm) to meter (m)
        """
        if isinstance(centimeter, (int, float)):
            meter = centimeter / 10
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def m2mm(meter: float):
        """
            Meter (m) to milimeter (mm)
        """
        if isinstance(meter, (int, float)):
            milimeter = meter * 1000
            logging.info(milimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def mm2m(milimeter: float):
        """
            Milimeter (mm) to meter (m)
        """
        if isinstance(milimeter, (int, float)):
            meter = milimeter / 100
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def in2cm(inch: float):
        """
            Inch (in) to centimeter (cm)
        """
        if isinstance(inch, (int, float)):
            centimeter = inch * 2.54
            logging.info(centimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def cm2in(centimeter: float):
        """
            Centimeter (cm) to inch (in)
        """
        if isinstance(inch, (int, float)):
            inch = centimeter * 0.393701
            logging.info(inch)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def main():
        try:
            Length.km2m()
            Length.m2km()
            Length.km2hm()
            Length.hm2km()
            Length.km2dam()
            Length.dam2km()
            Length.hm2m()
            Length.m2hm()
            Length.dam2m()
            Length.m2dam()
            Length.m2dm()
            Length.dm2m()
            Length.m2cm()
            Length.cm2m()
            Length.m2mm()
            Length.mm2m()
            Length.in2cm()
            Length.cm2in()
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            
        
    
class WeightMass:
    """
        Converting the measurement units of Weight and Mass
    """
    ton: float
    kilogram: float
    hectogram: float
    dekagram: float
    gram: float
    u: float
    
    def t2kg(ton: float):
        """
            Ton (t) to kilogram (kg)
        """
        if isinstance(ton, (int, float)):
            kilogram = ton * 1000
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def kg2t(kilogram: float):
        """
            Kilogram (kg) to ton (t)
        """
        if isinstance(kilogram, (int, float)):
            ton = kilogram / 1000
            logging.info(ton)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def kg2g(kilogram: float):
        """
            Kilogram (kg) to gram (g)
        """
        if isinstance(kilogram, (int, float)):
            gram = kilogram * 1000
            logging.info(gram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def g2kg(gram: float):
        """
            Gram (g) to kilogram (kg)
        """
        if isinstance(gram, (int, float)):
            kilogram = gram / 1000
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def kg2hg(kilogram: float):
        """
            Kilogram (kg) to hectogram (hg)
        """
        if isinstance(kilogram, (int, float)):
            hectogram = kilogram * 10
            logging.info(hectogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def hg2kg(hectogram: float):
        """
            Hectogram (hg) to kilogram (kg)
        """
        if isinstance(hectogram, (int, float)):
            kilogram = hectogram / 10
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def kg2dag(kilogram: float):
        """
            Kilogram (kg) to dekagram (dag)
        """
        if isinstance(kilogram, (int, float)):
            dekagram = kilogram * 100
            logging.info(dekagram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def dag2kg(dekagram: float):
        """
            Dekagram (dag) to kilogram (kg)
        """
        if isinstance(dekagram, (int, float)):
            kilogram = dekagram / 100
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def hg2g(hectogram: float):
        """
            Hectogram (hg) to gram (g)
        """
        if isinstance(hectogram, (int, float)):
            gram = hectogram * 100
            logging.info(gram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def g2hg(gram: float):
        """
            Gram (g) to hectogram (hg)
        """
        if isinstance(gram, (int, float)):
            hectogram = gram / 100
            logging.info(hectogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def dag2g(dekagram: float):
        """
            Dekagram (dag) to gram (g)
        """
        if isinstance(dekagram, (int, float)):
            gram = dekagram * 10
            logging.info(gram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def g2dag(gram: float):
        """
            Gram (g) to dekagram (dag)
        """
        if isinstance(gram, (int, float)):
            dekagram = gram / 10
            logging.info(dekagram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def lb2oz(pound: float):
        """
            Pound (lb) to ounce (oz)
        """
        if isinstance(pound, (int, float)):
            ounce = pound * 16
            logging.info(ounce)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def oz2lb(ounce: float):
        """
            Ounce (oz) to pound (lb)
        """
        if isinstance(ounce, (int, float)):
            pound = ounce * 0.0625
            logging.info(pound)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def u2kg(u: float):
        """
            Atomic mass unit (u) to kilogram (kg)
        """
        if isinstance(u, (int, float)):
            kilogram = u * 1.6605402E-27
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def kg2u(kilogram: float):
        """
            Kilogram (kg) to atomic mass unit (u)
        """
        if isinstance(kilogram, (int, float)):
            u = kilogram / 1.6605402E-27
            logging.info(u)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def main():
        try:
            WeightMass.t2kg()
            WeightMass.kg2g()
            WeightMass.kg2g()
            WeightMass.g2kg()
            WeightMass.kg2hg()
            WeightMass.hg2kg()
            WeightMass.kg2dag()
            WeightMass.dag2kg()
            WeightMass.hg2g()
            WeightMass.g2hg()
            WeightMass.dag2g()
            WeightMass.g2dag()
            WeightMass.lb2oz()
            WeightMass.oz2lb()
            WeightMass.u2kg()
            WeightMass.kg2u()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        
    
class Temperature:
    """
        Converting the measurement units of Temperature
    """
    Celsius: float
    Fahrenheit: float
    Kelvin: float
    
    def C2F(celsius: float):
        """
            Celsius (°C) to Fahrenheit (°F)
        """
        if isinstance(celsius, (int, float)):
            fahrenheit = (celsius * 9/5) + 32
            logging.info(fahrenheit)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def F2C(fahrenheit: float):
        """
            Fahrenheit (°F) to Celsius (°C)
        """
        if isinstance(fahrenheit, (int, float)):
            celsius = (fahrenheit - 32) * 5/9
            logging.info(celsius)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def C2K(celsius: float):
        """
            Celsius (°C) to Kelvin (K)
        """
        if isinstance(celsius, (int, float)):
            kelvin = celsius + 273.15
            logging.info(kelvin)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def K2C(kelvin: float):
        """
            Kelvin (K) to Celsius (°C)
        """
        if isinstance(kelvin, (int, float)):
            celsius = kelvin - 273.15
            logging.info(celsius)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def F2K(fahrenheit: float):
        """
            Fahrenheit (°F) to Kelvin (K)
        """
        if isinstance(fahrenheit, (int, float)):
            kelvin = ((fahrenheit - 32) * 5/9) + 273.15
            logging.info(kelvin)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def K2F(kelvin: float):
        """
            Kelvin (K) to Fahrenheit (°F)
        """
        if isinstance(kelvin, (int, float)):
            fahrenheit = ((kelvin - 273.15) * 9/5) + 32
            logging.info(fahrenheit)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def main() -> None:
        try:
            Temperature.C2F()
            Temperature.F2C()
            Temperature.C2K()
            Temperature.K2C()
            Temperature.F2K()
            Temperature.K2F()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
    
if __name__ == '__main__':
    value = Length.km2m(2)
    value
    
    value1 = Length.m2cm(2)
    value1
    
    mass = WeightMass.t2kg(4)
    mass