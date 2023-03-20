from S1E9 import Character


class Baratheon(Character):
    """Class Baratheon"""

    def __init__(self, first_name):
        """Init Baratheon class"""

        self.first_name = first_name
        self.is_alive = True
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector {self.first_name, self.eyes, self.hairs}"

    def __repr__(self):
        return f"Vector {self.first_name, self.eyes, self.hairs}"

    def die(self):
        """Baratheon method die"""

        self.is_alive = False


class Lannister(Character):
    """Class Lannister"""

    def __init__(self, first_name):
        """Init Lannister class"""

        self.first_name = first_name
        self.is_alive = True
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
        self.__str__()

    def __str__(self):
        return f"Vector {self.first_name, self.eyes, self.hairs}"

    def __repr__(self):
        return f"Vector {self.first_name, self.eyes, self.hairs}"

    def die(self):
        """Lannister method die"""
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, bool):
        """Lannister method create_lannister"""
        c = Lannister(first_name)
        return c
