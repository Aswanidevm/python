#encapsulation
#abstraction
#inheritance
#polymorpism many forms

class User():
    def sign_in(self):
        print("Logged in")
    def attack():
        print("nothing")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack()
        print(f"the power of Wizard {self.name} is {self.power}")


class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f"the power of Archer {self.name} is arrow with remaing {self.num_arrow}")


wizard1 = Wizard("latha", "curse")
archer1 = Archer("kedar", 30)

print(wizard1.name)
wizard1.sign_in()
wizard1.attack()

print(archer1.name)
archer1.sign_in()
archer1.attack()

print(isinstance(archer1, User))