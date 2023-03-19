from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""
    def __init__(self, first_name):
        """Init Character class"""
        self.first_name = first_name
        self.is_alive = True

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """A subclass of Character representing the Stark family in the game."""
    def die(self):
        """Stark method die"""
        self.is_alive = False
