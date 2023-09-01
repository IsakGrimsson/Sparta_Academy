print("\nQ1a\n")
# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class county():
    def __init__(self,name,continent,climate,language,population,gdp):
        self._name = name
        self._continent = continent
        self._language = language
        self._climate = climate
        self._population = population
        self._gdp = gdp

    def print(self):
        print(f'{self._name}')


print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
class city():
    def __init__(self,name,continent,climate,language,population,gdp,city_center):
        self._city_center = city_center
        super().__init__(name,continent,climate,language,population,gdp)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]

class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False

# A2a:

list_of_prime_numbers = []
for num in list_of_numbers:
    new_number_object = Number(num)
    if new_number_object.is_prime():
        list_of_prime_numbers.append(num)
print(list_of_prime_numbers)


print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
list_of_divisible_numbers = []
for num in list_of_numbers:
    new_number_object = Number(num)
    if new_number_object.divisible_by_n(3):
        if new_number_object.divisible_by_n(4):
            list_of_divisible_numbers.append(num)
print(list_of_divisible_numbers)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
       print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:


# -------------------------------------------------------------------------------------- #






