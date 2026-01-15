import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dungeon Descent")

# Clock; controls frame rate
clock = pygame.time.Clock()

# Enemy class
class Enemy:
    def __init__(self, x, y, width, height, color, image_path='Orc.png'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speed = 2  # pixels per frame     

# Creating enemy instances
enemy_1 = Enemy(800, 600, 60, 60, (255, 0, 0), 'Orc.png')  # Enemy 1
enemy_2 = Enemy(600, 400, 60, 60, (255, 0, 0), 'Orc.png')  # Enemy 2
enemy_3 = Enemy(400, 200, 60, 60, (255, 0, 0), 'Orc.png')  # Enemy 3
enemy_4 = Enemy(400, 400, 60, 60, (255, 0 , 0), 'Orc.png') # Enemy 4
enemy_5 = Enemy(500, 500, 60, 60, (255, 0, 0), 'Orc.png')  # Enemy 5

enemies = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5]

# Obstacle class
class Obstacle:
     def __init__(self, x, y, width, height, color, image_path= 'obstacle.png'):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.color = color
         self.image = pygame.image.load(image_path)
         self.image = pygame.transform.scale(self.image, (self.width, self.height))

# Creating obstacle instances
obstacle1 = Obstacle(200, 400, 50, 50, (0, 0, 0), 'obstacle.png')   # Obstacle 1
obstacle2 = Obstacle(350, 175, 50, 50, (0, 0, 0), 'obstacle.png')   # Obstacle 2
obstacle3 = Obstacle(425, 325, 50, 50, (0, 0, 0), 'obstacle.png')   # Obstacle 3
obstacle4 = Obstacle(600, 600, 50, 50 , (0, 0, 0), 'obstacle.png')  # Obstacle 4

obstacles = [obstacle1, obstacle2, obstacle3, obstacle4]

# Character settings
character_width, character_height = 60, 60
character_x, character_y =  100 , 600
character_speed = 3 # pixels per frame
# Adding image for character
character_image = pygame.image.load('Soldier.png')
character_image = pygame.transform.scale(character_image, (character_width, character_height))

# Adding background
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Keeps character in the screen
character_x = max(0, min(screen_width - character_width, character_x))
character_y = max(0, min(screen_height - character_height, character_y))

# Score counter
score = 0
font = pygame.font.Font(None, 30)
score_x, score_y = 10, 10

