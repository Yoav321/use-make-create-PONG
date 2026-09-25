"""
Starter code for a simple Pygame Pong game that will be finished and exported to the web
using the pygbag library.
Yoav Bierkatz - September 2026
"""

import asyncio
import pygame

async def main():
    # Game constants and variables
    WINDOW_TITLE: str = "Pong Starter"
    SCREEN_DIMENSIONS: tuple = (800, 600)
    FPS: int = 60

    BALL_RADIUS: int = 10
    BALL_COLOR: tuple = (255, 255, 255)
    ball_speed: list[int] = [4, -6]
    ball_location: list[int] = [SCREEN_DIMENSIONS[0] // 2, SCREEN_DIMENSIONS[1] // 2]

    LEFT_PADDLE_DIMENSIONS: tuple = (15, 100)
    LEFT_PADDLE_OFFSET: int = 30 # distance from left edge of screen
    LEFT_PADDLE_COLOR: tuple = (255, 255, 255)
    LEFT_PADDLE_SPEED: float = 8
    left_paddle: pygame.Rect = pygame.Rect(LEFT_PADDLE_OFFSET,
                                        SCREEN_DIMENSIONS[1] // 2 - LEFT_PADDLE_DIMENSIONS[1] // 2,
                                        LEFT_PADDLE_DIMENSIONS[0], LEFT_PADDLE_DIMENSIONS[1])
    RIGHT_PADDLE_DIMENSIONS: tuple = (15, 100)
    RIGHT_PADDLE_OFFSET: int = 770
    RIGHT_PADDLE_COLOR: tuple = (255,255,255)
    RIGHT_PADDLE_SPEED: float = 8
    right_paddle: pygame.Rect = pygame.Rect(RIGHT_PADDLE_OFFSET,
                                            SCREEN_DIMENSIONS[1] // 2 - RIGHT_PADDLE_DIMENSIONS[1] // 2,
                                            RIGHT_PADDLE_DIMENSIONS[0], RIGHT_PADDLE_DIMENSIONS[1])



    BG_COLOR: tuple = (0, 0, 0)
    

    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption(WINDOW_TITLE)
    clock: pygame.Clock = pygame.time.Clock()

    # MAIN GAME LOOP
    running: bool = True
    while running:

        pressed: list[bool] = pygame.key.get_pressed()
        
        if pressed[pygame.K_w] and left_paddle.top >= 0:
            left_paddle.top -= LEFT_PADDLE_SPEED
        
        if pressed[pygame.K_s] and left_paddle.bottom <= SCREEN_DIMENSIONS[1]:
            left_paddle.top += LEFT_PADDLE_SPEED       

        if pressed[pygame.K_UP] and right_paddle.top >= 0:
            right_paddle.top -= RIGHT_PADDLE_SPEED
        
        if pressed[pygame.K_DOWN] and right_paddle.bottom <= SCREEN_DIMENSIONS[1]:
            right_paddle.top += RIGHT_PADDLE_SPEED           

        # update the ball
        # check for top wall boundary  
        if check_ball_top_bottom_border(ball_location, BALL_RADIUS, SCREEN_DIMENSIONS):
            ball_speed[1] *= -1

        #Check for left paddle
        if check_ball_paddle_collision(ball_location, BALL_RADIUS, left_paddle):
            ball_speed[0] *= -1

        # Check for right paddle
        if check_ball_paddle_collision(ball_location, BALL_RADIUS, right_paddle):
            ball_speed[0] *= -1    



        ball_location[0] += ball_speed[0]
        ball_location[1] += ball_speed[1]


        # DRAW
        screen.fill(BG_COLOR) # background
        pygame.draw.rect(screen, LEFT_PADDLE_COLOR, left_paddle) # paddle
        pygame.draw.rect(screen, RIGHT_PADDLE_COLOR, right_paddle)
        pygame.draw.circle(screen, BALL_COLOR, ball_location, BALL_RADIUS) # ball

        pygame.display.flip() # update screen

        await asyncio.sleep(0) # necessary for pygbag

        clock.tick(FPS)
        pygame.event.pump()
    pygame.quit()


def check_ball_top_bottom_border(location: list[float],
                                radius: float, 
                                screen_dims: tuple) -> bool:
    """
    Checks whether the ball hits the top or bottom border

    Parameter:
        location :list[float] - the current location of the ball[x,y]
        radius : float - the ball radius 
        screen_dims: tuple - the size of the screen (w,h)
    
    Returns:
        Whether the ball is hitting a top or bottom border
    """
        # Checks for top boundary
    if location[1] - radius <= 0:
        return True
        
        # Check for bottom wall boundary
    if location[1] + radius >= screen_dims[1]:
        return True

    return False

def check_ball_paddle_collision(ball_location: list[float],
                                ball_radius: float,
                                paddle: pygame.Rect) -> bool:
    """
    Checks wether a ball has collided with a paddle
    Parameters: 
        ball_location: list [float] - location of the ball [x,y]
        ball_radius: float - the size of the ball
        paddle: pygame.Rect - A Rectangle object representing a paddle 

    Returns
        Whether the ball is colliding with any paddle edge
    """
    #check left edge of ball hitting paddle
    if ball_location[0] - ball_radius <= paddle.right and\
        ball_location[0] - ball_radius >= paddle.left and\
        ball_location[1] + ball_radius >= paddle.top and\
        ball_location[1] - ball_radius <= paddle.bottom:
        return True
    
    #check right edge of ball hitting paddle
    if ball_location[0] + ball_radius >= paddle.left and\
        ball_location[0] + ball_radius <= paddle.right and\
        ball_location[1] + ball_radius >= paddle.top and\
        ball_location[1] - ball_radius <= paddle.bottom:
        return True

    return False
    
        
# this will allow us to pybag
asyncio.run(main())