import pygame as pg

class Game:
    def __init__(self):               
        self.width = 800
        self.height = 600       
        self.gameDisplay = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()  
        
pg.init()

pg.display.set_caption( ' Snake ')  

def run(self):
        
        running = True
        # intialise timer for food spawning and movement
        food_timer = pg.time.get_ticks()
        snake_timer = pg.time.get_ticks()

        while running: 
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN: 
                    self.evaluate_key(event)
                if event.type == pg.QUIT:
                    running = False

            timer = pg.time.get_ticks()
            if timer - snake_timer > 40: # check if 40 ms since last move passed
                running = self.snake.move()
                self.check_food()
                snake_timer = timer

            if timer - food_timer > 2000: # generating  food every 2000ms
                self.generate_food()
                food_timer = timer

            self.clock.tick(100) # limits the game to 100 frames a second

            self.draw_all()
        pg.quit()

g = Game()
g.run()
    
       
       