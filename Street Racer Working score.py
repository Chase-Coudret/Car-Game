import pygame
import time
import random
pygame.init()

#Game Screen Size
screen = pygame.display.set_mode((500,700),pygame.RESIZABLE)

#Game Icon Loading
game_icon = pygame.image.load('Logo.png')
pygame.display.set_icon(game_icon)

#Game Title 
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
Traffic_height = [-700, -650, -600, -400,-200]

#Font Loading
exit_font = pygame.font.Font("freesansbold.ttf", 30)
score_font = pygame.font.SysFont("arialblack", 20)

#Loading the score Message 
def score_message(msg, txt_colour, bkgd_colour,):
    txt = exit_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center = (50, 80))
    screen.blit(txt, text_box)

def high_score_message(msg, txt_colour, bkgd_colour,):
    txt = exit_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center = (50, 30))
    screen.blit(txt, text_box)


def load_high_score():
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value
      





#Game Loop with Variables 
def game_loop():
    quit_game = False
    Car_x = 120
    Car_y = 550
    Car_x_change=0
    Car_y_change=0
    Car_y_velocity= 0
    Car_x_velocity= 0
    score = 0
    high_score = load_high_score()


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

    #Collitions For Traffic With Player 
        def collide(self):
            x_diff = self.location - Car_x
            y_diff = self.y - Car_y
            if abs (x_diff) < 70 and abs (y_diff) < 100:
                pygame.quit()
                quit()
                

        
    #Locations of Traffic 
    car_1 = traffic(-100, grey, -300)
    car_2 = traffic(700, grey, -400)
    car_3 = traffic(600, grey, -100)
    car_4 = traffic(600, grey, -20)

    #List of traffic 
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

            
                
                
              
        










        #Score Counting +1 every tick 
        score += 1
        print (score)
        
        #Player Collidable 'Body' Location
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

        
        
   
       

        print(score)
        print(high_score)
     

        #Image Desplaying 
        screen.blit(Backround_image, (0, 0))
        screen.blit(Car_image, (Car_x, Car_y))

        #Running Functions For Class 
        for items in car_list:
            items.draw()
            items.move()
            items.off_screen()
            items.collide()

        #Score Visualy Displaying 
        score_message (str(score),white,grey)

        high_score_message (str(high_score),white,grey)


        if (int(score)) > (int (high_score)):
            hi_score_file = open("HI_score.txt", 'w')
            hi_score_file.write(str(score))
            hi_score_file.close ()

        #Updating what is being displayed 
        pygame.display.update()

        #Game Frame Rate 
        clock.tick(60)

game_loop()

pygame.quit()
quit()
