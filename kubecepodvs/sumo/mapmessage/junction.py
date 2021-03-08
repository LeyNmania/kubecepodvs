from typing import List


class Junction:

    def __init__(self, id_, x, y, incLanes1, incLanes2, shape):
        self._id = str(id_)
        self._x = float(x)
        self._y = float(y)
        self._incLanes = str(incLanes1).split(
            ' ').extend(str(incLanes2).split(' '))
        self._shape = str(shape).split(' ')

    def get_id(self) -> str:
        return self._id

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_incLanes(self) -> List[str]:
        return self._incLanes

    def get_shape(self) -> List[str]:
        return self._shape
