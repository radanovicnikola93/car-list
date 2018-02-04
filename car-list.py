class Car(object):
    def __init__(self, c_manufacturer, c_model, km_driven, service):
        self.c_manufacturer = c_manufacturer
        self.c_model = c_model
        self.km_driven = km_driven
        self.service = service

    def full_name(self):
        return self.c_manufacturer + ' ' + self.c_model

opel = Car(c_manufacturer='Opel', c_model='Corsa', km_driven=120000, service="14/07/2017")
mercedes = Car(c_manufacturer='Mercedes', c_model='B', km_driven=100000, service="25/03/2017")
peugeot = Car(c_manufacturer='Peugeot', c_model='208', km_driven=80000, service="13/04/2017")
fiat = Car(c_manufacturer='Fiat', c_model='500', km_driven=8000, service="22/07/2017")

car_list = [opel, mercedes, peugeot, fiat]

for car in car_list:
    print car.full_name()
    print car.km_driven
    print car.service
    print ' '

def car_list(cars):
    if cars == []:
        print "There aren't any cars in your list. Please add some."
    else:
        for index, car in enumerate(cars):
            print "%s) %s %s with %s km driven so far. Last service date: %s" % (index+1, car.car_manufacturer, car.car_model,
                                                                                 car.kilometres_driven, car.last_service)
def create_vehicle_object(c_manufacturer, c_model, km_driven_str, service, cars):
    try:
        km_driven_str = km_driven_str.replace(",", ".")
        km_driven = float(km_driven_str)

        new_car = Car(c_manufacturer=c_manufacturer, c_model=c_model, km_driven=km_driven, service=service)

        cars.append(new_car)

        return True
    except ValueError:
        return False