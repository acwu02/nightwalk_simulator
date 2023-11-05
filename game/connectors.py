from graph import Edge

class Connector(Edge):
    def __init__(self, id, node1, node2):
        super().__init__(id, node1, node2)

class SuburbanRoad(Connector):
    pass

class UrbanRoad(Connector):
    pass

class Bridge(Connector):
    pass

class Tunnel(Connector):
    pass