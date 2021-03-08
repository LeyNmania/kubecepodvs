from kubecepodvs.sumo.mapmessage.lane import Lane
from kubecepodvs.sumo.mapmessage.junction import Junction
from typing import Dict, List


class Edge:

    def __init__(self, id_):
        self._id = str(id_)
        self._from = ''
        self._to = ''
        self._fromX = 0.0
        self._fromY = 0.0
        self._toX = 0.0
        self._toY = 0.0
        self._lanes = {}
        self._junctions = []

    def add_lanes(self, id_, lane: Lane):
        self._lanes[str(id_)] = lane
        shape = lane.get_shape()[0]
        init_pos = shape.split(',')
        self._fromX = float(init_pos[0])
        self._fromY = float(init_pos[1])

    def get_id(self) -> str:
        return self._id

    def get_lane(self, id_) -> Lane:
        return self._lanes[str(id_)]

    def get_lanes(self) -> Dict[str, Lane]:
        return self._lanes

    def get_from(self) -> str:
        return self._from

    def set_from(self, from_):
        self._from = str(from_)

    def get_to(self) -> str:
        return self._to

    def set_to(self, to):
        self._to = str(to)

    def get_fromX(self) -> float:
        return self._fromX

    def set_fromX(self, fromX):
        self._fromX = float(fromX)

    def get_fromY(self) -> float:
        return self._fromY

    def set_fromY(self, fromY):
        self._fromY = float(fromY)

    def get_toX(self) -> float:
        return self._toX

    def set_toX(self, toX):
        self._toX = float(toX)

    def get_toY(self) -> float:
        return self._toY

    def set_toY(self, toY):
        self._toY = float(toY)

    def add_junction(self, junction: Junction):
        self._junctions.append(junction)

    def get_junctions(self) -> List[Junction]:
        return self._junctions
