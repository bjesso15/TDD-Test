import unittest
from animal import Animal

class Test_animal(unittest.TestCase):
    def test_animal_cat(self):
        animal1 = Animal("cat")
        self.assertEqual(animal1.name, "Seymour")


    def test_animal_dog(self):
        animal2 = Animal("dog")
        self.assertEqual(animal2.name, "Spot")

    def test_animal_name(self):
        animal3 = Animal()
        self.assertEqual(animal3.name, Animal.name)

    def test_animal_type_and_size(self):
        animal4 = Animal("cat")
        if animal4.size == "small":
            self.assertEqual(animal4.speak(), "meow")
        else:
            self.assertEqual(animal4.speak(), "MEOW!")

    def test_animal_type_and_size1(self):
        animal5 = Animal("dog")
        if animal5.size == "small":
            self.assertEqual(animal5.speak(), "bow wow")
        elif animal5.size == "medium":
            self.assertEqual(animal5.speak(), "Ruff ruff")
        elif animal5.size == "large":
            self.assertEqual(animal5.speak(), "arf arf")

    def test_animal_age(self):
        animal6 = Animal()
        if animal6.age < 10:
            self.assertEqual(animal6.describe(), Animal.name + "is young")
        elif animal6.age > 10:
            self.assertEqual(animal6.describe(), Animal.name + "is old")

    