from classes import vertex

class Graph:


    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix
        self.current_vertex = 1
        self.current_edge = 1
        self.vertices = []
        self.edges = []
