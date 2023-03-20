class calculator:
    """Calculator class"""

    def __init__(self, list):
        """Init calculator class"""
        self.list = list

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of two vectors"""
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print("Dot product is :", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors"""
        tmp1 = V1.copy()
        tmp2 = V2.copy()
        for i in range(len(tmp1)):
            tmp1[i] += tmp2[i]
        tmp1 = [float(i) for i in tmp1]
        print("Add Vector is :", tmp1)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Sous two vectors"""
        tmp1 = V1.copy()
        tmp2 = V2.copy()
        for i in range(len(tmp1)):
            tmp1[i] -= tmp2[i]
        tmp1 = [float(i) for i in tmp1]
        print("Sous Vector is:", tmp1)
