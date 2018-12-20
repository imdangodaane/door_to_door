#!/usr/bin/env python3
from node import Node


class Graph:
    '''
    The Graph class will have a find_shortest_path method that will return
    the solution to the problem as a list.

    Graph and its representations

    Graph is a data structure that consists of following two components:
    1. A finite set of vertices also called as nodes.
    2. A finite set of ordered pair of the form (u, v) called as edge.
    The pair is ordered because (u, v) is not same as (v, u) in case of a
    directed graph(di-graph). The pair of the form (u, v) indicates that
    there is an edge from vertex u to vertex v.
    The edges may contain weight/value/cost.

    Following two are the most commonly used representations of a graph.
    1. Adjacency Matrix
    2. Adjacency List

    Vertex (Node)
    Edge
    -> Directed graph (one-way edges)

    G = (V, E)
    V = set of vertices
    E = set of edges

    Path (from one vertex to another vertex)
    Cycle (from one vertex and return to that vertex)

    When two vertices are connected by an edge, we say that they are "adjacent"

    A matrix is not a very efficient way to store sparse data

    Each vertex object in the graph maintains a list of the other vertices
    that it is connected to.
    '''
    def __init__(self):
        self.city_list = {}
        self.num_of_city = 0

    def add_city(self, city_name, latitude, longitude):
        self.num_of_city += 1
        new_city = Node(city_name, latitude, longitude)
        self.city_list[city_name] = new_city
        return new_city

    def add_edge(self, first_vertex, second_vertex, weight=None):
        pass

    def get_city(self, city_name):
        if city_name in self.city_list:
            return self.city_list[city_name]
        else:
            return None

    def get_cities(self):
        return self.city_list.keys()

    def find_shortest_path(self):
        # Object method using for find the shortest path and return it as a
        # list
        solution = []
        return solution
