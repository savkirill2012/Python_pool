import random


def turrets_generator():
    def turret_init(self):
        total = 100
        for elem in ["neuroticism", "openness",
                     "conscientiousness", "extraversion",
                     "agreeableness"]:
            if elem == "agreeableness":
                setattr(self, elem, total)
            else:
                r_val = int(random.random() * total)
                setattr(self, elem, r_val)
                total -= r_val

    def shoot(self):
        print("Shooting")

    def search(self):
        print("Searching")

    def talk(self):
        print("Talking")

    return type("Turret", (), {"__init__": turret_init, "talk": talk,
                               "search": search, "shoot": shoot})


if __name__ == "__main__":
    Turret = turrets_generator()
    new_test = Turret()
    new_test2 = Turret()
    print(new_test.neuroticism)
    print(new_test.openness)
    print(new_test.conscientiousness)
    print(new_test.extraversion)
    print(new_test.agreeableness)
    new_test.talk()
    new_test.shoot()
    new_test.search()
    print()
    print(new_test2.neuroticism)
    print(new_test2.openness)
    print(new_test2.conscientiousness)
    print(new_test2.extraversion)
    print(new_test2.agreeableness)
