from settings import *
from pygame.image import load
from os import path

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_SPACE))    
        self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING, PADDING ))
        self.display_surface = pygame.display.get_surface()
        
        self.shape_surfaces = {shape: load(path.join('.', 'images', f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}
        
        self.increment_height = self.surface.get_height() / 3
        
    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height/2 + i * self.increment_height
            rect = shape_surface.get_rect(center = (x, y))
            self.surface.blit(shape_surface, rect)
        
    def run(self, next_shapes,difficulty):
        if difficulty == 'medium':
            line_color = (255, 255, 0)  
        elif difficulty == 'hard':
            line_color = (255, 0, 0)  
        else:
            line_color = (0, 255, 0) 
        self.surface.fill(GRAY)
        self.display_pieces(next_shapes)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, line_color, self.rect, 2, 2)