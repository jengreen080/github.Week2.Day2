class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty_bus(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        people_to_pick_up = bus_stop.queue
        return self.passengers.append(people_to_pick_up)