"""
Starter code for a simple Pygame Pong game that will be finished and exported to the web
using the pygbag library.
First Last - Month Year
"""

import asyncio
import pygame

async def main():
    # Game constants and variables
    WINDOW_TITLE: str = "Pong Starter"
    SCREEN_DIMENSIONS: tuple = (800, 600)
    FPS: int = 60

    BALL_RADIUS: int = 15
    BALL_COLOR: tuple = (255, 255, 255)
    ball_speed: list[int] = [2, -4]
    ball_location: list[int] = [SCREEN_DIMENSIONS[0] // 2, SCREEN_DIMENSIONS[1] // 2]

    LEFT_PADDLE_DIMENSIONS: tuple = (15, 100)
    LEFT_PADDLE_OFFSET: int = 30 # distance from left edge of screen
    LEFT_PADDLE_COLOR: tuple = (255, 255, 255)
    left_paddle: pygame.Rect = pygame.Rect(LEFT_PADDLE_OFFSET,
                                        SCREEN_DIMENSIONS[1] // 2 - LEFT_PADDLE_DIMENSIONS[1] // 2,
                                        LEFT_PADDLE_DIMENSIONS[0], LEFT_PADDLE_DIMENSIONS[1])


    BG_COLOR: tuple = (0, 0, 0)
    

    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption(WINDOW_TITLE)
    clock: pygame.Clock = pygame.time.Clock()

    # MAIN GAME LOOP
    running: bool = True
    while running:

        # update the ball
        # check for top wall boundary
        if ball_location[1] - BALL_RADIUS <= 0:
            ball_speed[1] *= -1
        # Check for bottom wall boundary
        if ball_location[1] + BALL_RADIUS >= SCREEN_DIMENSIONS[1]:
            ball_speed[1] *= -1
        # Check for right wall boundary
        if ball_location[0] + BALL_RADIUS >= SCREEN_DIMENSIONS[0]:
            ball_speed[0] *= -1

        ball_location[0] += ball_speed[0]
        ball_location[1] += ball_speed[1]

        # DRAW
        screen.fill(BG_COLOR) # background
        pygame.draw.rect(screen, LEFT_PADDLE_COLOR, left_paddle) # paddle
        pygame.draw.circle(screen, BALL_COLOR, ball_location, BALL_RADIUS) # ball

        pygame.display.flip() # update screen

        await asyncio.sleep(0) # necessary for pygbag

        clock.tick(FPS)

    pygame.quit()


# this will allow us to pybag
asyncio.run(main())