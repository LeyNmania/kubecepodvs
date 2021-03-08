from kubecepodvs.sumo.io.netinputhandle import NetInputHandle
from kubecepodvs.sumo.io.sumotrinputhandle import SumotrInputHandle


def main():
    SumotrInputHandle('C:/Users/kyx19/Desktop/sumoData/map.sumo.tr',
                      NetInputHandle('C:/Users/kyx19/Desktop/sumoData/map.net.xml').get_map())


if __name__ == '__main__':
    main()