# Wave counter
wave = 1
font = pygame.font.Font(None, 30)
wave_x, wave_y = 810, 10

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key states (movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # Keeps character inside the screen
    character_x = max(0, min(screen_width - character_width, character_x))
    character_y = max(0, min(screen_height - character_height, character_y))    

    # Keep enemy inside the screen
    enemy_1.x = max(0, min(screen_width - enemy_1.width, enemy_1.x))
    enemy_1.y = max(0, min(screen_height - enemy_1.height, enemy_1.y))
    enemy_2.x = max(0, min(screen_width - enemy_2.width, enemy_2.x))
    enemy_2.y = max(0, min(screen_height - enemy_2.height, enemy_2.y))
    enemy_3.x = max(0, min(screen_width - enemy_3.width, enemy_3.x))
    enemy_3.y = max(0, min(screen_height - enemy_3.height, enemy_3.y))

    # Drawing
    screen.fill(WHITE)  # Clear screen
    screen.blit(background_image, (0, 0))
    screen.blit(character_image, (character_x, character_y))  # Draw character

    def draw_enemy(enemy):
        # Draws enemy onto screen
        screen.blit(enemy.image, (enemy.x, enemy.y))

    for enemy in enemies:
        # Uses function on all enemies
        draw_enemy(enemy)
 
    def draw_obstacle(obstacle):
        # Draws obstacle onto screen
        screen.blit(obstacle.image, (obstacle.x, obstacle.y))

    for obstacle in obstacles:
        # Uses function on all obstacles
        draw_obstacle(obstacle) 

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (score_x, score_y))
    
    # Draw wave counter
    wave_text = font.render(f"Wave: {wave}", True, (0, 0, 0))
    screen.blit(wave_text, (wave_x, wave_y))
    pygame.display.flip()  # Update display once
    # Limit FPS
    clock.tick(60)
    
 
    
    # Collision detection between enemies and character
    def collision_detection_enemy_to_character(enemy, character_x, character_y):
        if (character_x < enemy.x + enemy.width and
         character_x + character_width > enemy.x and
        character_y < enemy.y + enemy.height and
        character_y + character_height > enemy.y):
            pygame.quit()
            print("Game Over! You reached wave", wave, "and got", score, "score")
            sys.exit()
    
    for enemy in enemies:
         # Uses function on all enemies
        collision_detection_enemy_to_character(enemy, character_x, character_y)


    # Obstacle collision detection against enemies
    def collision_detection_obstacles_to_enemy(enemy, obstacle):
        #  All obstacle collision detections on all enemies
        if (enemy.x < obstacle.x + obstacle.width and
         enemy.x + enemy.width > obstacle.x and
        enemy.y < obstacle.y + obstacle.height and
        enemy.y + enemy.height > obstacle.y):    
            # Collision response, move enemy back
            if enemy.x < obstacle.x + obstacle.width / 2:
                enemy.x -= enemy.speed
            else:
                enemy.x += enemy.speed
            if enemy.y < obstacle.y + obstacle.height / 2:
                enemy.y -= enemy.speed
            else:
                enemy.y += enemy.speed
    
    for enemy in enemies:
        for obstacle in obstacles:
        # Uses obstacle collision detection function on every obstacle for all enemies
            collision_detection_obstacles_to_enemy(enemy, obstacle)
            

    # Move enemies towards character
    def enemy_follow_user(enemy, character_x, character_y):
        if enemy.x < character_x:
            enemy.x += enemy.speed
        elif enemy.x > character_x:
            enemy.x -= enemy.speed
        if enemy.y < character_y:
            enemy.y += enemy.speed
        elif enemy.y > character_y:
            enemy.y -= enemy.speed        
    
    for enemy in enemies:
        # Uses movement function on all enemies
        enemy_follow_user(enemy, character_x, character_y)


# First obstacle collision detection against character
    if (character_x < obstacle1.x + obstacle1.width and
            character_x + character_width > obstacle1.x and
            character_y < obstacle1.y + obstacle1.height and
            character_y + character_height > obstacle1.y):
            # Collision response, move character back
            if keys[pygame.K_LEFT]:
                character_x += character_speed
            if keys[pygame.K_RIGHT]:
                character_x -= character_speed
            if keys[pygame.K_UP]:
                character_y += character_speed
            if keys[pygame.K_DOWN]:
                character_y -= character_speed 
# Second obstacle collision detection against character
    if (character_x < obstacle2.x + obstacle2.width and
            character_x + character_width > obstacle2.x and
            character_y < obstacle2.y + obstacle2.height and
            character_y + character_height > obstacle2.y):
            # Collision response, move character back
            if keys[pygame.K_LEFT]:
                character_x += character_speed
            if keys[pygame.K_RIGHT]:
                character_x -= character_speed
            if keys[pygame.K_UP]:
                character_y += character_speed
            if keys[pygame.K_DOWN]:
                character_y -= character_speed 
# Third obstacle collision detection against character
    if (character_x < obstacle3.x + obstacle3.width and
            character_x + character_width > obstacle3.x and
            character_y < obstacle3.y + obstacle3.height and
            character_y + character_height > obstacle3.y):
            #  Collision response, move character back
            if keys[pygame.K_LEFT]:
                character_x += character_speed
            if keys[pygame.K_RIGHT]:
                character_x -= character_speed
            if keys[pygame.K_UP]:
                character_y += character_speed
            if keys[pygame.K_DOWN]:
                character_y -= character_speed
