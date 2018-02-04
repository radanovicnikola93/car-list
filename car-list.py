class Car(object):
    def __init__(self, c_manufacturer, c_model, km_driven, service):
        self.car_manufacturer = c_manufacturer
        self.car_model = c_model
        self.kilometres_driven = km_driven
        self.last_service = service

    def full_name(self):
        return self.car_manufacturer + ' ' + self.car_model

opel = Car(c_manufacturer='Opel', c_model='Corsa', km_driven=120000, service="14/07/2017")
mercedes = Car(c_manufacturer='Mercedes', c_model='B', km_driven=100000, service="25/03/2017")
peugeot = Car(c_manufacturer='Peugeot', c_model='208', km_driven=80000, service="13/04/2017")
fiat = Car(c_manufacturer='Fiat', c_model='500', km_driven=8000, service="22/07/2017")

car_list = [opel, mercedes, peugeot, fiat]

for car in car_list:
    print car.full_name()
    print car.kilometres_driven
    print car.last_service
    print ' '



