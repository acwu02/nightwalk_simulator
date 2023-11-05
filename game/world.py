import random

from graph import Graph
from factory import AreaFactory, ConnectorFactory
from areas import Apartments

MIN_AREAS = 10
MAX_AREAS = 13

MAX_CONNECTORS = 4

class World(Graph):
    def __init__(self):
        super().__init__()
        self.num_areas = random.randint(MIN_AREAS, MAX_AREAS)
        self.area_factory = AreaFactory()
        self.connector_factory = ConnectorFactory()
        self.add_areas()

    def add_areas(self):
        for i in range(self.num_areas):
            area = self.area_factory.generate_feature(i)
            self.add_node(area)
        spawn = Apartments(self.num_areas)
        self.add_node(spawn)

    def add_connectors(self):
        global test
        connectors = []
        for id, node in self.nodes.items():
            num_connectors = random.randint(1, MAX_CONNECTORS)
            for i in range(MAX_CONNECTORS):
                rand_node = self.get_random_node()
                connectors.append((node.id, rand_node.id))
        for id, node_pair in enumerate(connectors):
            connector = self.connector_factory.generate_feature(i)


