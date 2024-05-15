from settings import *
from os.path import join

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_SPACE - PADDING))    
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING ))  
               
        self.display_surface = pygame.display.get_surface()
        
        self.font = pygame.font.Font(None, 20)
        
        self.increment_height = self.surface.get_height() / 3
        
        self.score = 0
        self.level = 1
        self.lines = 0
        
    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white')
        text_rect = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rect)
        
    def update_level(self, lines):
        self.level = 1 + int(lines / 2)
        
    def run(self,difficulty):
        self.surface.fill(GRAY)
        for i, text in enumerate([("SCORE", self.score), ("LINES", self.lines), ("LEVEL", self.level)]):
            x = self.surface.get_width() / 2 
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x, y), text)

        if difficulty == 'medium':
            line_color = (255, 255, 0)  
        elif difficulty == 'hard':
            line_color = (255, 0, 0)  
        else:
            line_color = (0, 255, 0) 
            
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, line_color, self.rect, 2, 2)