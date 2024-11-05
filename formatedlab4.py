class Park:
    public_numerical = 0
    public_string = "String"

    def __init__(
        self,
        address="123 St",
        bike_path_length=11,
        ticket_price=22.11,
        public_numerical=33,
        public_string="str",
    ):
        self.__address = address
        self.__bike_path_length = bike_path_length
        self.__ticket_price = ticket_price
        self.public_numerical = public_numerical
        self.public_string = public_string

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_bike_path_length(self):
        return self.__bike_path_length

    def set_bike_path_length(self, bike_path_length):
        self.__bike_path_length = bike_path_length

    def get_ticket_price(self):
        return self.__ticket_price

    def set_ticket_price(self, ticket_price):
        self.__ticket_price = ticket_price

    def __str__(self):
        return f"Park(Address: {self.__address}, bike paths length: {self.__bike_path_length} meters,- ticket price: {self.__ticket_price} UAH, public Numerical: {self.public_numerical}, public String: {self.public_string})"

    def __repr__(self):
        return f"Park('{self.__address}', '{self.__bike_path_length}', {self.__ticket_price}),'{self.public_numerical}', '{self.public_string}'"

    def __del__(self):
        print(f"Park at {self.__address} has been deleted")


def main():
    park = Park()
    park_1 = Park("456 St", 44, 90.9, 1, "bebebe")
    park_2 = Park("55 St", 55, 66.0, 2, "mememe")
    park_3 = Park("765 St", 66, 77.5, 3, "klm")
    print(park)
    print(park_1)
    print(park_2)
    print(park_3)


if __name__ == "__main__":
    main()


print(Park.public_numerical)
print(Park.public_string)
number = Park()
print(number.public_numerical)
print(number.public_string)