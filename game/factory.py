import random
from areas import Apartments, Suburbs, ConvenienceStore, Park
from connectors import SuburbanRoad, UrbanRoad, Bridge, Tunnel

class Factory():
    def __init__(self, features, probabilities):
        self.features = features
        self.probabilities = probabilities
    def generate_feature(self, id):
        p = random.random()
        for feature, feature_p in sorted(self.probabilities.items(), key=lambda x: x[1]):
            if p <= feature_p:
                return self.features[feature](id)
        return self.features["default"](id)

class AreaFactory(Factory):
    def __init__(self):
        super().__init__({
            "apartments": Apartments,
            "suburbs": Suburbs,
            "convenience_store": ConvenienceStore,
            "park": Park,
            "default": Apartments
        }, {
            "apartments": 0.3,
            "suburbs": 0.6,
            "convenience_store": 0.8,
            "park": 0.95,
            "default": 1.0
        })

class ConnectorFactory(Factory):
    def __init__(self):
        super().__init__({
            "road_suburban": SuburbanRoad,
            "road_urban": UrbanRoad,
            "bridge": Bridge,
            "tunnel": Tunnel,
            "default": SuburbanRoad
        }, {
            "road_suburban": 0.3,
            "road_urban": 0.6,
            "bridge": 0.8,
            "tunnel": 0.95,
            "default": 1.0
        })
