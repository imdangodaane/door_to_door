#!/usr/bin/env python3


class Node:
    def __init__(self, city_name, latitude, longitude):
        self.city_name = city_name
        self.lat = latitude
        self.long = longitude
        self.connected_to = {}

    def add_neighbor(self, nbr, distance=None):
        self.connected_to[nbr] = distance

    def get_connections(self):
        return self.connected_to.keys()

    def get_city_name(self):
        return self.city_name

    def get_distance(self, nbr):
        return self.connected_to[nbr]

    def find_nearest_neighbor(self):
        try:
            return min(self.connected_to.keys(), key=lambda k: self.connected_to[k])
        except ValueError:
            return None
