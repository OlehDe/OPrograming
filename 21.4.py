class Cat:
  def __init__(self, breed, age, name, color):
      self.breed = breed
      self.age = age
      self.name = name
      self.color = color

exemplar1 = Cat("Бродяга", 2, "Барсік", "Чорний")
exemplar2 = Cat("Сіамський", 1, "Jojo", "Фіолетовий")
exemplar3 = Cat("Єгипецький", 3, "Marco", "Лисий")

print(f"breed: {exemplar1.breed}, age: {exemplar1.age}, name: {exemplar1.name}, color: {exemplar1.color}")
print(f"breed: {exemplar2.breed}, age: {exemplar2.age}, name: {exemplar2.name}, color: {exemplar2.color}")
print(f"breed: {exemplar3.breed}, age: {exemplar3.age}, name: {exemplar3.name}, color: {exemplar3.color}")
