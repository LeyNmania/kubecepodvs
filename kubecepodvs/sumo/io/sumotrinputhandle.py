from kubecepodvs.sumo.mapmessage.trafficmap import TrafficMap


class SumotrInputHandle:

    def __init__(self, filename, map_: TrafficMap):
        self._map = map_
        # 这里去掉了traffic log相关的属性

        with open(str(filename), 'r') as file:

            time = 0.0
            time_step_flag = True

            # edge
            edge_id = ''

            # lane
            lane_id = ''

            # vehicle id
            vehicle_id = ''
            # pos
            pos = 0.0
            # speed
            speed = 0.0

            while True:
                sline = str(file.readline(1024))
                if not sline:
                    break

                if sline.find('timestep') != -1 and time_step_flag:
                    vec = sline.split('"')

                    time = float(vec[1])
                    time_step_flag = False

                elif sline.find('timestep') != -1:
                    time_step_flag = True

                elif sline.find('edge id') != -1:
                    vec = sline.split('"')

                    edge_id = vec[1]

                elif sline.find('lane id') != -1:
                    vec = sline.split('"')

                    lane_id = vec[1]

                elif sline.find('vehicle id') != -1:
                    vec = sline.split('"')

                    vehicle_id = vec[1]
                    pos = float(vec[3])
                    speed = float(vec[5])

                    # 这里去掉了vehicle status和traffic log相关的代码
