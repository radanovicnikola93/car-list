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
def create_car_object(c_manufacturer, c_model, km_driven_str, service, cars):
    try:
        km_driven_str = km_driven_str.replace(",", ".")
        km_driven = float(km_driven_str)

        new_car = Car(c_manufacturer=c_manufacturer, c_model=c_model, km_driven=km_driven, service=service)
        cars.append(new_car)

        return True
    except ValueError:
        return False

def add_new_car(cars):
    c_manufacturer = raw_input("Please enter the car manufacturer: ")
    c_model = raw_input("Please enter the model of the car: ")
    km_driven_str = raw_input("Please enter the amount of kilometers that vehicle has done so far (just a number): ")
    service = raw_input("Please enter the last service date (DD.MM.YYYY): ")

    result = create_car_object(c_manufacturer, c_model, km_driven_str, service, cars)

    if result:
        print "You have successfully added %s %s as a new vehicle!" % (c_manufacturer, c_model)
    else:
        print "Please enter just a number for the kilometers done so far."


def choose_car(cars):
    print "Please choose the number of the vehicle that you would like to edit."
    print ""
    car_list(cars)
    print ""
    selection = raw_input("What vehicle number would you like to choose? ")
    return cars[int(selection) - 1]

