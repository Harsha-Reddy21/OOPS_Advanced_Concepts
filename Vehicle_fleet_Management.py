# from datetime import datetime
from datetime import datetime

class MaintenanceRecord:
    def __init__(self):  # Fixed: was _init__ (missing underscore)
        self.maintenance_logs=[]

    def add_maintenance(self,description):
        self.maintenance_logs.append({
            "date":datetime.now().strftime("%Y-%m-%d"),
            "description":description
        })

    def get_maintenance_history(self):
        return self.maintenance_logs

class Vehicle(MaintenanceRecord):
    def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type):
        super().__init__()
        self.vehicle_id=vehicle_id
        self.make=make
        self.model=model
        self.year=year
        self.daily_rate=daily_rate
        self.is_available=is_available
        self.mileage=mileage
        self.fuel_type=fuel_type
        
    def rent(self):
        if not self.is_available:
            return "Vehicle is not available for rent"
        self.is_available=False
        return f"Vehicle {self.vehicle_id} rented successfully"
    
    def return_vehicle(self):
        self.is_available=True
        return f"Vehicle {self.vehicle_id} returned successfully"
    
    def calculate_rental_cost(self,days):
        return self.daily_rate * days
    
    def get_vehicle_info(self):
        return f"Vehicle ID: {self.vehicle_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Daily Rate: ${self.daily_rate}, Available: {'Yes' if self.is_available else 'No'}, Mileage: {self.mileage} miles, Fuel Type: {self.fuel_type}"
    
    def calculate_fuel_efficiency(self):
        raise NotImplementedError("Subclasses must implement this method")  # Fixed: was return instead of raise
    

class Car(Vehicle):
    def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type,seating_capacity,transmission_type,has_gps):
        super().__init__(vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type)
        self.seating_capacity=seating_capacity
        self.transmission_type=transmission_type
        self.has_gps=has_gps 
        
    def get_vehicle_info(self):  # Fixed: removed duplicate method
        base_info=super().get_vehicle_info()
        return f"{base_info}, Seating Capacity: {self.seating_capacity}, Transmission: {self.transmission_type}, GPS: {'Yes' if self.has_gps else 'No'}"

    def calculate_rental_cost(self, days):
        multiplier=1.2 if self.has_gps else 1.0
        return self.daily_rate * days * multiplier
    
    def calculate_fuel_efficiency(self):
        return {"city_mpg":20,"highway_mpg":30}
    
class Motorcycle(Vehicle):
    def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type,engine_capacity,bike_type):
        super().__init__(vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type)
        self.engine_capacity=engine_capacity
        self.bike_type=bike_type 
        
    def get_vehicle_info(self):  # Fixed: removed duplicate method
        base_info=super().get_vehicle_info()
        return f"{base_info}, Engine Capacity: {self.engine_capacity} cc, Bike Type: {self.bike_type}"
    
    def calculate_rental_cost(self,days):
        return self.daily_rate * days * 0.8
    
    def calculate_fuel_efficiency(self):
        return 60
    
class Truck(Vehicle):
    def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type,cargo_capacity,is_cdl_required,max_weight):  # Fixed: added missing parameters and removed engine_capacity
        super().__init__(vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type)
        self.cargo_capacity=cargo_capacity
        self.is_license_required=is_cdl_required
        self.max_weight=max_weight  # Fixed: now properly defined as parameter
        
    def calculate_rental_cost(self,days):
        return self.daily_rate * days * 1.5
    
    def calculate_fuel_efficiency(self):
        return {"empty_mpg":15,"loaded_mpg":12}
    
    def get_vehicle_info(self):
        base_info=super().get_vehicle_info()
        return f"{base_info}, Cargo Capacity: {self.cargo_capacity} lbs, License Required: {'Yes' if self.is_license_required else 'No'}, Max Weight: {self.max_weight} lbs"
    

if __name__ == "__main__":
    car = Car("CAR001", "Toyota", "Camry", 2023, 45.0, True, 12000, "Petrol", 5, "Automatic", True)
    motorcycle = Motorcycle("BIKE001", "Harley", "Street 750", 2022, 35.0, True, 8000, "Petrol", 750, "Cruiser")
    truck = Truck("TRUCK001", "Ford", "F-150", 2023, 85.0, True, 15000, "Diesel", 5000, True, 8000)  # Fixed: updated parameters

    assert car.seating_capacity == 5
    assert car.rent().lower() == "vehicle car001 rented successfully"  # Fixed: corrected expected message
    assert car.is_available == False
    assert car.return_vehicle().lower() == "vehicle car001 returned successfully"  # Fixed: corrected expected message
    assert car.is_available == True

    assert abs(car.calculate_rental_cost(3) - (45.0 * 3 * 1.2)) < 0.01
    assert abs(motorcycle.calculate_rental_cost(3) - (35.0 * 3 * 0.8)) < 0.01
    assert abs(truck.calculate_rental_cost(2) - (85.0 * 2 * 1.5)) < 0.01

    vehicles = [car, motorcycle, truck]
    for v in vehicles:
        info = v.get_vehicle_info()
        assert v.make in info and v.model in info
        if hasattr(v, "seating_capacity"):
            assert str(v.seating_capacity) in info
        elif hasattr(v, "engine_capacity"):  # Fixed: was engine_cc, should be engine_capacity
            assert str(v.engine_capacity) in info
        elif hasattr(v, "cargo_capacity"):
            assert str(v.cargo_capacity) in info

    assert isinstance(car.calculate_fuel_efficiency(), dict)
    assert isinstance(motorcycle.calculate_fuel_efficiency(), (int, float))
    assert isinstance(truck.calculate_fuel_efficiency(), dict)

    # Maintenance records
    car.add_maintenance("Oil change")
    assert len(car.get_maintenance_history()) == 1



# class Vehicle:
#     def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type):
#         self.vehicle_id=vehicle_id
#         self.make=make
#         self.model=model
#         self.year=year
#         self.daily_rate=daily_rate
#         self.is_available=is_available
#         self.mileage=mileage
#         self.fuel_type=fuel_type
       
# class Car(Vehicle):
#     def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type,seating_capacity):
#         super().__init__(vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type)
#         self.seating_capacity=seating_capacity
       
# class Motorcycle(Vehicle):
#     def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type,engine_capacity):
#         super().__init__(vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type)

# class Truck(Vehicle):
#     def __init__(self,vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type,engine_capacity):
#         super().__init__(vehicle_id,make,model,year,daily_rate,is_available,mileage,fuel_type)
#         self.engine_capacity=engine_capacity









