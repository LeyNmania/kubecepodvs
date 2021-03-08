from typing import List


class Lane:

    def __init__(self, id_, length, shape):
        self._id = str(id_)
        self._length = float(length)
        self._shape = str(shape).split(' ')
        self._x = 0.0
        self._y = 0.0

    def get_id(self) -> str:
        return self._id

    def get_length(self) -> float:
        return self._length

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_shape(self) -> List[str]:
        return self._shape

    def set_x(self, x):
        self._x = float(x)

    def set_y(self, y):
        self._y = float(y)
