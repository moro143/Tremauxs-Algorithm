
class Robot:
    
    def __init__(self):
        self.NESW = 'N'
    
    def rotate(self, rotate_right=True):
        NESW_list = ['N', 'E', 'S', 'W', 'N','W']
        NESW_index = {'N': 0,
                        'E': 1,
                        'S': 2,
                        'W': 3,}
        if rotate_right:
            self.NESW = NESW_list[NESW_index[self.NESW]+1]
        else:
            self.NESW = NESW_list[NESW_index[self.NESW]-1] 

def possible_moves(pos, maze):
    x, y = pos[0], pos[1]
    result = []
    if x!=0:
        if maze[y][x-1]==1:
            result.append('W')
    if x!=len(maze[0])-1:
        if maze[y][x+1]==1:
            result.append('E')
    if y!=0:
        if maze[y-1][x]==1:
            result.append('N')
    if y!=len(maze)-1:
        if maze[y+1][x]==1:
            result.append('S')
    return result

def was_there(p, b):
    for i in b:
        if p[0]==i[0] and p[1]==i[1]:
            return True
    return False

if __name__ == '__main__':
    r = Robot()
    
    maze = [
            [1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            ]
    pos = [0, 0]

    intersections = []
    been = [pos]
    moves = []
    while True:
        print(pos)
        moves = possible_moves(pos, maze)
        
        if len(moves)>2:
            intersections.append(pos)
        
        what_add = {
            'N': [0, -1],
            'E': [1, 0],
            'S': [0, 1],
            'W': [-1, 0]
        }
        for i in moves:
            can_move = True
            if not was_there([pos[0]+what_add[i][0], pos[1]+what_add[i][1]], been):
                pos = [pos[0]+what_add[i][0], pos[1]+what_add[i][1]]
                been.append(pos)
                break
            else:
                can_move = False

        if not can_move:
            if len(intersections)>1:
                if intersections[-1]!=pos:
                    pos = intersections[-1]
                    intersections.pop()
                else:
                    intersections.pop()
                    pos = intersections[-1]
                    intersections.pop()
            else:
                break