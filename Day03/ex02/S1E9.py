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

    @classmethod
    def __str__(self):
        return f"<bound method Baratheon.__str__ of Vector:  \
        ({__class__.first_name, {__class__.eyes}, {__class__.hairs}})>"


class Stark(Character):
    """Class Stark"""
    def die(self):
        """Stark method die"""
        self.is_alive = False
