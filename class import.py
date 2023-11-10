class Ultrakill_character:

    def __init__(self, name, hp, ):
        self.name = name
        self.hp = 1

class King_Minos(Ultrakill_character):  #    Minos Prime
    def __init__(self, name):
        super().__init__(name, hp)


class Judge_of_Hell(Ultrakill_character):   #    Gabriel
    def __init__(self, name):
        super().__init__(name, hp)


class Supreme_Machine(Ultrakill_character):    #   V1, V2
    def __init__(self, name):
        super().__init__(name, hp)


class Greater_Machine(Ultrakill_character):    #    Swordsmachine
    def __init__(self, name):
        super().__init__(name, hp)

    print(f'{__name__=}')

    if __name__ == '__main__':
        person1 = King_Minos('Minos Prime')
        person2 = Judge_of_Hell('Gabriel')
        person3 = Supreme_Machine('V2')
        person4 = Greater_Machine('Swordsmachine')


#class Apostate_of_Hate(Ultrakill_character):    #   Gabriel_p2
