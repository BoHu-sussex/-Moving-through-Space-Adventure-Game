"""
    The three classes below create some error type to implement the exception handling.
"""
class ItemIdNotExistError(Exception):
    def __init__(self, message):
        print("Oops! " + message)

class RewardIdNotExistError(Exception):
    def __init__(self, message):
        print("Oops! " + message)

class DirectionNotExistError(Exception):
    def __init__(self, message):
        print(message)