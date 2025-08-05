"""This is a game of a car moving through traffic to earn a high score.

The score is earnt by passing oncoming traffic without touching it
"""
import pygame
import time
import random
pygame.init()

# Game Screen Size
screen = pygame.display.set_mode((500, 700), pygame.RESIZABLE)

# Game Icon Loading
game_icon = pygame.image.load('Logo.png')
pygame.display.set_icon(game_icon)

# Game Title
pygame.display.set_caption("Street Racer")


clock = pygame.time.Clock()


# Colours
Bluegreen = (200, 200, 255)
black = (0, 0, 0)
green = (188, 227, 199)
red = (255, 0, 0)
white = (255, 255, 255)
grey = (70, 70, 70, 255)

# Road Image Loading
Backround_image = pygame.image.load('Backround.png')
Backround_rect = Backround_image.get_rect()
Backround_image = pygame.transform.scale(Backround_image, (500, 700))

# car Image Loading
car_image = pygame.image.load('car.png')
car_rect = car_image.get_rect()
car_image = pygame.transform.scale(car_image, (70, 120))

# Traffic Image loading
car_image2 = pygame.image.load('car_2.png')
car_rect = car_image.get_rect()
car_image2 = pygame.transform.scale(car_image2, (70, 120))

# Lists for the x and y values of the traffic spawning.
lanes = [60, 200, 220, 360]
Traffic_height = [-900, -600, -300, -50]
Traffic_Speed = [10, 14, 16, 20]

# Font Loading
exit_font = pygame.font.Font("freesansbold.ttf", 30)
score_font = pygame.font.SysFont("arialblack", 20)


def message(msg, txt_colour, bkgd_colour,):
    """Define the ability to display a message.

    used to disply the death screen
    """
    txt = exit_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(250, 350))
    screen.blit(txt, text_box)


# Loading the score Message
def score_message(msg, txt_colour, bkgd_colour,):
    """Display the score message in top left at all times."""
    txt = exit_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(50, 70))
    screen.blit(txt, text_box)


def high_score_message(msg, txt_colour, bkgd_colour,):
    """Display the high-score in the top left, updates on restart."""
    txt = exit_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(50, 30))
    screen.blit(txt, text_box)


def load_high_score():
    """Read the high score file to know which value to display."""
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value


class Traffic:
    """Add a class of oncoming traffic."""

    def __init__(self, location, colour, y):
        """Use to initialize attributes of newly created objects."""
        self.location = location
        self.colour = colour
        self.y = y

    def draw(self):
        """Load PNG images and draw oncoming traffic in class."""
        pygame.draw.rect(screen, self.colour, [self.location, self.y, 80, 120])
        screen.blit(car_image2, (self.location, self.y))

    def move(self):
        """Choose random speed variable from Traffic_Speed list.

        Used to move oncoming traffic down the screen towards player
        """
        self.y += random.choice(Traffic_Speed)

    def off_screen(self):
        """Respawn oncoming traffic when off screen.

        When oncoming traffic fall of the bottom of the screen
        choose random lane from list to spawn in
        choose random height to spawn at
        add +1 to score
        """
        global score
        if self.y >= 700:
            self.location = random.choice(lanes)
            self.y = random.choice(Traffic_height)
            score += 1

    def collide(self):
        """Make player loss when coming in contact with oncoming traffic."""
        global game_over
        x_diff = self.location - car_x
        y_diff = self.y - car_y
        if abs(x_diff) < 70 and abs(y_diff) < 100:
            game_over = True
            return(game_over)
            time.sleep(2)
            self.y = random.choice(Traffic_height)


# Locations of Traffic
car_1 = Traffic(-100, grey, -100)
car_2 = Traffic(700, grey, -300)
car_3 = Traffic(600, grey, -500)
car_4 = Traffic(800, grey, -600)


# List of traffic
car_list = [car_1, car_2, car_3, car_4]


# Game Loop with Variables
def game_loop():
    """Define all variables and functions that will run when game is played."""
    global quit_game, game_over, car_x, car_y, score
    game_over = False
    quit_game = False
    score = 0
    car_x = 120
    car_y = 550
    car_y_velocity = 0
    car_x_velocity = 0

    high_score = load_high_score()

    # Game loop and movement
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LEFT:
                    car_x_velocity -= 15
                elif event.key == pygame.K_RIGHT:
                    car_x_velocity += 15
                elif event.key == pygame.K_SPACE:
                    car_x_velocity = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    car_x_velocity = 0
                elif event.key == pygame.K_RIGHT:
                    car_x_velocity = 0

        # Player Collidable 'Body' Location
        car_rect == (car_x, car_y)

        # car velocity saving/loading
        car_y += car_y_velocity
        car_x += car_x_velocity

        # Barriers to stop car going off screen
        if car_x >= 430:
            car_x_velocity = 0
        if car_x <= 20:
            car_x_velocity = 0

        # Image Desplaying
        screen.blit(Backround_image, (0, 0))
        screen.blit(car_image, (car_x, car_y))

        # Running Functions For Class
        for items in car_list:
            items.draw()
            items.move()
            items.off_screen()
            items.collide()

        # Score Visualy Displaying
        score_message(str(score), white, grey)

        high_score_message(str(high_score), white, grey)

        if (int(score)) > (int(high_score)):
            hi_score_file = open("HI_score.txt", 'w')
            hi_score_file.write(str(score))
            hi_score_file.close()

        # Loss Screen Allowing Restart
        while game_over is True:
            time.sleep(1)
            screen.fill(white)
            message("Game Over Press R to Restart", black, white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()

        # Updating what is being displayed
        pygame.display.update()

        # Game Frame Rate
        clock.tick(30)


game_loop()


pygame.quit()
quit()
