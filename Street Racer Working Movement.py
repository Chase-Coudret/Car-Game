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

Car_image2 = pygame.image.load ('Car_2.png')
Car_rect = Car_image.get_rect()
Car_image2 = pygame.transform.scale(Car_image2, (80,120))


      





#Game Loop with Variables 
def game_loop():
    quit_game = False
    Car_x = 120
    Car_y = 400
    Car_x_change=0
    Car_y_change=0
    Car_y_velocity= 0
    Car_x_velocity= 0
   
   

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
                elif event.key == pygame.K_UP:
                        Car_y_velocity -= 2
                elif event.key == pygame.K_DOWN:
                        Car_y_velocity += 2
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

   
            


        pygame.display.update()

        #Game Frame Rate 
        clock.tick(60)

game_loop()

pygame.quit()
quit()
