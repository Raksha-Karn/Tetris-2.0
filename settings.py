import pygame

WIDTH = 10
HEIGHT = 15
CELL_SIZE = 40

GAME_WIDTH, GAME_HEIGHT = WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE

SIDEBAR_WIDTH = 200
PREVIEW_SPACE = 0.7
SCORE_SPACE = 1 - PREVIEW_SPACE

PADDING = 20

WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

UPDATE_START_SPEED = 600
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(WIDTH//2, -1)


GRAY = '#1C1C1C'
YELLOW = '#F1E60D'
RED = '#E51B20'
BLUE = '#204B9B'
GREEN = '#65B32E'
PURPLE = '#7B217F'
CYAN = '#6CC6D9'
ORANGE = '#F07E13'
LINE_COLOR = '#FFFFFF'

TETROMINOS = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0, -1)], 'color': PURPLE},
    'O': {'shape': [(0,0), (0, -1), (1, 0), (1, -1)], 'color': GREEN},
    'J': {'shape': [(0,0), (0, -1), (0, 1), (-1, 1)], 'color': YELLOW},
    'L': {'shape': [(0,0), (0, -1), (0, 1), (1, 1)], 'color': ORANGE},
    'S': {'shape': [(0,0), (-1, 0), (0, -1), (1, -1)], 'color': BLUE},
    'Z': {'shape': [(0,0), (1, 0), (0, -1), (-1, -1)], 'color': CYAN},
    'I': {'shape': [(0,0), (0, -1), (0, -2), (0, 1)], 'color': RED},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200, 5: 5000}
