"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

name : 林志叡
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts
COUNT = NUM_LIVES


def main():
    global COUNT
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    label_win = GLabel('You Win!')
    label_lose = GLabel('Game Over')
    while True:
        # Check whether ball is below the horizon or not, if below horizon num of lives -=1
        if graphics.below_horizon():
            COUNT -= 1
            # If num of lives > 0 then reset position of ball , if < 0 then break
            if COUNT > 0:
                graphics.reset()
            else:
                break
        # Ball animation : move -> check collision condition(including wall and object)
        graphics.move()
        graphics.collision_wall()
        graphics.collision_object()
        pause(FRAME_RATE)

    if COUNT == 0:
        graphics.window.add(label_lose, x=graphics.window.width/2-label_lose.width/2, y=graphics.window.height/2)

if __name__ == '__main__':
    main()
