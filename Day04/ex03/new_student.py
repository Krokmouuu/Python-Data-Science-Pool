import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student class"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = f"{self.name[0]}{self.surname}".lower()
        self.id = generate_id()
