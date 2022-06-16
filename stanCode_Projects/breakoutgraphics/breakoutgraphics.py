"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

name : 林志叡
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'grey'
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'white'
        # Default initial velocity for the ball
        self.__vx = 0
        self.__vy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.drop_ball)
        onmousemoved(self.mouse)
        # Draw bricks
        # Double for loop to create bricks and set different colors in each row
        for i in range(brick_rows):
            for j in range(brick_cols):
                if j < 2:
                    self.brickij1 = GRect(brick_width, brick_height)
                    self.window.add(self.brickij1, x=i * (brick_width + brick_spacing),
                                    y=j * (brick_height + brick_spacing))
                    self.brickij1.filled = True
                    self.brickij1.fill_color = 'peru'
                elif j < 5:
                    self.brickij2 = GRect(brick_width, brick_height)
                    self.window.add(self.brickij2, x=i * (brick_width + brick_spacing),
                                    y=j * (brick_height + brick_spacing))
                    self.brickij2.filled = True
                    self.brickij2.fill_color = 'khaki'
                else:
                    self.brickij3 = GRect(brick_width, brick_height)
                    self.window.add(self.brickij3, x=i * (brick_width + brick_spacing),
                                    y=j * (brick_height + brick_spacing))
                    self.brickij3.filled = True
                    self.brickij3.fill_color = 'ivory'

        # place the element on window
        self.window.add(self.paddle, x=window_width / 2 - self.paddle.width / 2,
                        y=window_height - paddle_offset)
        self.window.add(self.ball, x=window_width / 2 - self.ball.width / 2,
                        y=window_height / 2 - self.ball.height / 2)

    # ---------------------------------method--------------------------------------------
    def mouse(self, mouse):
        # control the paddle and set limitation when the border of paddle is out of  window
        if mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def drop_ball(self, event):
        # when ball is not falling, player can click the mouse to set ball velocity
        if self.__vy == 0:
            self.__vx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__vx *= -1
            self.__vy = -1 * INITIAL_Y_SPEED

    def move(self):
        # move
        self.ball.move(self.__vx, self.__vy)

    def collision_wall(self):
        #  when ball collide the wall then reverse the velocity of the ball
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__vx *= -1
        if self.ball.y <= 0:
            self.__vy *= -1

    def reset(self):
        #  when the ball is below the horizon then reset ball to begin position and set velocity to zero
        self.__vx = 0
        self.__vy = 0
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2

    def collision_object(self):
        # Detect the corner of the ball if collide any object(using window.get_object_at)
        # when object is not none or paddle then remove the bricks
        # when collide to bricks or paddle then reverse the velocity of ball
        maybe_obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
        maybe_obj_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width)
        if maybe_obj_1 is not None:
            if maybe_obj_1 != self.paddle:
                self.__vy *= -1
                self.window.remove(maybe_obj_1)
            elif maybe_obj_1 == self.paddle:
                if self.__vy >= 0:
                    self.__vy *= -1
        else:
            if maybe_obj_2 is not None:
                if maybe_obj_2 != self.paddle:
                    self.__vy *= -1
                    self.window.remove(maybe_obj_2)
                elif maybe_obj_2 == self.paddle:
                    if self.__vy >= 0:
                        self.__vy *= -1
            else:
                if maybe_obj_3 is not None:
                    if maybe_obj_3 != self.paddle:
                        self.__vy *= -1
                        self.window.remove(maybe_obj_3)
                    elif maybe_obj_3 == self.paddle:
                        if self.__vy >= 0:
                            self.__vy *= -1
                else:
                    if maybe_obj_4 is not None:
                        if maybe_obj_4 != self.paddle:
                            self.__vy *= -1
                            self.window.remove(maybe_obj_4)
                        elif maybe_obj_4 == self.paddle:
                            if self.__vy >= 0:
                                self.__vy *= -1

    def below_horizon(self):
        # Detect if the ball is under horizon of the window
        x = self.ball.y > self.window.height
        return x
