import pygame
import os # Using this to help define path to images
from config import *
from sprites import *

# User events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
   
    # Draw the background
    WIN.blit(SPACE, (0, 0))
    
    # Draw the middle border
    pygame.draw.rect(WIN, BLACK, BORDER) # Argurments are surface you're drawing on, a color, and a rectangle
    
    # Draw health meters
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE) # 1 is for antialiasing
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE) 
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    # Draw the spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # Use blit when you draw a surface onto a screen
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    # Draw the bullets
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()

def yellow_movement_handle(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL    
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # DOWN
        yellow.y += VEL
        
def red_movement_handle(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL >0: # UP
        red.y -= VEL    
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # DOWN
        red.y += VEL

'''
This function will move the bullets, handle bullet collision, 
and remove bullets when they collide or go off-screen.
Loop through bullet lists and check for collision.
'''
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
            
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) 
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        # Control framerate
        clock.tick(FPS)
        # Event loop
        for event in pygame.event.get():
            # Usually check for quit first
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)                   
                    BULLET_FIRE_SOUND.play()
            
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
                
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        
        winner_text = ""
        
        if red_health <= 0:
            winner_text = "Yellow Wins"
        if yellow_health <= 0:
            winner_text = "Red Wins"
        if winner_text != "":
            draw_winner(winner_text)  
            break 
            
        
        # This method allows you to press multiple keys at once
        keys_pressed = pygame.key.get_pressed()
        yellow_movement_handle(keys_pressed, yellow)
        red_movement_handle(keys_pressed, red)
                
        handle_bullets(yellow_bullets, red_bullets, yellow, red)        
                
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
    main()
    
if __name__ == "__main__":
    main()