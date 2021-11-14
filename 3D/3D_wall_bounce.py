from vpython import *

BALL_POSITION_FACTOR = 0.005
MARK_ARROW_SCALE_FACTOR = 0.1
BALL_COLOR = color.cyan
MARK_ARROW_COLOR = color.yellow

WALL_THICKNESS = 0.5
WALL_LENGTH = 12
WALL_COLOR = color.gray(0.5)


wall_right = box(pos=vector(WALL_LENGTH/2, 0, 0), size=vector(WALL_THICKNESS, WALL_LENGTH, WALL_LENGTH), color=WALL_COLOR)
wall_left = box(pos=vector(-WALL_LENGTH/2, 0, 0), size=vector(WALL_THICKNESS, WALL_LENGTH, WALL_LENGTH), color=WALL_COLOR)

ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=BALL_COLOR, make_trail=False)
ball.velocity = vector(25, 0, 0)
ball.pos = ball.pos + ball.velocity * BALL_POSITION_FACTOR


while True:
    rate(60)

    # DETECT COLLISION WITH RIGHT AND LEFT WALL
    if ball.pos.x > (wall_right.pos.x - WALL_THICKNESS) \
            or ball.pos.x < (wall_left.pos.x + WALL_THICKNESS):
        ball.velocity.x = -ball.velocity.x

    ball.pos = ball.pos + ball.velocity * BALL_POSITION_FACTOR
