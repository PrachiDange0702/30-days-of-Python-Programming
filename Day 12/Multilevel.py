class Vehicle:
	def Vehicle_info(self):
		print("Inside vehicle class")

class Car(Vehicle):
	def car_info(self):
		print("Inside Car class")


class SportsCar(Car):
	def sport_info(self):
		print("Inside Sports car")

s_car=SportsCar()

s_car.Vehicle_info()
s_car.car_info()
s_car.sport_info()