# Fourth obstacle collision aginst character
    if (character_x < obstacle4.x + obstacle4.width and
            character_x + character_width > obstacle4.x and
            character_y < obstacle4.y + obstacle4.height and
            character_y + character_height > obstacle4.y):
            # Collision response, move character back
            if keys[pygame.K_LEFT]:
                character_x += character_speed
            if keys[pygame.K_RIGHT]:
                character_x -= character_speed
            if keys[pygame.K_UP]:
                character_y += character_speed
            if keys[pygame.K_DOWN]:
                character_y -= character_speed
   
   

  # Attack detection for enemy 1
    attack_range = 100  # attack range in pixels
    space_pressed = keys[pygame.K_SPACE]
    if space_pressed and (abs(character_x - enemy_1.x) < attack_range and
      
        abs(character_y - enemy_1.y) < attack_range):
        if (abs(character_x - enemy_1.x) < attack_range and
            abs(character_y - enemy_1.y) < attack_range):

        # Response for attacking the enemy
            enemy_1.x , enemy_1.y = random.randint(600, 800), random.randint(400, 600)  # moves the enemy to a random spot 
            print("Enemy defeated! +5 score")
        # Increase score for hitting the enemy
        score += 5
        wave = (score // 25) + 1
        if score == 200:
             pygame.quit
             print("You Win!")
    

    #  Attack detection for enemy 2
    if space_pressed and (abs(character_x - enemy_2.x) < attack_range and
        abs(character_y - enemy_2.y) < attack_range):
        if (abs(character_x - enemy_2.x) < attack_range and
            abs(character_y - enemy_2.y) < attack_range):

        # Response for attacking the enemy
            enemy_2.x , enemy_2.y = random.randint(600, 800), random.randint(400, 600)  # moves the enemy to a random spot 
            print("Enemy defeated! +5 score")
        # Increase score for hitting the enemy
        score += 5
        wave = (score // 25) + 1
        if score == 200:
            pygame.quit
            print("You Win!")
            sys.exit()        
        

    # Attack detection for enemy 3
    if space_pressed and (abs(character_x - enemy_3.x) < attack_range and
        abs(character_y - enemy_3.y) < attack_range):
        if (abs(character_x - enemy_3.x) < attack_range and
            abs(character_y - enemy_3.y) < attack_range):
        # Response for attacking the enemy
            enemy_3.x , enemy_3.y = random.randint(600, 800), random.randint(400, 600)  # moves the enemy to a random spot 
            print("Enemy defeated! +5 score")
    
        # Increase score for hitting the enemy
        score += 5
        wave = (score // 25) + 1
        if score == 200:
            pygame.quit()
            print("You Win!")
            sys.exit()


    # Attack detection for enemy 4
    if space_pressed and (abs(character_x - enemy_4.x) < attack_range and
        abs(character_y - enemy_4.y) < attack_range):
        if (abs(character_x - enemy_4.x) < attack_range and
            abs(character_y - enemy_4.y) < attack_range):

        # Response for attacking the enemy
            enemy_4.x , enemy_4.y = random.randint(600, 800), random.randint(400, 600)  # moves the enemy to a random spot 
            print("Enemy defeated! +5 score")
    
        # Increase score for hitting the enemy
        score += 5
        wave = (score // 25) + 1
        if score == 200:
            pygame.quit()
            print("You Win!")
            sys.exit()


    # Attack detection for enemy 5
    if space_pressed and (abs(character_x - enemy_5.x) < attack_range and
        abs(character_y - enemy_5.y) < attack_range):
        if (abs(character_x - enemy_5.x) < attack_range and
            abs(character_y - enemy_5.y) < attack_range):

        # Response for attacking the enemy
            enemy_5.x , enemy_5.y = random.randint(600, 800), random.randint(400, 600)  # moves the enemy to a random spot 
            print("Enemy defeated! +5 score")
    
        # Increase score for hitting the enemy
        score += 5
        wave = (score // 25) + 1
        if score == 200:
            pygame.quit()
            print("You Win!")
            sys.exit()