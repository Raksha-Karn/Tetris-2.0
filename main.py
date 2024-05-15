import pygame
from settings import *
from sys import exit
from os.path import join

from game import Game
from score import Score
from preview import Preview
from random import choice

class Main:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')
        
        self.difficulty = None
        
        self.music = pygame.mixer.Sound(join('.', 'sound', 'win.mp3'))
        self.music.set_volume(0.05)
        
    def display_welcome_screen(self):
        font = pygame.font.Font(None, 36)
        welcome_text = font.render("Choose a difficulty", True, LINE_COLOR)
        instruction_text = font.render("----------------------------", True, LINE_COLOR)
        text_easy = font.render("Easy", True, GREEN)
        text_medium = font.render("Medium", True, YELLOW)
        text_hard = font.render("Hard", True, RED)
        
        welcome_rect = welcome_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
        instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        text_rect_easy = text_easy.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        text_rect_medium = text_medium.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        text_rect_hard = text_hard.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if text_rect_easy.collidepoint(mouse_pos):
                        self.difficulty = 'easy'
                        return
                    elif text_rect_medium.collidepoint(mouse_pos):
                        self.difficulty = 'medium'
                        return
                    elif text_rect_hard.collidepoint(mouse_pos):
                        self.difficulty = 'hard'
                        return
            
            self.screen.fill(GRAY)
            self.screen.blit(welcome_text, welcome_rect)
            self.screen.blit(instruction_text, instruction_rect)
            self.screen.blit(text_easy, text_rect_easy)
            self.screen.blit(text_medium, text_rect_medium)
            self.screen.blit(text_hard, text_rect_hard)
            
            pygame.display.update()
            self.clock.tick()
    
    def run(self):
        self.display_welcome_screen()
        
        self.music.play()

        if self.difficulty:
            self.game = Game(self.get_next_shape, self.update_score, self.difficulty)
            self.game.run(self.difficulty)

        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
        
        # Components
        self.score = Score()
        self.preview = Preview()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(GRAY)
            
            self.game.run(self.difficulty)
            self.score.run(self.difficulty)
            self.preview.run(self.next_shapes,self.difficulty)
            
            pygame.display.update()
            self.clock.tick()
    
    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level
        
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape


if __name__ == '__main__':
    main = Main()
    main.run()
