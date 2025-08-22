#completed, some bugs tho, will fix later (probably never lol)

import pygame, sys, random

# setup
pygame.mixer.pre_init(44100,-16,1, 1024)
pygame.init()
clock = pygame.time.Clock()

#gamezone
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PONG by VEDANSH SHARMA")


#rectssss
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#colorssssss
bg_color = pygame.Color('black')
bluish_black = (0,0,139)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
black = (0,0,0)
white = (255,255,255)


ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7


#function for animation
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(bounce_sound)
        ball_speed_y *= -1



    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:    
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
 


    if ball.colliderect(opponent) and ball_speed_y < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

#opponent animation functionnn
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    

#ball reset mechanic
def ball_restart():
    global ball_speed_x, ball_speed_y, current_time, score_time

    current_time = pygame.time.get_ticks()

    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("Start in:(3)",False, white )
        screen.blit(number_three,(screen_width/2 - 100, screen_height/2 + 20))
    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("Start in:(2)",False, white )
        screen.blit(number_two,(screen_width/2 - 100, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("start in:(1)",False, white )
        screen.blit(number_one,(screen_width/2 - 100, screen_height/2 + 20))


    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None

#player animation function
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


#text variabless
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

#sound channel
pong_sound = pygame.mixer.Sound("assets/hitt.wav")
score_sound = pygame.mixer.Sound("assets/score.ogg")
bounce_sound = pygame.mixer.Sound("assets/bounce.ogg")


#timer
score_time = True

while True:
    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed += 10
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed -= 10
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed += 10


    #logixxx
    ball_animation()
    player_animation()
    opponent_animation()

    
    #visualssss
    screen.fill(bg_color)
    pygame.draw.rect(screen, bluish_black, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, green, ball)
    pygame.draw.aaline(screen, white, (screen_width/2,0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()


    player_text = game_font.render(f"{player_score}", False, white)
    screen.blit(player_text,(700,384))

    opponent_text = game_font.render(f"{opponent_score}", False, white)
    screen.blit(opponent_text,(652,384))


    # updating
    pygame.display.flip()
    clock.tick(60)