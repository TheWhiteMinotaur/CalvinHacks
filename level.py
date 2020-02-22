#!/usr/bin/python3

# Map file scheme
# {
#   path: [
#       [x, y, w, h],
#       [x, y, w, h]
#   ],
#   start_area: [x, y, w, h],
#   events: [
#       [x, y, w, h],
#   ],
#   enemies: [
#       [],
#       [],
#   ]
# }

import json

class Level:
    def __init__(self):
        self.rawJSON = ""
        self.path = [[]]
        self.start_area = []
        self.events = [[]]
        self.enemies = []

    def parse(self, filename):
        with open(filename, 'r') as map_data:
            self.rawJSON = map_data.read()
            data = json.loads(map_data.read())
            self.path = [[int(i) for i in a] for a in data["path"]]
            self.start_area = [int(i) for i in data["start_area"]]
            self.events = [[int(i) for i in a] for a in data["events"]]
            self.enemies = [int(i) for i in data["enemies"]]

    def is_point_in_path(self, point):
        for area in self.path:
            if (abs(point[0] - area[0]) < area[2] and abs(point[1] - area[1]) < area[3]):
                return True
        return False

    
