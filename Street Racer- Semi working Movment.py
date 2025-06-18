import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((300,500),pygame.RESIZABLE)
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


Backround_image = pygame.image.load ('Backround.png')
Backround_rect = Backround_image.get_rect()
Backround_image = pygame.transform.scale(Backround_image, (300,500))

Car_image = pygame.image.load ('Car.png')
Car_rect = Car_image.get_rect()
Car_image = pygame.transform.scale(Car_image, (60,100))


def game_loop():
    quit_game = False
    Car_x = 120
    Car_y = 400
    Car_x_change=0
    Car_y_change=0

    
   

 #Game loop and movement 
    
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Car_x_change = -20
                    Car_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    Car_x_change = 20
                    Car_y_change = 0
                elif event.key == pygame.K_UP:
                    Car_y_change = -20
                    Car_x_change = 0
                elif event.key == pygame.K_DOWN:
                    Car_y_change = 20
                    Car_x_change = 0


    
        Car_x +=Car_x_change
        Car_y +=Car_y_change
     
        

        
        
   
       

        
     


        screen.fill(white)
        screen.blit(Backround_image, (0, 0))
        screen.blit(Car_image, (Car_x, Car_y))



        pygame.display.update()

        clock.tick(20)

game_loop()

pygame.quit()
quit()
