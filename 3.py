
with open('3.txt', 'r') as f:
    moves = [line.split(',') for line in f.readlines()]

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)
    
    """
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    """
    
    def __repr__(self):
        return f'Point: ({self.x}, {self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        return abs(self.x) + abs(self.y) < abs(other.x) + abs(other.y)
    
    def mdist(self):
        return self.x + self.y


nwires = len(moves)
point_map = {}
dirs = {
    'R': Point(1, 0),
    'U': Point(0, 1),
    'D': Point(0, -1),
    'L': Point(-1, 0)
}

for wire, wire_moves in enumerate(moves):

    curpos = Point(0,0)
    step_count = 0

    for move in wire_moves:
        dirr = move[0]
        move_cnt = int(move[1:])

        for single_move in range(move_cnt):
            curpos += dirs[dirr]
            step_count += 1

            if curpos not in point_map.keys():
                point_map[curpos] = ({wire}, {wire: step_count})
            else:
                point_map[curpos][0].add(wire)
                point_map[curpos][1][wire] = step_count

print(nwires)
#print(point_map.keys())
crossovers = {point: (wire_set, wire_stepcount)
              for point, (wire_set, wire_stepcount) in point_map.items()
              if len(wire_set) == nwires}
    
print(f'3.1: {min(crossovers.keys()).mdist()}')


ans2 = min([sum(wire_stepcount.values())
            for point, (wire_set, wire_stepcount) in crossovers.items()])

print(f'3.2: {ans2}')






