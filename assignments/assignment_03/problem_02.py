class Vehicle:
    """
    age: age in years
    condition: condition (proportion relative to new)
    """
    def __init__(self, age: int = 0, condition: float = 1):
        assert age >= 0
        assert 1 >= condition >= 0
        self.age = age
        self.condition = condition

    """
    crash Vehicle, renders it unusable
    """
    def crash(self):
        self.condition = 0

    """
    restore Vehicle, (close) to its former glory
    """
    def restore(self):
        self.condition = max(0.95, self.condition)

    def __repr__(self):
        properties = [f"{key.capitalize()}: {value}" for key, value in self.__dict__.items()] 
        return "<<\n" +  f"[{self.__class__.__name__}]" + "\n- " + "\n- ".join(properties) + "\n>>"

class Car(Vehicle):
    """
    model: model of car
    seats: number of seats in the car
    odometer: distance travelled in kms
    """
    def __init__(self, model: str, seats: int = 4, odometer: int = 0, *args, **kwargs):
        assert seats > 0
        assert odometer >= 0
        super().__init__(*args, **kwargs)
        self.model = model
        self.seats = seats
        self.odometer = odometer

    """
    distance: distance to be covered in km 

    condition is degraded by 1e-6 per km travelled (up to a million kms before reaching condition 0)
    """
    def drive(self, distance: float):
        if self.condition > 0:
            self.odometer += distance
            self.condition = max(0, self.condition - distance*1e-6)
        else:
            print("[ERROR] Car cannot drive until repaired or restored.")

class Plane(Vehicle):
    """
    model: model of plane
    seating_capacity: number of passengers able to be carried
    """
    def __init__(self, model: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    """
    duration: flight duration in hours 

    condition is degraded by 0.0001 per hour flown
    plane can only fly if condition is 0.4 or better
    """
    def fly(self, duration: float):
        # planes have strict standards for inspection approval than cars
        if self.condition >= 0.4: 
            self.condition = max(0, self.condition - duration * 1e-4)
        else:
            print("[ERROR] Plane cannot fly until repaired or restored.")

class CommercialAirplane(Plane):
    """
    airline: airline under which the airpline is operating
    seating_capacity: number of passengers that will fit in the plane
    """
    def __init__(self, model: str, seating_capacity: int, airline: str, *args, **kwargs):
        assert seating_capacity > 0
        super().__init__(model, *args, **kwargs)
        self.airline = airline
        self.seating_capacity = seating_capacity

class FighterJet(Plane):
    """
    nationality: country operating the airplane
    weaponry: weapon "accessories"
    """
    def __init__(self, model: str, nationality: str, weaponry: list[str],*args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.nationality = nationality
        self.weaponry = weaponry