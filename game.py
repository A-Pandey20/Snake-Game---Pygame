''' This file contains the snake_game_pygame class '''
import pygame
from random import randint
from helper import Direction, Color, Args, Point

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class snake_game_pygame:
    def __init__(self, w=640, h=480):
        ''' initialization '''
        self.w = w
        self.h = h
        self.dir = Direction()
        self.color = Color()
        self.args = Args(block_size=20, speed=20)

        # initialize display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        
        # initialize game state -> right movement at the centre of canvas
        self.direction = self.dir.right
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-self.args.block_size, self.head.y), Point(self.head.x-(2*self.args.block_size), self.head.y)]
        
        self.score = 0
        self.food = None
        self._new_food()
        
    def _new_food(self):
        ''' Places new food(random location) '''
        x = randint(0, (self.w-self.args.block_size )//self.args.block_size )*self.args.block_size 
        y = randint(0, (self.h-self.args.block_size )//self.args.block_size )*self.args.block_size
        self.food = Point(x, y)
        if self.food in self.snake:
            self._new_food()
        
    def take_step(self):
        ''' Registers User Input and takes next step
            Set to public so to be accessed in main.py '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = self.dir.left
                elif event.key == pygame.K_RIGHT:
                    self.direction = self.dir.right
                elif event.key == pygame.K_UP:
                    self.direction = self.dir.up
                elif event.key == pygame.K_DOWN:
                    self.direction = self.dir.down
        
        # Movement
        self._move(self.direction)      # update the head
        self.snake.insert(0, self.head)
        
        # Check if collided
        game_over = False
        if self._collided():
            game_over = True
            return game_over, self.score
            
        # New food placed or movement
        if self.head == self.food:
            self.score += 1
            self._new_food()
        else:
            self.snake.pop()
        
        # UI and clock update
        self._update_ui()
        self.clock.tick(self.args.speed)

        # return
        return game_over, self.score
    
    def _collided(self):
        ''' checks if already collided '''
        # collides with a boundary
        if self.head.x > self.w - self.args.block_size or self.head.x < 0 or self.head.y > self.h - self.args.block_size or self.head.y < 0:
            return True
        # collides with itself
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        ''' updates UI '''
        self.display.fill(self.color.black)
        
        for pt in self.snake:
            pygame.draw.rect(self.display, self.color.blue1, pygame.Rect(pt.x, pt.y, self.args.block_size, self.args.block_size))
            pygame.draw.rect(self.display, self.color.blue2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        pygame.draw.rect(self.display, self.color.red, pygame.Rect(self.food.x, self.food.y, self.args.block_size, self.args.block_size))
        
        text = font.render("Score: " + str(self.score), True, self.color.white)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
    def _move(self, direction):
        ''' moves the snake '''
        x = self.head.x
        y = self.head.y
        if direction == self.dir.right:
            x += self.args.block_size
        elif direction == self.dir.left:
            x -= self.args.block_size
        elif direction == self.dir.down:
            y += self.args.block_size
        elif direction == self.dir.up:
            y -= self.args.block_size
            
        self.head = Point(x, y)

#########################################################################################################################################