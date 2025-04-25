class Car:
   mark = "Volkswagen"
   model = "Passat B5"
   weight = 25000
   price = 7000

print(f"weight: {Car.weight}, mark: {Car.mark}, model: {Car.model}, price: {Car.price}")

print(getattr(Car, "mark", False))
print(getattr(Car, "model", False))
setattr(Car, "color", "black")
delattr(Car, "weight")

print(f"mark: {Car.mark}, model: {Car.model}, price: {Car.price}")

