class Person:
   def __init__(self):
       self.first_name = "Олег"
       self.last_name = "Дячок"
       self.age = 18
       self.date_of_birth = "2007-01-07"

person = Person()

print(f"first_name: {hasattr(person, 'first_name')}")
