class Book:
    def __init__(self, author, title, price):
        self.__author = ""
        self.__title = ""
        self.__price = 0
        self.set_author(author)
        self.set_title(title)
        self.set_price(price)

    def set_author(self, author):
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_price(self, price):
        self.__price = price

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

book1 = Book("Тарас Шевченко", "Кобзар", 150)
book2 = Book("Ліна Костенко", "Маруся Чурай", 200)
book3 = Book("Леся Українка", "Лісова пісня", 180)

print("Книга 1:", book1.get_author(), "-", book1.get_title(), "-", book1.get_price(), "грн")
print("Книга 2:", book2.get_author(), "-", book2.get_title(), "-", book2.get_price(), "грн")
print("Книга 3:", book3.get_author(), "-", book3.get_title(), "-", book3.get_price(), "грн")
