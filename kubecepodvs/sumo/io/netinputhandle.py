from kubecepodvs.sumo.mapmessage.edge import Edge
from kubecepodvs.sumo.mapmessage.lane import Lane
from kubecepodvs.sumo.mapmessage.junction import Junction
from kubecepodvs.sumo.mapmessage.trafficmap import TrafficMap


class NetInputHandle:

    def __init__(self, filename):
        self._map = TrafficMap()

        with open(str(filename), 'r') as file:

            # edge
            edge_id = ''
            from_ = ''
            to = ''
            edge = None

            # lane
            lane_id = ''
            lane_length = 0.0
            lane_shape = ''

            # junction
            junction_id = ''
            junction_lane1 = ''
            junction_lane2 = ''
            junction_shape = ''

            while True:
                sline = str(file.readline(1024))
                if not sline:
                    break

                if sline.find('edge id') != -1:
                    vec = sline.split('"')

                    edge_id = vec[1]
                    edge = Edge(edge_id)

                    if len(vec) > 5:
                        from_ = vec[3]
                        to = vec[5]
                        edge.set_from(from_)
                        edge.set_to(to)

                elif sline.find('</edge>') != -1:
                    if edge:
                        self._map.add_edge(edge_id, edge)

                elif sline.find('lane id') != -1:
                    vec = sline.split('"')

                    lane_id = vec[1]

                    if len(vec) > 13:
                        lane_length = float(vec[11])
                        lane_shape = vec[13]
                    elif len(vec) > 11:
                        lane_length = float(vec[9])
                        lane_shape = vec[11]
                    else:
                        lane_length = float(vec[7])
                        lane_shape_ = vec[9].split(
                            ' ')  # 原版在这里就是新建了一个也叫lane_shape的vector<string>变量 而不是string 然后没有用它 人间迷惑行为

                    edge.add_lanes(lane_id, Lane(
                        lane_id, lane_length, lane_shape))

                elif sline.find('junction id') != -1:
                    vec = sline.split('"')

                    junction_id = vec[1]
                    junction_lane1 = vec[9]
                    junction_lane2 = vec[11]

                    if len(vec) > 13:
                        junction_shape = vec[13]

                    junction = Junction(
                        junction_id, vec[5], vec[7], junction_lane1, junction_lane2, junction_shape)
                    self._map.add_junction(junction_id, junction)

    def get_map(self) -> TrafficMap:
        return self._map
