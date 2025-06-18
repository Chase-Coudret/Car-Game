import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((500,700),pygame.RESIZABLE)
game_icon = pygame.image.load('Logo.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Street Racer")


clock = pygame.time.Clock()


# Colours  
Bluegreen = (200, 200, 255)
black = (0, 0, 0)
green = (188, 227, 199)
red = (255, 0, 0)
white = (255, 255, 255)
grey = (70,70,70,255)

#Road Image Loading 
Backround_image = pygame.image.load ('Backround.png')
Backround_rect = Backround_image.get_rect()
Backround_image = pygame.transform.scale(Backround_image, (500,700))

#Car Image Loading 
Car_image = pygame.image.load ('Car.png')
Car_rect = Car_image.get_rect()
Car_image = pygame.transform.scale(Car_image, (80,120))

#Traffic Image loading
Car_image2 = pygame.image.load ('Car_2.png')
Car_rect = Car_image.get_rect()
Car_image2 = pygame.transform.scale(Car_image2, (80,120))

# Lists for the x and y values of the traffic spawning.
lanes = [60,200,360]
Traffic_height = [-1000,-800,-600, -400,-200]



      
      





#Game Loop with Variables 
def game_loop():
    quit_game = False
    Car_x = 120
    Car_y = 550
    Car_x_change=0
    Car_y_change=0
    Car_y_velocity= 0
    Car_x_velocity= 0
    

    #Traffic Class 
    class traffic:
        def __init__(self, location,colour, y,):
            self.location = location
            self.colour = colour
            self.y = y

    #Traffic PNG loading
        def draw(self):
            pygame.draw.rect(screen, self.colour, [self.location, self.y, 80,120])
            screen.blit(Car_image2, (self.location, self.y))
        
      
    #Traffic Movement
        def move(self):
            self.y += 20

    #Traffic off screen respawning 
        def off_screen(self):
            if self.y >= 700:
                self.location = random.choice (lanes)
                self.y = random.choice (Traffic_height)

        def collide(self):
            x_diff = self.location - Car_x
            y_diff = self.y - Car_y
            if abs (x_diff) < 70 and abs (y_diff) < 100:
                pygame.quit()
                quit()
                

        
   
    car_1 = traffic(-100, grey, -200)
    car_2 = traffic(700, grey, -200)
    car_3 = traffic(600, grey, -200)
    car_4 = traffic(600, grey, -200)

    car_list = [car_1, car_2, car_3, car_4]
        

   
   

 #Game loop and movement 
    while not quit_game:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LEFT:
                        Car_x_velocity -= 15
                elif event.key == pygame.K_RIGHT:
                        Car_x_velocity += 15
                elif event.key == pygame.K_SPACE:
                        Car_x_velocity = 0
                        Car_y_velocity = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    Car_y_change = -0.1
                elif event.key == pygame.K_DOWN:
                    Car_y_change = 0.1
                elif event.key == pygame.K_LEFT:
                    Car_x_velocity = 0
                elif event.key == pygame.K_RIGHT:
                    Car_x_velocity = 0
                    
                
                
              
        














        Car_rect == (Car_x, Car_y)  

        #Car velocity saving/loading 
        Car_y += Car_y_velocity
        Car_y_change += Car_y_velocity
        Car_x += Car_x_velocity
        Car_x_change += Car_x_velocity

        #Barriers to stop car going off screen
        if Car_x <= 0:
            Car_x_velocity = 0
        if Car_x >= 440:
            Car_x_velocity = 0
        if Car_y >= 550:
            Car_y_velocity = 0
        if Car_y <= 0:
            Car_y_velocity = 0 

        
        
   
       

        
     

        #Image Desplaying 
        
        screen.blit(Backround_image, (0, 0))
        screen.blit(Car_image, (Car_x, Car_y))

        for items in car_list:
            items.draw()
            items.move()
            items.off_screen()
            items.collide()
            


        pygame.display.update()

        #Game Frame Rate 
        clock.tick(60)

game_loop()

pygame.quit()
quit()
