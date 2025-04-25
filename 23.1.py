class Clock:
    def __init__(self, time=0):
        self.__time = 0
        self.set_time(time)

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(time):
        return isinstance(time, int) and 0 <= time < 100000

clock = Clock(4530)
print("Поточний час:", clock.get_time())
