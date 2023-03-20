from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class King"""

    def __init__(self, first_name):
        """Init King class"""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, eyes):
        """King method set_eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """King method set_hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """King method get_eyes"""
        return self.eyes

    def get_hairs(self):
        """King method get_hairs"""
        return self.hairs
