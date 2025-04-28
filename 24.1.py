import re

class CardCheck:
    @staticmethod
    def check_card_number(card_number: str) -> bool:
        pattern = r'^\d{4}(-\d{4}){3}$'
        return bool(re.fullmatch(pattern, card_number))

    @classmethod
    def check_name(cls, name: str) -> bool:
        pattern = r'^[A-Z]+ [A-Z]+$'
        return bool(re.fullmatch(pattern, name))

if __name__ == "__main__":
    number = '4321-8765-9012-4321'
    name = 'YURIY RYBAK'

    is_number_valid = CardCheck.check_card_number(number)
    is_name_valid = CardCheck.check_name(name)

    print(f"Card number valid: {is_number_valid}")
    print(f"Name valid: {is_name_valid}")         