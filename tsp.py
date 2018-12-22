#!/usr/bin/env python3
import argparse
import sys
import collections
import time
from operator import itemgetter
from subprocess import Popen
from node import Node
from graph import Graph



def get_from_cmd():
    # Get algorithm from choices, default is nearest neighbour
    parser = argparse.ArgumentParser(prog='TSP')
    parser.add_argument("-k", "--kind", type=str, default='nn')
    parser.add_argument("filename")

    args = parser.parse_args()
    return args.filename, args.kind


def valid_and_read(filename):
    # Valid file and return content in file
    try:
        with open(filename, 'r') as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        print("Invalid file", file=sys.stderr)


def calc_distance(x1, y1, x2, y2):
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    return round((abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1/2), 4)


def find_all_neighbor():
    pass


def make_graph(cities):
    now = time.time()
    cities = sort_and_slice(cities)
    _graph = Graph()
    for city in cities:
        if city:
            _graph.add_city(city[0], city[1], city[2])
    queue = collections.deque(_graph.get_cities())
    while queue:
        city = queue.popleft()
        for i in range(len(queue)):
            distance = calc_distance(city.lat, city.long,
                                     queue[i].lat, queue[i].long)
            _graph.add_edge(city.city_name, queue[i].city_name, distance)
            city.add_neighbor(queue[i].city_name, distance)
    print(time.time() - now)
    return _graph


def nearest_neighbor(cities):
    first_city = cities[0].split(', ')[0]
    _graph = make_graph(cities)
    path = []
    queue = collections.deque()
    path.append(first_city)
    queue.append(first_city)
    tmp = list(_graph.get_distance_dict())
    tmp.sort(key=itemgetter(1))
    while queue:
        if len(path) == len(cities):
            break
        for i in range(len(tmp)):
            if first_city in tmp[i][0]:
                eles = tmp[i][0].split('<=>')
                if first_city == eles[0]:
                    nearest_city = eles[1]
                else:
                    nearest_city = eles[0]
                path.append(nearest_city)
                queue.append(nearest_city)
                del tmp[i]
                break
    print(path)


def my_algorithm():
    # My solution for this project
    first_city = cities[0]
    cities = sort_and_slice(cities)
    percent = round(len(_graph.get_cities()) / 10)


def sort_and_slice(cities):
    tmp = []
    for city in cities:
        tmp.append(city.split(', '))
    tmp.sort(key=lambda x: (float(x[1]), float(x[2])))
    return tmp


def main():
    '''
    '''
    filename, choice = get_from_cmd()
    content = valid_and_read(filename)
    cities = content.split('\n')[:-1]
    nearest_neighbor(cities)
    if choice == 'nn':
        # nearest_neighbor(cities)
        pass
    else:
        pass


if __name__ == "__main__":
    main()
