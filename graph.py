#!/usr/bin/env python3
from node import Node
from operator import itemgetter


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
        self.distance_dict = {}
        self.num_of_city = 0

    def add_city(self, city_name, latitude, longitude):
        self.num_of_city += 1
        new_city = Node(city_name, latitude, longitude)
        self.city_list[city_name] = new_city
        return new_city

    def add_edge(self, first_city, second_city, distance=None):
        try:
            self.distance_dict[first_city].add((second_city, distance))
        except KeyError:
            self.distance_dict[first_city] = set()
            self.distance_dict[first_city].add((second_city, distance))
        try:
            self.distance_dict[second_city].add((first_city, distance))
        except KeyError:
            self.distance_dict[second_city] = set()
            self.distance_dict[second_city].add((first_city, distance))

    def get_city(self, city_name):
        if city_name in self.city_list:
            return self.city_list[city_name]
        else:
            return None

    def get_city_names(self, excep=None):
        tmp = list(self.city_list.keys())
        if excep and excep in tmp:
            tmp.remove(excep)
        return tmp

    def get_cities(self):
        return self.city_list.values()

    def get_distance_dict(self):
        return self.distance_dict

    def find_shortest_path(self):
        # Object method using for find the shortest path and return it as a
        # list
        solution = []
        return solution

    def g_calc_distance(self, cities):
        total = 0
        for i in range(len(cities) - 1):
            for city in self.distance_dict[cities[i]]:
                if cities[i+1] == city[0]:
                    total += city[1]
                    break
        return total

    def nearest_neighbor(self, first_city):
        total_distance = 0
        path = []
        path.append(first_city)
        while len(path) != len(self.distance_dict.keys()):
            last_visit = path[-1]
            tmp = list(self.distance_dict[last_visit])
            tmp.sort(key=itemgetter(1))
            for city in tmp:
                if city[0] not in path:
                    path.append(city[0])
                    total_distance += city[1]
                    break
        print(path)
        print("Total distance = " + str(total_distance))
