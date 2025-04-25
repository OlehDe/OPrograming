class Car:
    def __init__(self, brand, model, year, speed, power, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        self.power = power
        self.color = color

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Driver:
    def __init__(self, name, age, driving_experience):
        self.name = name
        self.age = age
        self.driving_experience = driving_experience

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Driving Experience: {self.driving_experience} years"

class Race:
    def start_race(self, car1, car2):
        score_car1 = car1.speed + car1.power * 0.1 + car1.year * 0.05 + car1.model.count("X") * 10
        score_car2 = car2.speed + car2.power * 0.1 + car2.year * 0.05 + car2.model.count("X") * 10

        score_driver1 = car1.speed * 0.1 + car1.power * 0.2 + car1.year * 0.1 + driver1.driving_experience * 2
        score_driver2 = car2.speed * 0.1 + car2.power * 0.2 + car2.year * 0.1 + driver2.driving_experience * 2

        if score_car1 + score_driver1 > score_car2 + score_driver2:
            return car1
        else:
            return car2

    def print_winner(self, winner):
        print(f"The winner is {winner}!")

if __name__ == "__main__":
    car1 = Car("BMW", "X5", 2022, 250, 300, "Black")
    car2 = Car("Audi", "A6", 2023, 240, 280, "White")
    driver1 = Driver("John", 35, 15)
    driver2 = Driver("Alice", 28, 10)
    race = Race()

    winner = race.start_race(car1, car2)
    race.print_winner(winner)
