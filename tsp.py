#!/usr/bin/env python3
import argparse
import sys
import collections
import time
from operator import itemgetter
from random import shuffle
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
    # Calculate distance base-on Euclid
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    return round((abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1/2), 4)


def make_graph(cities):
    # Make graph object
    tmp = []
    for city in cities:
        tmp.append(city.split(', '))
    cities = list(tmp)
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
            # city.add_neighbor(queue[i].city_name, distance)
    return _graph


def nearest_neighbor(cities):
    # Nearest neighbor algorithm
    first_city = cities[0].split(', ')[0]
    _graph = make_graph(cities)
    _graph.nearest_neighbor(first_city)


def sort_and_slice(cities):
    # Slice cities into list of cities, then sort by second and third
    # element (latitude and longitude)
    tmp = []
    for city in cities:
        tmp.append(city.split(', '))
    tmp.sort(key=lambda x: (float(x[1]), float(x[2])))
    return tmp


def calc_total_distance(cities):
    # Calculate total distance of a city list
    total_distance = 0
    for i in range(len(cities) - 1):
        total_distance += calc_distance(cities[i][1], cities[i][2],
                                        cities[i+1][1], cities[i+1][2])
    return total_distance


def find_best_route(list_cities):
    # Find best route of a city list base-on total distance
    total_distance = 10000
    best_route = None
    for pair in list_cities:
        tmp = calc_total_distance(pair)
        if tmp < total_distance:
            total_distance = tmp
            best_route = pair
    print(total_distance)
    return best_route


def my_algorithm(cities):
    # My solution for this project
    path = []
    first_city = cities[0].split(', ')
    path.append(cities[0].split(', ')[0])
    cities = sort_and_slice(cities)
    percent = round(len(cities) / 10)
    shuffle_times = round(len(cities))
    ind = cities.index(first_city)
    # while len(path) != len(cities):
    last_visit = first_city
    tmp = []
    shuffle_list = []
    for i in range(ind - percent, ind + percent):
        try:
            if i == ind: # Don't append last city
                continue
            tmp.append(cities[i])
        except IndexError:
            continue
    for i in range(shuffle_times):
        _ = list(tmp)
        shuffle(_)
        _.insert(0, first_city)
        shuffle_list.append(_)
    print(shuffle_list)
    best_route = find_best_route(shuffle_list)
    print(best_route)
    # print(path)


def main():
    '''
    '''
    filename, choice = get_from_cmd()
    content = valid_and_read(filename)
    cities = content.split('\n')[:-1]
    if choice == 'nn':
        nearest_neighbor(cities)
    else:
        my_algorithm(cities)


if __name__ == "__main__":
    flag = time.time()
    main()
    print("Total time = " + str(time.time() - flag))
