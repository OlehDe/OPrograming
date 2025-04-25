class Car:
  def __init__(self, brand, model, year):
      self.brand = brand
      self.model = model
      self.year = year

  def display_info(self):
      print(f"brand: {self.brand}, model: {self.model}, year: {self.year}")

  def change_model(self):
      new_model = input("input new model: ")
      self.model = new_model
      return new_model

  def calculate_age(self):
      age_car = 2025 - self.year
      return f"Років: {age_car}"

car1 = Car("bugati", "s5", 2020)
car2 = Car("mersedes", "r2", 2015)
car3 = Car("BMW", "m5", 2019)

car1.display_info()
car2.display_info()
car3.display_info()

car1.change_model()
car2.change_model()
car3.change_model()

print(car1.calculate_age())
print(car2.calculate_age())
print(car3.calculate_age())