import random
import os

from graph import Node
from feature import Feature

class Area(Node, Feature):
    def __init__(self, id):
        Node.__init__(id)
    def generate_bg(self):
        if self.bg_files:
            self.bg = random.choice(self.bg_files)

class Apartments(Area):
    def __init__(self):
        Feature.__init__("apartments")

class Suburbs(Area):
    def __init__(self):
        Feature.__init__("suburbs")

class ConvenienceStore(Area):
    def __init__(self):
        Feature.__init__("conveniencestore")

class Park(Area):
    pass