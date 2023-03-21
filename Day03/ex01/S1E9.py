from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""
    def __init__(self, first_name):
        """Init Character class"""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = None
        self.eyes = None
        self.hairs = None

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Class Stark"""
    def die(self):
        """Stark method die"""
        self.is_alive = False
