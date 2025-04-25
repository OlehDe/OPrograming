class Money:
    def __init__(self, money=0):
        self.__money = 0
        self.set_money(money)

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, money_obj):
        if isinstance(money_obj, Money):
            self.__money += money_obj.get_money()

    @staticmethod
    def __check_money(money):
        return isinstance(money, int) and money >= 0

money1 = Money(10)
money2 = Money(20)
money1.set_money(100)
money2.add_money(money1)

print(money1.get_money())
print(money2.get_money())
