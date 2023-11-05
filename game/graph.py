# Implementation of graph data structure

import random

class Node():
    def __init__(self, id):
        self.id = id

class Edge():
    def __init__(self, id, node1, node2):
        self.id = id
        self.node1 = node1
        self.node2 = node2

class Graph():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.adjacency_list = {}

    def add_node(self, node: Node):
        self.nodes[node.id] = node
        self.adjacency_list[node.id] = []

    # TODO abstract away edge formation?
    def add_edge(self, node1: Node, node2: Node):
        self.adjacency_list[node1.id].append(node2)
        self.adjacency_list[node2.id].append(node1)

    def get_random_node(self):
        return self.nodes[random.randint(0, len(self.nodes) - 1)]


