from collections import UserDict
from datetime import datetime
import pickle
from colorama import Fore, Style, init
import re


# Клас для базового поля (Field) і його наслідування
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise ValueError("Invalid phone number format") + Fore.RED
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") + Fore.RED
        super().__init__(self.value)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


# Клас Record: запис для контакту
class Record:
    pass

    def add_phone(self, phone):
        pass

    def remove_phone(self, phone):
        pass

    def edit_phone(self, old_phone, new_phone):
        pass

    def add_birthday(self, birthday):
        pass

    def days_to_birthday(self):
        pass

    def __str__(self):
        pass


# Клас AddressBook
class AddressBook(UserDict):
    pass

    def find(self, name):
        pass

    def delete(self, name):
        pass

    def get_upcoming_birthdays(self):
        pass


# Для зберігання даних у файл

# serialisation

def save_data():
    pass


# deserialisation

def load_data():
    pass


# Декоратор для обробки помилок
def input_error(func):
    pass


# Команди для роботи з адресною книгою
@input_error
def add_contact(args, book: AddressBook):
    pass


@input_error
def change_phone(args, book: AddressBook):
    pass


@input_error
def show_phones(args, book: AddressBook):
    pass


@input_error
def show_all(book: AddressBook):
    pass


@input_error
def add_birthday(args, book: AddressBook):
    pass


@input_error
def birthdays(args, book: AddressBook):
    pass


# Функція для обробки команд
def parse_input():
    pass


# Головна функція для запуску програми
def main():
    pass


if __name__ == "__main__":
    main()
