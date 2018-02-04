class Car(object):
    def __init__(self, c_manufacturer, c_model, km_driven, service):
        self.c_manufacturer = c_manufacturer
        self.c_model = c_model
        self.km_driven = km_driven
        self.service = service

    def full_name(self):
        return self.c_manufacturer + ' ' + self.c_model

    def add_km(self, new_km):
        self.km_driven += new_km

    def update_service_date(self, new_date):
        self.service = new_date

def car_list(cars):
    if cars == []:
        print "There aren't any cars in your list. Please add some."
    else:
        for index, car in enumerate(cars):
            print "%s) %s %s with %s km driven so far. Last service date: %s" % (index+1, car.c_manufacturer, car.c_model,
                                                                                 car.km_driven, car.service)
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

def add_new_km(cars):
    select_vehicle = choose_car(cars)

    print "Vehicle selected: %s %s with %s km." % (select_vehicle.c_manufacturer, select_vehicle.c_model, select_vehicle.km_driven)
    print ""
    new_km_str = raw_input("How many kilometers would you like to add to the existing ones? (enter only a number) ")
    print ""

    try:
        new_km_str = new_km_str.replace(",", ".")
        new_km = float(new_km_str)

        select_vehicle.add_km(new_km)
        print "New number of kilometers for %s %s is now: %s." % (select_vehicle.c_manufacturer, select_vehicle.c_model, select_vehicle.km_driven)
    except ValueError:
        print "Please enter just a number for the kilometers you'd like to add."

def change_service_date(cars):
    select_vehicle = choose_car(cars)

    print "Vehicle selected: %s %s with service date: %s." % (select_vehicle.c_manufacturer, select_vehicle.c_model, select_vehicle.service)
    print ""
    new_service_date = raw_input("What is the new service date for this vehicle? (DD.MM.YYYY) ")
    print ""
    select_vehicle.update_service_date(new_date=new_service_date)
    print "Service date updated!"

def save(cars):
    with open("cars.txt", "w+") as car_file:
        for car in cars:
            car_file.write("%s,%s,%s,%s\n" % (car.c_manufacturer, car.c_model, car.km_driven, car.service))

def main():
    print "Welcome to the Car Manager program."

    cars = []

    with open("cars.txt", "w+") as car_file:
        for line in car_file:
            try:
                c_manufacturer, c_model, km_driven_str, service = line.split(",")
                create_car_object(c_manufacturer, c_model, km_driven_str, service, cars)
            except ValueError:
                continue

        while True:
            print ""
            print "Please pick one of the following options:"
            print "1) See a list of all the company vehicles."
            print "2) Add new vehicle."
            print "3) Edit the kilometers done for the chosen vehicle."
            print "4) Edit the last service date for the chosen vehicle."
            print "5) Quit the program."
            print ""

            choice = int(raw_input("Which option would you like to choose? (1, 2, 3, 4, 5) "))
            print ""

            if choice == 1:
                car_list(cars)
            elif choice == 2:
                add_new_car(cars)
            elif choice == 3:
                add_new_km(cars)
            elif choice == 4:
                change_service_date(cars)
            elif choice == 5:
                print "Thank you for using the Car Manager!"
                save(cars)
                break
            else:
                print "Please type just numbers from option 1 to 5"

if __name__ == "__main__":
    main()