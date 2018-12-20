#!/usr/bin/env python3


class Node:
    #
    def __init__(self, city_name, latitude, longitude):
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.city_name) + 'connected to' + str([x.city_name
                   for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_city_name(self):
        return self.city_name

    def get_weight(self, nbr):
        return self.connected_to[nbr]
