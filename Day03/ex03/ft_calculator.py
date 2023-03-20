class calculator:
    """Calculator class"""
    def __init__(self, list):
        """Init calculator class"""
        self.list = list

    def __add__(self, object) -> None:
        """Add method"""
        self.list = [x + object for x in self.list]
        print(self.list)

    def __mul__(self, object) -> None:
        """Mul method"""
        self.list = [x * object for x in self.list]
        print(self.list)

    def __sub__(self, object) -> None:
        """Sub method"""
        self.list = [x - object for x in self.list]
        print(self.list)

    def __truediv__(self, object) -> None:
        """Div method"""
        try:
            if object == 0:
                raise ValueError("Can't divide by 0")
        except ValueError as e:
            print("ValueError:", e)
            exit()
        self.list = [x / object for x in self.list]
        print(self.list)
