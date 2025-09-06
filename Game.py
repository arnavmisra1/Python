import pygame
import random
import math
from pygame import mixer

#calling all functions in pygame
pygame.init()

#screen setup
screen = pygame.display.set_mode((800, 600))

#icon and title
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Background.jpg')

#add music
mixer.music.load('background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)


#player
img_player = pygame.image.load('rocket.png')
player_x = 368
player_y = 500
player_x_change = 0



#enemy
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 7


for e in range(number_of_enemies):
    img_enemy.append(pygame.image.load('skull.png'))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    enemy_x_change.append(1)
    enemy_y_change.append(50)


#bullet
img_bullet = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 1
visible_bullet = False

#score
score = 0
my_font = pygame.font.Font('freesansbold.ttf', 20)
text_x = 10
text_y = 10

# End of game text
end_font = pygame.font.Font('freesansbold.ttf', 40)

def final_text():
    my_final_font = end_font.render("Game Over :((", True, (255,255,255))
    screen.blit(my_final_font, (200,200))




#show score function
def show_score(x, y):
    text = my_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))

#player function
def player(x, y):
    screen.blit(img_player, (x, y))

#enemy function
def enemy(x, y, en):
    screen.blit(img_enemy[en], (x, y))

#shoot bullet
def shoot_bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x+16, y+10))

#detect collision
def there_is_a_collision(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance < 27:
        return True
    else:
        return False


#game loop
is_running = True

while is_running:
    #Background
    screen.blit(background, (0, 0))

    #event iteration
    for event in pygame.event.get():
        #closing event
        if event.type == pygame.QUIT:
            is_running = False

        #press key up and release key cases
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('shot.mp3')
                bullet_sound.play()
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0


    #modify player location
    player_x += player_x_change

    #keep player inside screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # modify enemy location
    for enem in range(number_of_enemies):
        #end of game
        if enemy_y[enem] > 500:
            for k in range(number_of_enemies):
                enemy_y[k] = 1000
            final_text()
            break
        enemy_x[enem] += enemy_x_change[enem]

    # keep enemy inside screen
        if enemy_x[enem] <= 0:
            enemy_x_change[enem] = 0.2
            enemy_y[enem] += enemy_y_change[enem]
        elif enemy_x[enem] >= 736:
            enemy_x_change[enem] = -0.2
            enemy_y[enem] += enemy_y_change[enem]

        # collision
        collision = there_is_a_collision(enemy_x[enem], enemy_y[enem], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound('punch.mp3')
            collision_sound.play()
            bullet_y = 500
            visible_bullet = False
            score += 1
            enemy_x[enem] = random.randint(0, 736)
            enemy_y[enem] = random.randint(50, 200)

        enemy(enemy_x[enem], enemy_y[enem], enem)


    #bullets movement
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False
    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change





    player(player_x, player_y)
    show_score(text_x, text_y)


    #update
    pygame.display.update()

