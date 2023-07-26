import pygame
import random
import sys
from pygame.locals import *

images = {}
sounds = {}
number = {}
fps = 40

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


def isCollide(playery, bird_rect, hurele_rect, new_hurdle_rect):
    if playery <= 0 or playery >= 525 - images['player'].get_height():
        sounds['die'].play()
        return True

    if bird_rect.colliderect(hurele_rect):
        sounds['die'].play()
        return True
    if bird_rect.colliderect(new_hurdle_rect):
        sounds['die'].play()
        return True


def get_hurdle():
    hurdle_x = screen_width + 10
    hurdle_y = random.randrange(0, 525 - images['hurdle1'].get_height())
    return {'x': hurdle_x, 'y': hurdle_y}


def main_game():

    player_x = screen_width / 10
    player_y = (screen_height - images['player'].get_height()) / 2

    player_velocity_down = -3
    player_velocity_up = -45

    hurdle_velocity = -3
    new_hurdle = get_hurdle()
    hurdle = new_hurdle



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_SPACE):
                if player_y > 0:
                    player_y += player_velocity_up
                    sounds['fly'].play()

        if hurdle['x'] == 104:
            new_hurdle = get_hurdle()

        if hurdle['x'] == -175:
            hurdle = get_hurdle()

        player_y -= player_velocity_down
        hurdle['x'] += hurdle_velocity
        new_hurdle['x'] += hurdle_velocity

        bird_rect = pygame.Rect(player_x, player_y, images['player'].get_width()-30, images['player'].get_height()-30)
        hurdle_rect = pygame.Rect(hurdle['x'], hurdle['y'], images['hurdle1'].get_width()-100, images['hurdle1']
                                  .get_height()-50)
        new_hurdle_rect = pygame.Rect(new_hurdle['x'], new_hurdle['y'], images['hurdle1'].get_width()-100,
                                      images['hurdle1'].get_height()-50)

        crash_test = isCollide(player_y, bird_rect, hurdle_rect, new_hurdle_rect)

        if crash_test:
            return True
        screen.blit(images['background'], (0, 0))
        screen.blit(number['2'], ((screen_width - number['0'].get_width()) / 2, 20))
        screen.blit(images['player'], (player_x, player_y))
        screen.blit(images['hurdle1'], (hurdle['x'], hurdle['y']))
        screen.blit(images['hurdle1'], (new_hurdle['x'], new_hurdle['y']))
        pygame.display.update()
        fps_clock.tick(fps)


def welcome():
    # Calculating initial position of the bird and hurdle
    player_x = int(screen_width / 10)
    player_y = int(((screen_height - images['player'].get_height()) / 2))
    hurdle_x = int(screen_width / 2)
    hurdle_y = int((screen_height - images['hurdle1'].get_height()) / 2)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                print('Exit')
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

        screen.blit(images['background'], (0, 0))
        screen.blit(images['start'], (75, 20))
        screen.blit(images['player'], (player_x, player_y,))
        screen.blit(images['hurdle1'], (hurdle_x, hurdle_y))
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == "__main__":
    pygame.init()  # initializing pygame modules
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird by Ritesh kr. Gupta")

    images['player'] = pygame.transform.scale(pygame.image.load('Gallary/Bird.png').convert_alpha(), (50, 50))
    number['0'] = pygame.transform.scale(pygame.image.load('Gallary/0.png').convert_alpha(), (30, 30))
    number['1'] = pygame.transform.scale(pygame.image.load('Gallary/1.png').convert_alpha(), (30, 30))
    number['2'] = pygame.transform.scale(pygame.image.load('Gallary/2.png').convert_alpha(), (30, 30))
    number['3'] = pygame.transform.scale(pygame.image.load('Gallary/3.png').convert_alpha(), (30, 30))
    number['4'] = pygame.transform.scale(pygame.image.load('Gallary/4.png').convert_alpha(), (30, 30))
    number['5'] = pygame.transform.scale(pygame.image.load('Gallary/5.png').convert_alpha(), (30, 30))
    number['6'] = pygame.transform.scale(pygame.image.load('Gallary/6.png').convert_alpha(), (30, 30))
    number['7'] = pygame.transform.scale(pygame.image.load('Gallary/7.png').convert_alpha(), (30, 30))
    number['8'] = pygame.transform.scale(pygame.image.load('Gallary/8.png').convert_alpha(), (30, 30))
    number['9'] = pygame.transform.scale(pygame.image.load('Gallary/9.png').convert_alpha(), (30, 30))
    images['background'] = pygame.transform.scale(pygame.image.load('Gallary/Background.png').convert_alpha(),
                                                  (400, 600))
    images['start'] = pygame.transform.scale(pygame.image.load('Gallary/start.png').convert_alpha(), (250, 250))
    images['hurdle1'] = pygame.transform.scale(pygame.image.load('Gallary/Hurdle.png').convert_alpha(), (280, 188))

    sounds['die'] = pygame.mixer.Sound('Sounds/kill_sound.wav')
    sounds['background'] = pygame.mixer.Sound('Sounds/bg_sound.wav')
    sounds['fly'] = pygame.mixer.Sound('Sounds/flying.wav')

    while True:
        welcome()
        crash = main_game()
        if crash:
            welcome()
