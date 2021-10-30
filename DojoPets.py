
class Ninjas:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pets("guido","type2","alot",100,100)
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.walk()
        print(self.pet.health)

    def feed():
        pass

    def bathe():
        pass

class Pets(Ninjas):
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print("au au au au au!")







Leo = Ninjas("lEO","Silva","cute","wiskas","food")
Leo.walk()
