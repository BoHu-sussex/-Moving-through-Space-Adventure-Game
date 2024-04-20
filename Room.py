"""
    Create a room.
"""

class Room:

    def __init__(self, name, description, monster):
        """
        Initialize the room.
        :param name: the name of the room.
        :param description: some sentences describing the room.
        :param monster: the monster stays in the room.
        """
        self.name = name
        self.description = description
        self.monster = monster
        # the rewards list in the room.
        self.rewards = []
        # the dictionary of all the next rooms of this room and their directions.
        self.next_rooms = {}
        # label if player has won this room already.
        self.is_win = False

    def set_next_room(self, direction, next_room):
        """
        Set next rooms for this room. The next room is a dictionary, the `key` is the direction and the `value` is the corresponding next room.
        :param direction: the direction of the next room.
        :param next_room: one next room of this room.
        :return: None
        """
        self.next_rooms[direction] = next_room

    def show_next_rooms(self):
        # print(f"Because the monster in room {self.name} is defeated, you can go to next room now. here are the next rooms and their directions:")
        print(f"Here are the neighbor rooms...")
        room_id = 1
        for direction, room in self.next_rooms.items():
            if room.is_win:
                message = "(You have already won this room.)"
            else:
                message = "(You have not won this room yet.)"
            print(f"* id-{room_id}:\n    Direction: `{direction}`\n    Next room: `{room.name}`\n    {message} ")
            room_id += 1

    def add_rewards(self, reward):
        """
        Add rewards to a room.
        :param reward: an item to be added.
        :return: None
        """
        self.rewards.append(reward)

    def show_rewards(self):

        print(f"Congratulation! You triumph the Monster {self.monster.name}. Here is the list of rewards:")
        # show the items in a room.
        for reward_id, reward in enumerate(self.rewards):
            print(f"* id-{reward_id + 1}: ")
            print(f"    name: {reward.name}\n    description: {reward.description}\n    weight: {reward.weight}\n    kind: {reward.kind}\n    level: {reward.level}")

    def show_description(self):
        return self.description