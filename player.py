from random import shuffle

action_list = [
        'Income','Foreign Aid', 'Coup', 'Tax',
        'Assesinate', 'Exchange', 'Steal'
        ]

p1_characters = []
p2_characters = []
p3_characters = []

character_list = [
        'duke', 'assassin', 'ambassador', 'captain', 'contessa',
        'duke', 'assassin', 'ambassador', 'captain', 'contessa',
        'duke', 'assassin', 'ambassador', 'captain', 'contessa'
        ]

p1_money = 2
p2_money = 2
p3_money = 2

p1_deck = [p1_characters,p1_money]
p2_deck = [p2_characters,p2_money]
p3_deck = [p3_characters,p3_money]


class Player:
    def character(self):
        shuffle(character_list)
        character = character_list[0]
        character_list.remove(character)
        return character


p1 = Player()
p1_characters.append(p1.character())
p1_characters.append(p1.character())
#print(p1_characters)

p2 = Player()
p2_characters.append(p2.character())
p2_characters.append(p2.character())
#print(p2_characters)

p3 = Player()
p3_characters.append(p3.character())
p3_characters.append(p3.character())
#print(p3_characters)

#print(character_list)
print(p1_deck)
print(p2_deck)
print(p3_deck)