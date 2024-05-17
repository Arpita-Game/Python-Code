class Person:
    def talk(self):
        print("Talk")


class Player(Person):
    def play(self):
        print("Lets Play")


class Captain(Player):
    def captaincy(self):
        print("I'm a captain")


person1 = Person()
person1.talk()
player1 = Player()
player1.play()
player1.talk()
captain1 = Captain()
captain1.captaincy()