from vpython import *
from random import randrange

BOUNCE_RANDOM_LIMIT = 10
BALL_POSITION_FACTOR = 0.005
MARK_ARROW_SCALE_FACTOR = 0.1

BALL_COLOR = color.cyan
MARK_ARROW_COLOR = color.yellow

WALL_THICKNESS = 0.2
WALL_LENGTH = 12
WALL_COLOR = color.gray(0.5)


wall_right = box(pos=vector(WALL_LENGTH/2, 0, 0), size=vector(WALL_THICKNESS, WALL_LENGTH, WALL_LENGTH), color=WALL_COLOR)
wall_left = box(pos=vector(-WALL_LENGTH/2, 0, 0), size=vector(WALL_THICKNESS, WALL_LENGTH, WALL_LENGTH), color=WALL_COLOR)
wall_top = box(pos=vector(0, WALL_LENGTH/2, 0), size=vector(WALL_LENGTH, WALL_THICKNESS, WALL_LENGTH), color=WALL_COLOR)
wall_bottom = box(pos=vector(0, -WALL_LENGTH/2, 0), size=vector(WALL_LENGTH, WALL_THICKNESS, WALL_LENGTH), color=WALL_COLOR)
wall_back = box(pos=vector(0, 0, -WALL_LENGTH/2), size=vector(WALL_LENGTH, WALL_LENGTH, WALL_THICKNESS), color=WALL_COLOR)
wall_front_pos = vector(0, 0, WALL_LENGTH/2)

ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=BALL_COLOR, make_trail=False)
ball.velocity = vector(25, 0, 0)
ball.pos = ball.pos + ball.velocity * BALL_POSITION_FACTOR

mark_arrow = arrow(pos=ball.pos, axis=MARK_ARROW_SCALE_FACTOR * ball.velocity, color=MARK_ARROW_COLOR)


def bounce_random():
    return randrange(-BOUNCE_RANDOM_LIMIT, BOUNCE_RANDOM_LIMIT)


while True:
    rate(60)

    # DETECT COLLISION WITH RIGHT AND LEFT WALL
    if ball.pos.x > (wall_right.pos.x - WALL_THICKNESS) \
            or ball.pos.x < (wall_left.pos.x + WALL_THICKNESS):
        ball.velocity.x = -ball.velocity.x
        ball.velocity = vector(ball.velocity.x, bounce_random(), bounce_random())

    # DETECT COLLISION WITH TOP AND BOTTOM WALL
    if ball.pos.y > (wall_top.pos.y - WALL_THICKNESS) \
            or ball.pos.y < (wall_bottom.pos.y + WALL_THICKNESS):
        ball.velocity.y = -ball.velocity.y
        ball.velocity = vector(ball.velocity.x, ball.velocity.y, bounce_random())

    # DETECT COLLISION WITH BACK AND FRONT WALL
    if ball.pos.z < (wall_back.pos.z - WALL_THICKNESS) \
            or ball.pos.z > (wall_front_pos.z + WALL_THICKNESS):
        ball.velocity.z = -ball.velocity.z
        ball.velocity = vector(ball.velocity.x, bounce_random(), ball.velocity.z)

    mark_arrow.pos = ball.pos
    mark_arrow.axis = ball.velocity * MARK_ARROW_SCALE_FACTOR

    ball.pos = ball.pos + ball.velocity * BALL_POSITION_FACTOR
