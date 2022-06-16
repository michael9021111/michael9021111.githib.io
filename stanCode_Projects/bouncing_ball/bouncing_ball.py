"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# global variable

VX = 3
DELAY = 3
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
VY = 0
count_limit = 3
break_count = 0
count = count_limit
can_click = 1
# set global variable count_limit to limit bouncing time
# set global variable count, break_count to calculate bounce time and show the left bounce time on left window


window = GWindow(800, 500, title='bouncing_ball.py')
label = GLabel('count: ' + str(count))
rect = GOval(SIZE, SIZE)
rect.filled = True
rect.color = 'black'


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(label, x=0, y=label.height)
    window.add(rect, START_X, START_Y)
    if break_count < count_limit and count > 0:
        if can_click == 1:
            onmouseclicked(drop)


def drop(mouse):
    global VY
    global break_count
    global count
    global can_click
    if break_count < count_limit:
        if can_click == 1:
        # Only bounce when number of break_count less than limit
            while True:
                VY += GRAVITY
                rect.x = rect.x + VX
                rect.y = rect.y + VY
                pause(DELAY)
                if rect.y >= window.height:
                    VY = -0.9 * VY
                    can_click = 0
                    # When ball was reflected from the ground, velocity times -0.9
                if rect.x >= window.width:
                    # When ball bounce out of window, ball set back to original point
                    # variable count -1 and replace the label text
                    # break_count +1 to control the left chances
                    rect.x = START_X
                    rect.y = START_Y
                    break_count += 1
                    count -= 1
                    label.text = 'count: ' + str(count)
                    can_click = 1
                    break


if __name__ == "__main__":
    main()
