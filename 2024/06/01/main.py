from enum import Enum
from pprint import pprint as pp
import sys

class Guard:             
    def __init__(self, x, y, orientation):
        self._map = None
        self.x = x
        self.y = y
        self.orientation = orientation
        self.positions_occupied = 0

    def set_map(self, _map):
        self._map = _map

    def look_in_current_direction(self):
        if self.orientation % 4 == 0: # RIGHT
            return _map[self.y][self.x + 1]
        
        if self.orientation % 4 == 1: # DOWN
            return _map[self.y + 1][self.x]
        
        if self.orientation % 4 == 2: # LEFT
            return _map[self.y][self.x - 1]
        
        if self.orientation % 4 == 3: # UP
            return _map[self.y - 1 ][self.x]

    def turn_clockwise(self):
        self.orientation += 1

    def check_map(self):
        _map[self.y][self.x] = 'X'

    def move_in_current_direction(self):
        if self.orientation % 4 == 0: # RIGHT
            self.x += 1
        
        if self.orientation % 4 == 1: # DOWN
            self.y += 1
        
        if self.orientation % 4 == 2: # LEFT
            self.x -= 1
        
        if self.orientation % 4 == 3: # UP
            self.y -= 1

        if self.x < 0 or self.y < 0:
            print("Attempted to move OOB")
            raise IndexError

    def increment_position_count(self):
        if _map[self.y][self.x] != 'X':
            self.positions_occupied += 1

# main
input_file = sys.argv[1]

guard = None
_map = []

try:
    with open(input_file, 'r') as f:
        for y, line in enumerate(f):
            _map.append(list(line)[:-1])
            for x, _char in enumerate(line):
                if _char == '^':
                    guard = Guard(x=x, y=y, orientation=3)

except FileNotFoundError as e:
    print(e)
    exit()
           
if guard:
    guard.set_map(_map)
    print(f"Guard starting at position ({guard.x}, {guard.y})")
else:
    print("We never found the guard's starting point")
    exit()

try:
    while True:
        guard.increment_position_count()
        guard.check_map()
        next_pos = guard.look_in_current_direction()
        if next_pos == "#":
            guard.turn_clockwise()
        guard.move_in_current_direction()
        
except IndexError as e:
    print(f"The guard hit the boundary at position ({guard.x}, {guard.y}).")
    print(f"She occupied {guard.positions_occupied} positions" )
    
    with open('map_output.txt', 'w') as f:
        for line in guard._map:
            f.write(''.join(line))
