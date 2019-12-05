import pygame
white = (255, 255, 255)
black = (0, 0, 0)
def tytitam():
    while True:
        yield white
        yield black


class Chess_board:

    def __init__(self, screen):
        self.screen = screen
        self.x = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.y = list('abcdefgh')
        self.board = {}
        for y in self.y:
            for x in self.x:
                self.board[f'{y}{x}'] = {'res': 1, 'color': tytitam()}

    def draw(self):
        coord = [30, 40,]
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,
                                 (64, 128, 255),
                                 (coord[0] + i * 30, coord[1] + j * 30, 30,
                                  30))
        for cord, rect in self.board.items():
            surface = (30, 30)
            print(cord, rect)
            pygame.draw.rect(surface, rect['color'], 2)

class Chessman:
    def __init__(self, team, board):
        self.team = team
        self.status = True
        if self.status:
            self.board = board

    def board_to_num(self, cord):
        y, x = list(cord)
        x = self.board.x.index(x)
        y = self.board.y.index(y)
        return y, x

    def num_to_board(self, list_hit):
        hit_cords = []
        for y, x in list_hit:
            if x in range(0, 8) and y in range(0, 8):
                x = self.board.x[x]
                y = self.board.y[y]
                if self.board.board.get(f'{y}{x}'):
                    hit_cords.append(f'{y}{x}')
                else:
                    print('-')

        return hit_cords

class Horse(Chessman):

    def __init__(self, team, board):
        super().__init__(team, board)

    def hit_mask(self, cord):
        y, x = self.board_to_num(cord)
        z = [(y-1, x-2), (y-1, x+2), (y+1, x-2), (y+1, x+2), (y-2, x-1), (y-2, x+1), (y+2, x-1), (y+2, x+1)]
        z = self.num_to_board(z)
        return z
var = []
def funk(chessman, cord, target, history_stips=None):
    global var
    if history_stips:
        h = history_stips.copy()
    else:
        h = [cord,]
    if len(var) > 0 and len(var) < len(h)+1:
        return False

    z = chessman.hit_mask(cord)
    if target in z:
        h.append(target)
        var = h
        return True


    for i in z:
        if i not in h:
            h.append(i)
            if funk(chessman, i, target, history_stips=h):
                break
            else:
                h.remove(i)




pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
board = Chess_board(screen)

horse = Horse('while', board)
funk(horse, 'b1', 'g7')
print(var)

screen.fill((192, 192, 192))
pygame.display.update()
clock.tick(60)
