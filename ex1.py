cars = 50
drivers =5
space_in_a_car = 4.0
drivers_can_take = 3
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = drivers_can_take / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", drivers_can_take, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")