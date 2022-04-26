from pydantic.dataclasses import dataclass
from math import pow, sqrt


class SumException(Exception):
    """raised when vectors can not be sum"""
    pass


class MulException(Exception):
    """raised when vectors can not be mul"""
    pass


@dataclass
class Point:
    x: float
    y: float
    z: float


class Vector:
    EXC_INFO_MUL = "You can't mul these vectors, try to transfer them in one point"
    EXC_INFO_SUM = "You can't sum these vectors, try to transfer them in one point"

    # def __init__(self, start, end):
    #     self.start = {
    #         'x': start.x,
    #         'y': start.y,
    #         'z': start.z
    #     }
    #     self.end = {
    #         'x': end.x,
    #         'y': end.y,
    #         'z': end.z,
    #     }
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def length(self):
        return sqrt(pow(self.end.x - self.start.x, 2) + pow(self.end.y - self.start.y, 2)
                    + pow(self.end.z - self.start.z, 2))

    def parallel_transfer(self):
        self.end.x -= self.start.x
        self.end.y -= self.start.y
        self.end.z -= self.start.z
        self.start.x = 0.0
        self.start.y = 0.0
        self.start.z = 0.0

    def possibility_to_sum(self, other):
        if self.start == other.start:
            return True
        else:
            return False

    def possibility_to_mul(self, other):
        if self.start == other.start:
            return True
        else:
            return False

    def __add__(self, other):
        """Summarize two vectors"""
        if self.possibility_to_sum(other) is True:
            end_point = Point(self.end.x + other.end.x, self.end.y + other.end.y,
                              self.end.z + other.end.z)
            return Vector(self.start, end_point)
        else:
            raise SumException(self.EXC_INFO_SUM)

    def scalar_mul(self, other):
        pass

    def __mul__(self, other):
        if self.possibility_to_mul(other) is True:
            end_point = Point(self.end.y * other.end.z - self.end.z * other.end.y,
                              -(self.end.x * other.end.z - self.end.z * other.end.x),
                              self.end.x * other.end.y - self.end.y * other.end.x)
            return Vector(self.start, end_point)
        else:
            raise MulException(self.EXC_INFO_MUL)

# p1 = Point(0, 0, 0)
# p2 = Point(1, 2, 3)
# p3 = Point(0, 0, 0)
# p4 = Point(4, 5, 6)
# v1 = Vector(p1, p2)
# print(vars(v1))
# v1.parallel_transfer()
# print(vars(v1))
# v2 = Vector(p3, p4)
# v3 = v2 + v1
# print(vars(v3))
# v4 = v1 * v2
# print(vars(v4))
# print(v1.possibility_to_sum(v2))
# print(v1.possibility_to_mul(v2))
# print(v1.length())
