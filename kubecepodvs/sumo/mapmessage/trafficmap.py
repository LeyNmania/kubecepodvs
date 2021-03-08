from kubecepodvs.sumo.mapmessage.junction import Junction
from kubecepodvs.sumo.mapmessage.edge import Edge
from typing import Dict


class TrafficMap:

    def __init__(self):
        self._edges = {}
        self._junctions = {}

    def compute_position(self, junction: Junction):

        find_flag = False
        junction_lanes = junction.get_incLanes()

        if junction_lanes:
            jit = iter(junction_lanes)
            for j in jit:
                eit = iter(self._edges)
                for e in eit:
                    if find_flag is True:
                        break
                    edge = e.values()

                    if (str(edge.get_from())) and (str(edge.get_from()) is str(junction.get_id())):
                        edge.set_fromX(junction.get_x())
                        edge.set_fromY(junction.get_y())

                    if (str(edge.get_to())) and (str(edge.get_to()) is str(junction.get_id())):
                        edge.set_toX(junction.get_x())
                        edge.set_toY(junction.get_y())

                    lanes = edge.get_lanes()
                    lit = iter(lanes)
                    for l in lit:
                        lane = l.values()

                        if str(lane.get_id()) is str(j):
                            lane.set_x(junction.get_x())
                            lane.set_y(junction.get_y())

                            find_flag = True
                            break

                    edge.add_junction(junction)

    def add_edge(self, id_, edge: Edge):
        self._edges[str(id_)] = edge

    def add_junction(self, id_, junction: Junction):
        self._junctions[str(id_)] = junction
        self.compute_position(junction)

    def get_edge(self, id_) -> Edge:
        return self._edges[str(id_)]

    def get_junction(self, id_) -> Junction:
        return self._junctions[str(id_)]

    def get_edges(self) -> Dict[str, Edge]:
        return self._edges

    def get_junctions(self) -> Dict[str, Junction]:
        return self._junctions
