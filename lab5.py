# змінити назви змінних і класів згідно з PEP8, додати декоратори, доробити метод sort

from enum import Enum

class Gender(Enum):
    FEMALE = 5
    MALE = 4
    NON_BINARY = 3
    OTHER = 2

class Guest:
    def __init__(self, guest_id=123, name="Ivan", age=20, city="Lviv", phone_number=1234567890, gender=Gender.FEMALE):
        self.__id = guest_id
        self.__name = name
        self.__age = age
        self.__city = city
        self.__phone_number = phone_number
        self.__gender = gender

    def get_id(self):
        return self.__id
    
    def id(self, guest_id):
        self.__id = guest_id

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_city(self):
        return self.__city
    
    def set_city(self, city):
        self.__city = city

    def get_phone_number(self):
        return self.__phone_number
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def is_lucky_phone_number(self):
        return str(self.__phone_number).count("7") > 3

    def __del__(self):
        print(f"Guest {self.__name} has been deleted")

    def __str__(self):
        return (f"Guest (id: {self.__id}, name: {self.__name}, age: {self.__age}, from city: {self.__city}, with phone number: {self.__phone_number})")

    def __repr__(self):
        return (f"Guest({self.__id}, {self.__name}, {self.__age}, {self.__city}, {self.__phone_number}, {self.__gender})")



class Party:
    def __init__(self, day, reason):
        self.__day = day
        self.__reason = reason
        self.guests = []

    @property
    def get_day(self):
        return self.__day
    
    @get_day.setter
    def day(self, day):
        self.__day = day

    @property
    def get_reason(self):
        return self.__reason

    @get_reason.setter
    def reason(self, reason):
        self.__reason = reason

    def __del__(self):
        print(f"Party on {self.__day} has been deleted")

    def add_guest(self, guest):
        self.guests.append(guest)

    def find_average_age(self, gender=Gender):
        ages = [guest.get_age() for guest in self.guests if guest.get_gender() == gender]
        return sum(ages) / len(ages)

    def sort_guests_by_id(self):
        sorted_guests = self.guests.sort(key = lambda guest: guest.get_id())
        return sorted_guests

    def __str__(self):
        return (f"Party (on {self.__day} is dedicated to {self.__reason})")

    def __repr__(self):
        return (f"Party ('{self.__day}', '{self.__reason}')")

if __name__ == "__main__":
    guest_1 = Guest(1, "Alina", 20, "Lviv", "7771234567", Gender.FEMALE)
    guest_2 = Guest(2, "Bob", 25, "London", "1234567", Gender.MALE)
    guest_3 = Guest(3, "Char", 29, "Kyiv", "7777777", Gender.NON_BINARY)
    guest_4 = Guest(4, "Asdf", 27, "City", "7775678901", Gender.OTHER)
    guest_5 = Guest(5, "Mia", 30, "ASDF", "345676543456", Gender.FEMALE)
    party = Party("31.10.2024", "Helloween")

    party.add_guest(guest_1)
    party.add_guest(guest_2)
    party.add_guest(guest_3)
    party.add_guest(guest_4)
    party.add_guest(guest_5)

    print("Average age of FEMALE guests:", party.find_average_age(Gender.FEMALE))
    print("Average age of MALE guests:", party.find_average_age(Gender.MALE))
    print("Average age of NON_BINARY guests:", party.find_average_age(Gender.NON_BINARY))
    print("Average age of OTHER guests:", party.find_average_age(Gender.OTHER))

    party.sort_guests_by_id()
    print(party)

    print(guest_1.is_lucky_phone_number())
    print(guest_2.is_lucky_phone_number())
    print(guest_3.is_lucky_phone_number())
    print(guest_4.is_lucky_phone_number())
    print(guest_5.is_lucky_phone_number())