import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 400]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                       Vector2(random.randint(
                           20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                       Vector2(4*random.random() - 2, 4*random.random() - 2),
                       [255, 10, 0], 20)
    object_list.append(kinetic)

    block = KineticBlock(Vector2(200, 200), 100, 100, [0, 0, 255])
    object_list.append(block)

    paddle = KineticBlock(Vector2(400, 400), 220, 100, [0, 255, 0])
    object_list.append(paddle)


def test_something(object_list):
    for brick in range(10):
        block = KineticBlock(Vector2(random.randint(
            20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)), 100, 50, [0, 0, 255])
    object_list.append(block)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)
    test_something(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            print('Move the paddle LEFT')
            object_list[2].rectangle.move_ip(-1, 0)
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            print('Move the paddle RIGHT')
            object_list[2].rectangle.move_ip(1, 0)
            pass

        for object in object_list:
            object.update()
            object.check_collision()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
