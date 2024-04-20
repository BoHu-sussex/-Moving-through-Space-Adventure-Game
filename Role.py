from Errors import DirectionNotExistError

"""
    Create roles in the game.
"""
class Role:

    def __init__(self, name, description):
        """
        Initialize a role.
        :param name: the name of a role.
        :param description: sentences describing a role.
        """
        self.name = name
        self.description = description

    def show_description(self):
        print(f"\nDescription of {self.name}: {self.description}\n")

class Fighter(Role):

    def __init__(self, name, description, hp, attack):
        """
        Initialize a fighter.
        :param name: the name of a fighter.
        :param description: sentences describing a fighter.
        :param hp: the blood volume of a fighter, a fighter will die if hp <= 0.
        :param attack: the attack value of a fighter, which causes corresponding damage to opponent.
        """
        super().__init__(name, description)
        self.hp = hp
        self.hp_limit = hp
        self.attack = attack
        self.alive = True

    def die(self):
        print(f"Fight over!\n{self.name} is dead!\n")
        self.alive = False
        return True

class Knight(Fighter):
    def __init__(self, name, description, hp, attack, capacity):
        """
        Initialize a knight.
        :param name: the name of a knight.
        :param description: sentences describing a knight.
        :param hp: the blood volume of a knight, a knight will die if hp <= 0.
        :param attack: the attack value of a knight, which causes corresponding damage to monster.
        :param capacity: the max weight of total items in the backpack the knight can afford.
        """
        super().__init__(name, description, hp, attack)
        self.capacity = capacity
        self.backpack = []

    def drop(self, item):
        self.backpack.remove(item)
        return True

    def choose_next_room(self, current_room):

        choose_direction = input("Please choose one to continue your adventure!\n> Enter the `direction` of the room you want to go (text only, case sensitive): ")
        # make sure the direction player entered existing.
        if choose_direction not in current_room.next_rooms.keys():
            raise DirectionNotExistError("Oops! No such direction exists in the current room...\nplease enter again.\n")
        return choose_direction

    def inventory(self):
        print(f"Here are all the items in your backpack: ")
        for item_id, item in enumerate(self.backpack):
            print(f"* id-{item_id + 1}:\n    name: {item.name}\n    description: {item.description}\n    weight: {item.weight}\n    kind: {item.kind}\n    level: {item.level}")

    def increase_attack(self):
        self.attack += 2
        print(f"    * `attack`: {self.attack - 2} ---> {self.attack}")
        return True
    def increase_hp_limit(self):
        self.hp_limit += 2
        print(f"    * `HP`: {self.hp_limit - 2} ---> {self.hp_limit}\n")
        return True

    def increase_capacity(self):
        self.capacity += 2
        print(f"You get stronger!\n    * `capacity`: {self.capacity - 2} ---> {self.capacity}")
        return True

    def current_weight(self):
        s = 0
        for item in self.backpack:
            s += item.weight
        return s


class Monster(Fighter):
    def __init__(self, name, description, hp, attack, growl, level):
        super().__init__(name, description, hp, attack)
        self.growl = growl
        self.level = level

    def make_growl(self):
        return self.growl