class Park:
    public_numerical = 0
    public_string = "String"
    
    def __init__(self, address = "123 St", bike_path_length = 11, ticket_price = 22.11, public_numerical = 33, public_string = "str"):
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
        return (f"Park(Address: {self.__address}, bike paths length: {self.__bike_path_length} meters,- ticket price: {self.__ticket_price} UAH, public Numerical: {self.public_numerical}, public String: {self.public_string})")

    def __repr__(self):
        return (f"Park('{self.__address}', '{self.__bike_path_length}', {self.__ticket_price}),'{self.public_numerical}', '{self.public_string}'")

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


# class Puzzle:
#     public_numerical45 = 0
#     public_string45 = "str"
    
#     def __init__(self, description="bebebe", count_of_elements=100, width_of_the_box=50, height_of_the_box=80, public_numerical45=99, public_string45="abc"):
#         self.__description = description
#         self.__count_of_elements = count_of_elements
#         self.__width_of_the_box = width_of_the_box
#         self.__height_of_the_box = height_of_the_box
#         self.public_numerical45 = public_numerical45
#         self.public_string45 = public_string45

#     def get_description(self):
#         return self.__description
    
#     def set_description(self, description):
#         self.__description = description

#     def get_count_of_elements(self):
#         return self.__count_of_elements
    
#     def set_count_of_elements(self, count_of_elements):
#         self.__count_of_elements = count_of_elements

#     def get_width_of_the_box(self):
#         return self.__width_of_the_box
    
#     def set_width_of_the_box(self, width_of_the_box):
#         self.__width_of_the_box = width_of_the_box

#     def get_height_of_the_box(self):
#         return self.__height_of_the_box

#     def set_height_of_the_box(self, height_of_the_box):
#         self.__height_of_the_box = height_of_the_box

#     def __str__(self):
#         return (f"Puzzle(description: {self.__description}, count_of_elements: {self.__count_of_elements}, width_of_the_box: {self.__width_of_the_box}, height_of_the_box: {self.__height_of_the_box}, public_numerical: {self.public_numerical45}, public_string: {self.public_string45})")

#     def __repr__(self):
#         return (f"Puzzle('{self.__description}', {self.__count_of_elements}, {self.__width_of_the_box}, {self.__height_of_the_box}, {self.public_numerical45}, {self.public_string45})")

#     def __del__(self):
#         print(f"Puzzle {self.__description} has been deleted")


# def main():
#     puzzle = Puzzle()
#     puzzle_1 = Puzzle("asd", 11, 22, 33, 44, "qwe")
#     puzzle_2 = Puzzle("zxc", 12, 23, 34, 45, "cvb")
#     puzzle_3 = Puzzle("fgh", 23, 56, 67, 78, "mem")
#     print(puzzle)
#     print(puzzle_1)
#     print(puzzle_2)
#     print(puzzle_3)


# class Turtle:
#     public_numerical77 = 0
#     public_string77 = "hjkl"

#     def __init__(self, scientific_name = "hjk", movement_speed_in_water = 90, mass = 50):
#         self.__scientific_name = scientific_name
#         self.__movement_speed_in_water = movement_speed_in_water
#         self.__mass = mass

#     def get_scientific_name(self):
#         return self.__scientific_name

#     def set_scientific_name(self, scientific_name):
#         self.__scientific_name = scientific_name

#     def get_movement_speed_in_water(self):
#         return self.__movement_speed_in_water
    
#     def set_movement_speed_in_water(self, movement_speed_in_water):
#         self.__movement_speed_in_water = movement_speed_in_water

#     def get_mass(self):
#         return self.__mass
    
#     def set_mass(self, mass):
#         self.__mass = mass

#     def __str__(self):
#         return (f"Turtle(scientific_name: {self.__scientific_name}, movement_speed_in_water: {self.__movement_speed_in_water}, mass: {self.__mass})")
    
#     def __repr__(self):
#         return (f"Turtle('{self.__scientific_name}', {self.__movement_speed_in_water}, {self.__mass})")
    
#     def __del__(self):
#         print(f"Turtle {self.__scientific_name} has been deleted")

#     def main():
#         turtle = Turtle()
#         turtle_1 = Turtle("ghjkl", 10, 20)
#         turtle_2 = Turtle("lokjhb", 23, 65)
#         turtle_3 = Turtle("dfghj", 44, 55)
#         print(turtle)
#         print(turtle_1)
#         print(turtle_2)
#         print(turtle_3)

# if __name__== "__main__":
#     main()