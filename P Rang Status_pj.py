class Ultrakill_character:
    def __init__(self, name, hp, ):
        self.name = name
        self.hp = 1


    #def salutation_Minos(self):
    #    print(f'{self.name} Ahh… Free at last. O Gabriel. Now dawns thy reckoning, and thy gore shall glisten before the temples '
    #        'of man. Creature of steel… My gratitude upon thee for my freedom, but the crimes thy kind have'
    #        ' committed against humanity are NOT forgotten. And thy punishment… is DEATH.')
    #def salutation_V2(self):
    #        print(f'{self.name} 110010011010011100101')
    #def salutation_Gabriel(self):
    #        print(f'{self.name} Machine, turn back now. The layers of this palace are not for your kind. Turn back, or you will be'
    #              ' crossing the will of God' + ' ...Your choice is made..')


    def punch_reaction(self):
        pass


    def punch(self, other, hp):
        if hp <= 0:
            print("Can't punch, character is already dead")
        else:
             other.hp -= 1
        if other.hp <= 0:
#            punch_reaction


    def ordering(self):
        pass
    #    if hp = max:
    #        salution()
    #    other = name


