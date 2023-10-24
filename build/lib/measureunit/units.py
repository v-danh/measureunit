import logging
logging.basicConfig(level=logging.INFO, 
                    format=' %(asctime)s | %(levelname)s | %(message)s')


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
<<<<<<< HEAD
        meter = kilometer * 1000
        if not isinstance(kilometer, (int, float)):
            raise ValueError("The value must be an integer.")
        else:
            return meter
    
=======
        if isinstance(kilometer, (int, float)):
            meter = kilometer * 1000
            logging.info(meter)
        else:
            raise ValueError("The value must be an integer. Please try again!")

>>>>>>> main
    def m2km(meter: float):
        """
            Meter (m) to kilometer (km)
        """
<<<<<<< HEAD
        kilometer = meter / 1000
        if not isinstance(meter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kilometer
    
=======
        if isinstance(meter, (int, float)):
            kilometer = meter / 1000
            logging.info(kilometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')

>>>>>>> main
    def km2hm(kilometer: float):
        """
            Kilometer (km) to hectometer (hm)
        """
<<<<<<< HEAD
        hectometer = kilometer * 10
        if not isinstance(kilometer, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return hectometer
    
=======
        if isinstance(kilometer, (int, float)):
            hectometer = kilometer * 10
            logging.info(hectometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def hm2km(hectometer: float):
        """
            Hectometer (hm) to kilometer (km)
        """
<<<<<<< HEAD
        kilometer = hectometer / 10
        if not isinstance(hectometer, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kilometer
=======
        if isinstance(hectometer, (int, float)):
            kilometer = hectometer / 10
            logging.info(kilometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
>>>>>>> main
    
    def km2dam(kilometer: float):
        """
            Kilometer (km) to decameter (dam)
        """
<<<<<<< HEAD
        decameter = kilometer * 100
        if not isinstance(kilometer, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return decameter
=======
        if isinstance(kilometer, (int, float)):
            decameter = kilometer * 100
            logging.info(decameter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
>>>>>>> main
    
    def dam2km(decameter: float):
        """
            Decameter (dam) to kilometer (km)
        """
<<<<<<< HEAD
        kilometer = decameter / 100
        if not isinstance(decameter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kilometer
=======
        if isinstance(decameter, (int, float)):
            kilometer = decameter / 100
            logging.info(kilometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
>>>>>>> main
    
    def hm2m(hectometer: float):
        """
            Hectometer (hm) to meter (m)
        """
<<<<<<< HEAD
        meter = hectometer * 100
        if not isinstance(hectometer, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return meter
    
=======
        if isinstance(hectometer, (int, float)):
            meter = hectometer * 100
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def m2hm(meter: float):
        """
            Meter (m) to hectometer (hm)
        """
<<<<<<< HEAD
        hectometer = meter / 100
        if not isinstance(meter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return hectometer
    
=======
        if isinstance(meter, (int, float)):
            hectometer = meter / 100
            logging.info(hectometer)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def dam2m(decameter: float):
        """
            Dacameter (dam) to meter (m)
        """
<<<<<<< HEAD
        meter = decameter * 10
        if not isinstance(decameter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return meter
    
=======
        if isinstance(decameter, (int, float)):
            meter = decameter * 10
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def m2dam(meter: float):
        """
            Meter (m) to decameter (dam)
        """
<<<<<<< HEAD
        decameter = meter / 10
        if not isinstance(meter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return decameter
    
=======
        if isinstance(meter, (int, float)):
            decameter = meter / 10
            logging.info(decameter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def m2dm(meter: float):
        """
            Meter (m) to decimeter (dm)
        """
<<<<<<< HEAD
        decimeter = meter * 10
        if not isinstance(meter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return decimeter
    
=======
        if isinstance(meter, (int, float)):
            decimeter = meter * 10
            logging.info(decimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def dm2m(decimeter: float):
        """
            Decimeter (dm) to meter (m)
        """
<<<<<<< HEAD
        meter = decimeter / 10
        if not isinstance(decimeter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return meter
    
=======
        if isinstance(decimeter, (int, float)):
            meter = decimeter / 10
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def m2cm(meter: float):
        """
            Meter (m) to centimeter (cm)
        """
<<<<<<< HEAD
        centimeter = meter * 10
        if not isinstance(meter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return centimeter
    
=======
        if isinstance(meter, (int, float)):
            centimeter = meter * 10
            logging.info(centimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def cm2m(centimeter: float):
        """
            Centimeter (cm) to meter (m)
        """
<<<<<<< HEAD
        meter = centimeter / 10
        if not isinstance(centimeter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return meter
    
=======
        if isinstance(centimeter, (int, float)):
            meter = centimeter / 10
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def m2mm(meter: float):
        """
            Meter (m) to milimeter (mm)
        """
<<<<<<< HEAD
        milimeter = meter * 1000
        if not isinstance(meter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return milimeter
    
=======
        if isinstance(meter, (int, float)):
            milimeter = meter * 1000
            logging.info(milimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def mm2m(milimeter: float):
        """
            Milimeter (mm) to meter (m)
        """
<<<<<<< HEAD
        meter = milimeter / 100
        if not isinstance(milimeter, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return meter
    
=======
        if isinstance(milimeter, (int, float)):
            meter = milimeter / 100
            logging.info(meter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def in2cm(inch: float):
        """
            Inch (in) to centimeter (cm)
        """
<<<<<<< HEAD
        centimeter = inch * 2.54
        if not isinstance(inch, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return centimeter
    
=======
        if isinstance(inch, (int, float)):
            centimeter = inch * 2.54
            logging.info(centimeter)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def cm2in(centimeter: float):
        """
            Centimeter (cm) to inch (in)
        """
<<<<<<< HEAD
        inch = centimeter * 0.393701
        if not isinstance(inch, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return inch
    
=======
        if isinstance(inch, (int, float)):
            inch = centimeter * 0.393701
            logging.info(inch)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
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
<<<<<<< HEAD
            logging.error(f'An error occurred: {e}. Please try again!')
            
=======
            logging.error(f'An error occurred: {e}')
            
        
    
>>>>>>> main
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
<<<<<<< HEAD
        kilogram = ton * 1000
        if not isinstance(ton, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            logging.info(kilogram)
    
=======
        if isinstance(ton, (int, float)):
            kilogram = ton * 1000
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def kg2t(kilogram: float):
        """
            Kilogram (kg) to ton (t)
        """
<<<<<<< HEAD
        ton = kilogram / 1000
        if not isinstance(kilogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return ton
    
=======
        if isinstance(kilogram, (int, float)):
            ton = kilogram / 1000
            logging.info(ton)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def kg2g(kilogram: float):
        """
            Kilogram (kg) to gram (g)
        """
<<<<<<< HEAD
        gram = kilogram * 1000
        if not isinstance(kilogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return gram
    
=======
        if isinstance(kilogram, (int, float)):
            gram = kilogram * 1000
            logging.info(gram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def g2kg(gram: float):
        """
            Gram (g) to kilogram (kg)
        """
<<<<<<< HEAD
        kilogram = gram / 1000
        if not isinstance(gram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kilogram
    
=======
        if isinstance(gram, (int, float)):
            kilogram = gram / 1000
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def kg2hg(kilogram: float):
        """
            Kilogram (kg) to hectogram (hg)
        """
<<<<<<< HEAD
        hectogram = kilogram * 10
        if not isinstance(kilogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return hectogram
    
=======
        if isinstance(kilogram, (int, float)):
            hectogram = kilogram * 10
            logging.info(hectogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def hg2kg(hectogram: float):
        """
            Hectogram (hg) to kilogram (kg)
        """
<<<<<<< HEAD
        kilogram = hectogram / 10
        if not isinstance(hectogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kilogram
    
=======
        if isinstance(hectogram, (int, float)):
            kilogram = hectogram / 10
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def kg2dag(kilogram: float):
        """
            Kilogram (kg) to dekagram (dag)
        """
<<<<<<< HEAD
        dekagram = kilogram * 100
        if not isinstance(kilogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return dekagram
    
=======
        if isinstance(kilogram, (int, float)):
            dekagram = kilogram * 100
            logging.info(dekagram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def dag2kg(dekagram: float):
        """
            Dekagram (dag) to kilogram (kg)
        """
<<<<<<< HEAD
        kilogram = dekagram / 100
        if not isinstance(dekagram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kilogram
    
=======
        if isinstance(dekagram, (int, float)):
            kilogram = dekagram / 100
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def hg2g(hectogram: float):
        """
            Hectogram (hg) to gram (g)
        """
<<<<<<< HEAD
        gram = hectogram * 100
        if not isinstance(hectogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return gram
    
=======
        if isinstance(hectogram, (int, float)):
            gram = hectogram * 100
            logging.info(gram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def g2hg(gram: float):
        """
            Gram (g) to hectogram (hg)
        """
<<<<<<< HEAD
        hectogram = gram / 100
        if not isinstance(gram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return hectogram
    
=======
        if isinstance(gram, (int, float)):
            hectogram = gram / 100
            logging.info(hectogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def dag2g(dekagram: float):
        """
            Dekagram (dag) to gram (g)
        """
<<<<<<< HEAD
        gram = dekagram * 10
        if not isinstance(dekagram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return gram
    
=======
        if isinstance(dekagram, (int, float)):
            gram = dekagram * 10
            logging.info(gram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def g2dag(gram: float):
        """
            Gram (g) to dekagram (dag)
        """
<<<<<<< HEAD
        dekagram = gram / 10
        if not isinstance(gram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return dekagram
    
=======
        if isinstance(gram, (int, float)):
            dekagram = gram / 10
            logging.info(dekagram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def lb2oz(pound: float):
        """
            Pound (lb) to ounce (oz)
        """
<<<<<<< HEAD
        ounce = pound * 16
        if not isinstance(pound, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return ounce
    
=======
        if isinstance(pound, (int, float)):
            ounce = pound * 16
            logging.info(ounce)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def oz2lb(ounce: float):
        """
            Ounce (oz) to pound (lb)
        """
<<<<<<< HEAD
        pound = ounce * 0.0625
        if not isinstance(ounce, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return pound
    
=======
        if isinstance(ounce, (int, float)):
            pound = ounce * 0.0625
            logging.info(pound)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def u2kg(u: float):
        """
            Atomic mass unit (u) to kilogram (kg)
        """
<<<<<<< HEAD
        kilogram = u * 1.6605402E-27
        if not isinstance(u, (int, float)):
            raise ValueError('The value must be an integer.')  
        else:
            return kilogram
    
=======
        if isinstance(u, (int, float)):
            kilogram = u * 1.6605402E-27
            logging.info(kilogram)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def kg2u(kilogram: float):
        """
            Kilogram (kg) to atomic mass unit (u)
        """
<<<<<<< HEAD
        u = kilogram / 1.6605402E-27
        if not isinstance(kilogram, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return u
    
=======
        if isinstance(kilogram, (int, float)):
            u = kilogram / 1.6605402E-27
            logging.info(u)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
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
<<<<<<< HEAD
            logging.error(f'An error occurred: {e}. Please try again!')
=======
            logging.error(f"An error occurred: {e}")
        
>>>>>>> main
    
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
<<<<<<< HEAD
        fahrenheit = (celsius * 9/5) + 32
        if not isinstance(celsius, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return fahrenheit
    
=======
        if isinstance(celsius, (int, float)):
            fahrenheit = (celsius * 9/5) + 32
            logging.info(fahrenheit)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def F2C(fahrenheit: float):
        """
            Fahrenheit (°F) to Celsius (°C)
        """
<<<<<<< HEAD
        celsius = (fahrenheit - 32) * 5/9
        if not isinstance(fahrenheit, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return celsius
    
=======
        if isinstance(fahrenheit, (int, float)):
            celsius = (fahrenheit - 32) * 5/9
            logging.info(celsius)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def C2K(celsius: float):
        """
            Celsius (°C) to Kelvin (K)
        """
<<<<<<< HEAD
        kelvin = celsius + 273.15
        if not isinstance(celsius, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kelvin
    
=======
        if isinstance(celsius, (int, float)):
            kelvin = celsius + 273.15
            logging.info(kelvin)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def K2C(kelvin: float):
        """
            Kelvin (K) to Celsius (°C)
        """
<<<<<<< HEAD
        celsius = kelvin - 273.15
        if not isinstance(kelvin, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return celsius
    
=======
        if isinstance(kelvin, (int, float)):
            celsius = kelvin - 273.15
            logging.info(celsius)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def F2K(fahrenheit: float):
        """
            Fahrenheit (°F) to Kelvin (K)
        """
<<<<<<< HEAD
        kelvin = ((fahrenheit - 32) * 5/9) + 273.15
        if not isinstance(fahrenheit, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return kelvin
    
=======
        if isinstance(fahrenheit, (int, float)):
            kelvin = ((fahrenheit - 32) * 5/9) + 273.15
            logging.info(kelvin)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
>>>>>>> main
    def K2F(kelvin: float):
        """
            Kelvin (K) to Fahrenheit (°F)
        """
<<<<<<< HEAD
        fahrenheit = ((kelvin - 273.15) * 9/5) + 32
        if not isinstance(kelvin, (int, float)):
            raise ValueError('The value must be an integer.')
        else:
            return fahrenheit
    
    def main():
=======
        if isinstance(kelvin, (int, float)):
            fahrenheit = ((kelvin - 273.15) * 9/5) + 32
            logging.info(fahrenheit)
        else:
            raise ValueError('The value must be an integer. Please try again!')
        
    def main() -> None:
>>>>>>> main
        try:
            Temperature.C2F()
            Temperature.F2C()
            Temperature.C2K()
            Temperature.K2C()
            Temperature.F2K()
            Temperature.K2F()
        except Exception as e:
<<<<<<< HEAD
            logging.error(f'An error occurred: {e}. Please try again!')
    
if __name__ == '__main__':
    v = Length.km2m()
    logging.info(f'The result of v = {v}')
=======
            logging.error(f"An error occurred: {e}")
    
if __name__ == '__main__':
    value = Length.km2m(2)
    value
    
    value1 = Length.m2cm(2)
    value1
    
    mass = WeightMass.t2kg(4)
    mass
>>>>>>> main
