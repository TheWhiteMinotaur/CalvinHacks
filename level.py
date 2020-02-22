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
        # map data
        self.rawJSON = ""
        self.path = [[]]
        self.start_area = []
        self.events = []
        self.enemies = []
        #self.player = Player()

    def parse_enemies(self, enemies):
        for e in enemies:
            self.enemies.add(Enemy(

            ))

    def parse(self, filename):
        with open(filename, 'r') as map_data:
            self.rawJSON = map_data.read()
            data = json.loads(self.rawJSON)
            self.path = [[int(i) for i in a] for a in data["path"]]
            self.start_area = [int(i) for i in data["start_area"]]
            #self.events = [[int(i) for i in a] for a in data["events"]]
            #self.enemies = [int(i) for i in data["enemies"]]

    def is_point_in_path(self, point):
        print(self.path)
        for area in self.path:
            if (point[0] - area[0] < area[2] and point[0] - area[0] >= 0 and
                point[1] - area[1] < area[3] and point[1] - area[1] >= 0):
                return True
        return False
