#encapsulation
#abstraction
#inheritance
#polymorpism many forms

class User():
    # def __init__(self, email):
    #     self.email = email
    #     # print(email)
    def sign_in(self):
        print("Logged in")
    def attack():
        print("nothing")

class Wizard(User):
    def __init__(self, name, power):
        # User.__init__(self, email)
        # super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack()
        print(f"the power of Wizard {self.name} is {self.power}")


class Archer(User):
    
    def __init__(self, name, num_arrow):
        # User.__init__(self, email)
        # super().__init__(email)
        self.name = name
        self.num_arrow = num_arrow

    def attacck(self):
        print(f"the power of Archer {self.name} is arrow with remaing {self.num_arrow}")


wizard1 = Wizard("latha", "curse")
archer1 = Archer("kedar", 30)

# print(wizard1.name)
# wizard1.sign_in()
# wizard1.attack()

# print(archer1.name)
# archer1.sign_in()
# archer1.attack()

# print(isinstance(archer1, User))
# print(archer1.email)
def ataack(char):
    print(f"Hello {char.name}")
    char.sign_in()
    char.attack()
#     char.email
    # print(f"Email id of {char.name} is {char.email}")

# ataack(wizard1)
# ataack(archer1)

#multiple inheritance

class Hybrid(Wizard, Archer):
    def __init__(self, name, power, num_arrow):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrow)

hy = Hybrid("aswa", 30, 32)
hy.attack()