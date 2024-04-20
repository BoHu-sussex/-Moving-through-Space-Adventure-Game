import random
import time
from Room import Room
from Role import *
from Reward import Reward
from Errors import *

"""
    This class is the main class of the Project 1. 
    My Project 1 is a game about a knight whose goal is to rescue a princess. 
    The princess is trapped in a big castle which has ten rooms, and each room has a monster. 
    So the player control the knight to fight against the monster at each room. 
    After player defeats a monster in one room, knight can choose a reward and add it to backpack, then choose a next room to go. 
    A reward is a weapon or a potion, which is an item knight can use in the next fight to increase the probability of win. 
    Knight will successfully rescue the princess and win the game after defeating all the ten monsters in each rooms.
"""
class Game:

    def __init__(self):
        """
        Initialize the game.
        1. create all the rewards and monsters.
        2. create all the rooms and each room has its monster and rewards.
        3. `current_room` is the room where player is located now.
        4. create the knight and princess.
        """
        self.create_monsters()
        self.create_rewards()
        self.create_rooms()
        self.visited_rooms = [self.room1] # record the rooms which have been visited already.
        self.current_room = self.visited_rooms[-1]
        self.knight = Knight("", "You are a knight on an adventure to save a princess.", 10, 3, 3)
        self.princess = Role("Lolly", "You are a princess trapped in a castle, waiting to be rescued by a knight")

    def create_monsters(self):
        """
        Create ten monsters for each room.
        :return: None
        """
        self.monster1 = Monster("Witch",
                                "Witches wear black robes and are good at using evil spells to launch attacks.", 4, 1,
                                "Fehfehfehfeh! Interesting young man. Are you ready for dying under my spell?", 1)
        self.monster2 = Monster("Ogre", "The ogre has a large body and sharp claws, and it moves quickly.", 6, 2,
                                "Shahahahaha! I'll tear you to pieces!", 2)
        self.monster3 = Monster("Vampire", "Vampires can fly very fast, and their high-pitched calls are fascinating.",
                                9, 3, "Gegyagyagyagya! I can't wait to taste your blood!", 3)
        self.monster4 = Monster("Night Demon",
                                "A night demon is an evil demon that can ingest your soul if you're not careful.", 12,
                                4, "Gabababababa! I will eat your soul for my snack！", 4)
        self.monster5 = Monster("Dark elf",
                                "Dark elf live underground and have black skin. Although it is small in size, do not underestimate its tricks.",
                                15, 5, "Wiihahahahaha! Self-righteous human beings!", 5)
        self.monster6 = Monster("Werewolf",
                                "A half-human, half-wolf creature usually depicted as taking on the form of a Wolf when the moon is full. They possess great strength and agility, as well as ferocious aggression.",
                                18, 6, "Murufufufufufufu！ I could eat you in one bite!", 6)
        self.monster7 = Monster("Zombie", "A dead body, possessed by evil forces, a slave to the unconscious.", 21, 7,
                                "Wiiwiwiwiwiwi! Come to hell with me!", 7)
        self.monster8 = Monster("Warlock",
                                "Male humans who master dark magic gain power and the ability to control other creatures by learning dark magic and rituals.",
                                24, 8, "Kishishishishishi! I'll cut your eyes out and drink them!", 8)
        self.monster9 = Monster("Ghost",
                                "They usually appear at night or in dark places and are accompanied by a cold and eerie atmosphere.",
                                27, 9, "How can you beat me if you can't even see me?", 9)
        self.monster10 = Monster("Dark Dragon",
                                 "The Dark Dragon is a very powerful evil creature with dark scales and sharp claws. Dark Dragons are usually powerful in attack and magic, capable of spitting fire and creating dark magic.",
                                 30, 10, "Gurararararara！Stupid human!", 10)

    def create_rooms(self):
        """
        1. Create rooms
        2. Add rewards for each room.
        3. Set next rooms for each room.
        :return: None
        """
        # create rooms.
        self.room1 = Room("Castle Kitchen",
                          "It's the kitchen and pantry inside the castle, where the cooks and servants worked.",
                          self.monster1)
        self.room2 = Room("Banquet Hall",
                          "The banqueting Hall in the castle is used for banquets and large dinners, with long tables and ornate decorations.",
                          self.monster2)
        self.room3 = Room("Stable",
                          "The stables in the castle are used to keep horses and other livestock, usually with mangers, feed cabinets, saddles and other horse gear.",
                          self.monster3)
        self.room4 = Room("Castle Hall",
                          "The main meeting place of the castle, located on the first floor of the main castle, was a place for nobles to meet, dine and perform ceremonies. The hall has high ceilings, ornate frescoes and luxurious furniture.",
                          self.monster4)
        self.room5 = Room("Central Stairs",
                          "The central staircase of the castle, one of the main passageways of the castle, leads to the various floors of the castle. The central staircase is located in the center of the main building and can easily connect the various floors.",
                          self.monster5)
        self.room6 = Room("Castle Chapel",
                          "Located near the main castle or in the tower, it was used as a place for nobles to perform religious ceremonies and prayers. There are altars, ICONS, candlesticks and other religious articles in the church.",
                          self.monster6)
        self.room7 = Room("Guard Room",
                          "A place used for guarding soldiers, usually at the entrance to a castle or near a fortification. The guard room usually contains beds, weapons and equipment for soldiers.",
                          self.monster7)
        self.room8 = Room("Castle Library",
                          "Located in a quiet corner of the main castle, it is used for the collection of books, documents and works of art. There are bookshelves, reading tables, chairs and lighting equipment in the study.",
                          self.monster8)
        self.room9 = Room("Castle Wall",
                          "The exterior defensive structure of the castle, made of thick stone or brick, varies in height and thickness according to the size and importance of the castle. The walls were usually topped with battlements and archeries to provide the convenience of defense and attack.",
                          self.monster9)
        self.room10 = Room("State Apartments",
                           "A residence for guests of honour, located on the top floor of the main building. The apartment is richly decorated, with a high level of etiquette and reception atmosphere.",
                           self.monster10)

        # add rewards to each room.
        self.room1.add_rewards(self.weapon1)
        self.room1.add_rewards(self.weapon2)
        self.room2.add_rewards(self.potion1)
        self.room2.add_rewards(self.weapon3)
        self.room3.add_rewards(self.weapon4)
        self.room3.add_rewards(self.potion2)
        self.room4.add_rewards(self.weapon5)
        self.room4.add_rewards(self.weapon6)
        self.room5.add_rewards(self.potion3)
        self.room5.add_rewards(self.weapon7)
        self.room6.add_rewards(self.weapon8)
        self.room6.add_rewards(self.potion4)
        self.room7.add_rewards(self.weapon9)
        self.room7.add_rewards(self.weapon10)
        self.room8.add_rewards(self.potion5)
        self.room8.add_rewards(self.weapon11)
        self.room8.add_rewards(self.potion6)
        self.room9.add_rewards(self.weapon12)
        self.room9.add_rewards(self.weapon13)
        self.room9.add_rewards(self.weapon14)

        # set next rooms for each room.
        self.room1.set_next_room("Behind the door", self.room2)
        self.room1.set_next_room("Outside the window", self.room3)
        self.room2.set_next_room("Outside the left door", self.room3)
        self.room2.set_next_room("Outside the main door", self.room4)
        self.room2.set_next_room("Outside the right door", self.room5)
        self.room3.set_next_room("Over the fence", self.room2)
        self.room3.set_next_room("Outside the window", self.room6)
        self.room4.set_next_room("Outside the left door", self.room7)
        self.room4.set_next_room("Outside the main door", self.room5)
        self.room5.set_next_room("Go up the stair", self.room4)
        self.room5.set_next_room("Go down the stair", self.room6)
        self.room6.set_next_room("Outside the left door", self.room5)
        self.room6.set_next_room("Outside the main door", self.room8)
        self.room7.set_next_room("Outside the left door", self.room9)
        self.room7.set_next_room("Outside the main door", self.room8)
        self.room8.set_next_room("Outside the right door", self.room7)
        self.room8.set_next_room("Outside the main door", self.room9)
        self.room9.set_next_room("Outside the main door", self.room10)

    def create_rewards(self):
        """
        Create rewards for each room.
        :return: None
        """
        # rewards of room1
        self.weapon1 = Reward("British Hunting Knife", "A weapon commonly used by English hunters and adventurers.", 1,
                              "weapon", 1)
        self.potion1 = Reward("Apple flavored potion", "Can restore some of your HP.", 1, "potion", 1)
        # rewards of room2
        self.weapon2 = Reward("Hatchet", "A small axe, usually used for easy carrying.", 2, "weapon", 2)
        self.weapon3 = Reward("Stiletto sword", "A short sword used in Italy with a very thin and sharp blade.", 2,
                              "weapon", 2)
        # rewards of room3
        self.weapon4 = Reward("Tang Sword", "Weapons used during the Tang Dynasty", 3, "weapon", 3)
        self.potion2 = Reward("Tablet", "Can restore some of your HP.", 3, "potion", 3)
        # rewards of room4
        self.weapon5 = Reward("Roman Short sword", "A short sword used in ancient Rome.", 4, "weapon", 4)
        self.weapon6 = Reward("Battle Axe",
                              "A large axe used specifically for combat. The shape and weight of the battle axe are designed to be effective in cutting down enemies in battle.",
                              4, "weapon", 4)
        # rewards of room5
        self.potion3 = Reward("Elixir", "Can restore some of your HP.", 5, "potion", 5)
        self.weapon7 = Reward("Long sword",
                              "A sword used in medieval Europe with a longer blade and a guard between the tip and the handle. ",
                              5, "weapon", 5)
        # rewards of room6
        self.weapon8 = Reward("Longbow",
                              "A traditional English bow and arrow known for its long bow and high shooting power. The long bow has a long range, which can reach more than 300 meters, so it was widely used in the Middle Ages.",
                              6, "weapon", 6)
        self.potion4 = Reward("stimulant",
                              "Can restore some of your HP.", 6,
                              "potion", 6)
        # rewards of room7
        self.weapon9 = Reward("Composite Bow",
                              "A compound bow is a bow made using a number of different materials, usually made from materials such as wood, carbon fiber, fiberglass, and metal. This bow has higher shooting power and better accuracy, which is suitable for use in hunting and fighting.",
                              7, "weapon", 7)
        self.weapon10 = Reward("Recurve Bow",
                               "The recurve bow is a bow with a special shape, whose body bends inward when the string is drawn, forming a 'C' shape. This bow has higher shooting power and better accuracy, which is suitable for use in competitions and hunting.",
                               7, "weapon", 7)
        # rewards of room8
        self.potion5 = Reward("Pill", "Can restore some of your HP.", 8, "potion", 8)
        self.weapon11 = Reward("Crossbow",
                               "A crossbow is a bow and arrow that uses a mechanical device to draw the strings, usually made of materials such as wood, metal, and leather. This bow and arrow can be aimed and fired without the use of manpower, so it has higher accuracy and longer range. Crossbows were widely used in Europe during the Middle Ages, especially in castles and city defenses.",
                               8, "weapon", 8)
        self.potion6 = Reward("Ointment", "Can restore some of your HP", 8, "potion", 9)
        # rewards of room9
        self.weapon12 = Reward("War Hammer",
                               "A war hammer is a common European mace, usually made of iron or steel, with a sharp hammer head and a longer grip. The hammer can be used for both melee and throwing.",
                               9, "weapon", 9)
        self.weapon13 = Reward("Berken hatchet",
                               "The Berken hatchet is a French mace with a wide axe and a longer grip. Its axe part is decorated with metal spikes or bulges to increase the force of damage.",
                               9, "weapon", 10)
        self.weapon14 = Reward("Bomb",
                               "It's powerful enough to do a lot of damage at once. But it's heavy and can only be used once.",
                               9, "weapon", 10)

    def fight(self):
        """
        The process of a fight in one room. A fight may include many rounds.
        At a fight, the knight can:
        1. inventory backpack before fight if backpack is not empty.
        2. choose an item before each fight round.
        3. the item make effect.
        4. loop the fight until knight dies or monster dies.
        :return: None
        """
        fight_round = 1
        input("(Enter whatever to continue the game...)")
        print(f"Monster {self.current_room.monster.name}: {self.current_room.monster.make_growl()} \n")

        # inventory backpack if not empty.
        if not self.knight.backpack:
            print(f"{self.knight.name} now your backpack is empty.\nSo you have to fight with the Monster {self.current_room.monster.name} without weapon.\nAfter you triumph the Monster {self.current_room.monster.name}, you will get a reward.\n")

            # player can choose to continue the game or look up to help tips.
            input("(Enter whatever to continue the game...)")
            # is_ready = input("> Enter 'y' if you are ready to fight, enter 'help' to get some helps: ")
            # if is_ready == 'help':
            #     self.show_helps()
        else:
            # Inventory backpack.
            check1 = input(f"> Enter 'y' to inventory your backpack: ")
            if check1 == 'y':
                self.knight.inventory()

        # input("(Enter whatever to continue the game...)")

        time.sleep(1)

        # the fight begin. fight will continue until the knight or monster dies.
        print('-----FIGHT BEGIN!-----')

        time.sleep(1)

        while self.knight.hp > 0 and self.current_room.monster.hp > 0:
            print(f"\nRound {fight_round}")

            # Choose a weapon or a potion.
            if self.knight.backpack:
                print(f"{self.knight.name} please choose one in your backpack in this round.\n")

                # make sure one item in the backpack is chosen.
                while True:
                    try:
                        choose_id = int(input("> Enter the id number of the item you want to use in this round: ")) - 1
                        if choose_id not in range(len(self.knight.backpack)):
                            raise ItemIdNotExistError(f"No such item id in your backpack, please enter again.\n")
                        item = self.knight.backpack[choose_id]
                        break
                    except ItemIdNotExistError:
                        pass
                    except ValueError:
                        print("Oops! You must enter an int number\n")
                        pass

                # the item makes effect and the effect depends on the kind of each item.
                if item.kind == 'potion':
                    # restore some HP.
                    hp_before_knight = self.knight.hp # record the HP before using the potion.
                    self.knight.hp = min(self.knight.hp_limit, self.knight.hp + random.randint(item.level, item.level * 2))

                    hp_before_monster = self.current_room.monster.hp
                    self.current_room.monster.hp -= random.randint(1, self.knight.attack)

                    print(f"{self.knight.name} use the potion `{item.name}`.\n    HP of {self.knight.name}: {hp_before_knight} ---> {self.knight.hp}")
                    print(f"Without weapon {self.knight.name} causes some damage on the Monster {self.current_room.monster.name}.\n    HP of Monster {self.current_room.monster.name}: {hp_before_monster} ---> {max(0, self.current_room.monster.hp)}")

                else:
                    # cause the hp of monster decreased.
                    attack = random.randint(item.level, item.level + self.knight.attack)
                    hp_before = self.current_room.monster.hp
                    self.current_room.monster.hp -= attack
                    print(f"{self.knight.name} use the weapon `{item.name}`.\n    HP of Monster {self.current_room.monster.name}: {hp_before} ---> {max(0, self.current_room.monster.hp)}")

                time.sleep(1)

                if self.current_room.monster.hp > 0:
                    # knight suffers damage caused by monster.
                    hp_before = self.knight.hp
                    self.knight.hp -= self.current_room.monster.attack
                    print(f"Monster {self.current_room.monster.name} causes {self.current_room.monster.attack} damage on {self.knight.name}.\n    HP of {self.knight.name}: {hp_before} ---> {max(0, self.knight.hp)}\n")
            # if backpack is empty, knight have to fight without weapon.
            else:
                hp_before = self.current_room.monster.hp
                self.current_room.monster.hp -= self.knight.attack
                print(f"{self.knight.name} causes {self.knight.attack} damage on the Monster {self.current_room.monster.name}.\n    HP of Monster {self.current_room.monster.name}: {hp_before} ---> {max(0, self.current_room.monster.hp)}")
                if self.current_room.monster.hp > 0:
                    hp_before = self.knight.hp
                    self.knight.hp -= self.current_room.monster.attack
                    # print(f"Monster {self.current_room.monster.name} causes {self.current_room.monster.attack} damage on the Knight {self.knight.name}. Now the Knight {self.knight.name}'s HP is {max(0, self.knight.hp)}\n")
                    print(f"Monster {self.current_room.monster.name} causes {self.current_room.monster.attack} damage on {self.knight.name}.\n    HP of {self.knight.name}: {hp_before} ---> {max(0, self.knight.hp)}\n")
            time.sleep(1)

            # the fight round increases 1
            fight_round += 1

        # time.sleep(1)

        # fight end. knight dies or monster dies.
        print("-----FIGHT END!-----")
        input("(Enter whatever to continue the game...)")
        if self.knight.hp <= 0:
            self.knight.die()
        else:
            self.current_room.monster.die()

    def play(self):
        """
        1. check whether the room is already passed.
        2. initialise the fight.
        3. execute the fight.
        4. knight can have capacity, attack and hp increased if winning the room. besides player can choose one reward.
        5. player can choose next room to continue adventure.
        6. return back to the last room if player loses the fight of this room.
        :return: None
        """
        print(f"\n     Location: {self.current_room.name}     \n")

        # fight with the monster of current room if this room is not passed yet.
        if not self.current_room.is_win:

            time.sleep(1)

            print(f"Pay attention {self.knight.name}!!!\nNow you are at {self.current_room.name}.\n"
                  f"Description of {self.current_room.name}: {self.current_room.show_description()}"
                  f"\nYou will encounter the Monster {self.current_room.monster.name}.", end='')
            self.current_room.monster.show_description()

            # initialise the fight.
            self.knight.hp = self.knight.hp_limit
            self.knight.alive = True
            self.current_room.monster.hp = self.current_room.monster.hp_limit

            # fight
            self.fight()

            # check whether the big boss is defeated and player wins the game.
            if not self.monster10.alive:
                return

            # player wins the room if knight defeats the monster.
            if self.knight.alive:
                self.current_room.is_win = True
                # increase the capacity, attack value and hp value of knight.
                self.knight.increase_capacity()
                self.knight.increase_attack()
                self.knight.increase_hp_limit()

                input("(Enter whatever to continue the game...)")

                time.sleep(1)

                # knight can choose a reward to fill backpack after winning the room.
                print("-----Choose a reward-----")
                self.current_room.show_rewards()
                print(f"\nNow you can choose a reward and add it to your backpack.\nPlease note that each reward has its weight and now your capacity is {self.knight.capacity}")

                # make sure one of the rewards is chosen.
                while True:
                    try:
                        reward_id = int(input(f"> Enter the id of reward you want: ")) - 1
                        if reward_id not in range(len(self.current_room.rewards)):
                            raise RewardIdNotExistError("No such reward id in the rewards list, please enter again.")

                        # add the reward to backpack.
                        self.knight.backpack.append(self.current_room.rewards[reward_id])
                        print(f"\nYou choose the {self.current_room.rewards[reward_id].name}. ", end='')
                        break
                    except RewardIdNotExistError:
                        pass
                    except ValueError:
                        print("Oops! You must enter an int number")
                        pass

                # if the total weight of items in backpack is greater than knight's capacity, player have to throw some items in backpack.
                while self.knight.capacity < self.knight.current_weight():
                    print("Oops! Your backpack has no enough space, you must drop one item. ")
                    # list all the items in backpack.
                    self.knight.inventory()

                    # make sure one item in backpack is dropped.
                    while True:
                        try:
                            drop_id = int(input(f"> Enter the id of item you want to drop: ")) - 1
                            if drop_id not in range(len(self.knight.backpack)):
                                raise ItemIdNotExistError(f"No such item id in your backpack, please enter again.")
                            self.knight.drop(self.knight.backpack[drop_id])
                            break
                        except ItemIdNotExistError:
                            pass
                        except ValueError:
                            print("Oops! You must enter an int number")
                            pass

                    print(f"You drop the `{self.knight.backpack[drop_id - 1].name}`")

                print(f"\nNow your total weight: {self.knight.current_weight()}\nNow your capacity: {self.knight.capacity}\n")

                # Choose the next room to go.
                print("-----Choose next room-----\n")

                time.sleep(1)

                self.current_room.show_next_rooms()

                # make sure one of the next rooms is chosen.
                while True:
                    try:
                        choose_direction = self.knight.choose_next_room(self.current_room)
                        # updating the current room.
                        self.current_room = self.current_room.next_rooms[choose_direction]
                        self.visited_rooms.append(self.current_room)
                        break
                    except DirectionNotExistError:
                        pass

            # return back to the last room if fail the fight.
            else:
                print(f"Sorry...The Monster {self.current_room.monster.name} is too hard to defeat...\n")
                self.visited_rooms.pop()
                print(f"You return back last room {self.visited_rooms[-1].name}. \n")
                self.current_room = self.visited_rooms[-1]
                input("(Enter whatever to continue the game...)")

        # just take this room as a transfer station.
        else:
            print("Emmm...This room has nothing left, please choose another room to continue your adventure.\n")
            self.current_room.show_next_rooms()

            # make sure one of the next rooms is chosen.
            while True:
                try:
                    choose_direction = self.knight.choose_next_room(self.current_room)
                    print(f"You leave the room {self.current_room.name}\n\n")
                    self.current_room = self.current_room.next_rooms[choose_direction]
                    break
                except DirectionNotExistError:
                    pass

            # updating the list of visited rooms.
            if self.current_room not in self.visited_rooms:
                self.visited_rooms.append(self.current_room)

    def welcome(self):
        """
        Show some welcome information.
        :return: None
        """
        print(f"Once upon a time there was a princess named {self.princess.name}.")


        time.sleep(1)

        print(f"Unluckily she was trapped in a castle where is occupied by ten evil monsters.")

        time.sleep(1)

        print(f"Now {self.knight.description}")

        time.sleep(1)

        print(f"Each monster stays in a room so you must go to each room and defeat the monster there.\n")

        time.sleep(1)
        while not self.knight.name:
            self.knight.name = input("> Please enter your name: ")
            if not self.knight.name:
                print("You have to enter a name!")
        print("\n-----GAME START-----\n")

    def show_helps(self):
        print("Feel confused?\nNow your backpack is empty so you have to fight against monster without weapon.\nAfter you win you can choose a weapon or a potion!\nDon't worry, this fight will be easy.")

    def you_win(self):
        print(f"The final Boss is defeated and you WIN the Game!!!!\nThe princess {self.princess.name} is safe now!\nKnight {self.knight.name} you are absolutely a hero!")
        input("(Enter whatever to quit the game...)")

def main():
    game = Game()
    game.welcome()
    # loop the game until the final monster is defeated.
    while game.monster10.alive:
        game.play()
    game.you_win()

if __name__ == "__main__":
    main()