#!/usr/bin/env python3
import argparse
import sys
import node
import graph


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


def calc_distance(first, second):
    pass


def nearest_neighbor():
    # The nearest neighbour algorithm
    pass


def sorted_cities(city_list):
    tmp = []
    for city in city_list:
        tmp.append(city.split(', '))
    tmp.sort(key=lambda x: (float(x[1]), float(x[2])))
    return tmp


def main():
    '''
    '''
    filename, choice = get_from_cmd()
    content = valid_and_read(filename)
    cities = content.split('\n')[:-1]
    first_city = cities[0]
    cities = sorted_cities(cities)
    print(first_city)

    if choice == 'nn':
        nearest_neighbor()
    else:
        pass


if __name__ == "__main__":
    main()
