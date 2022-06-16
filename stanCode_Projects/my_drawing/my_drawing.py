"""
File: my_drawing
Name: 林志叡
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
SIZE = 15
window = GWindow(800, 500, title='Mosaic Micky')


def main():
    """
    title:mosaic micky
    Assemble the famous micky mouse in black and white bricks
    """
    #background
    for i in range(int(window.width/SIZE)):
        for j in range(int(window.height/SIZE)):
            oval = GRect(SIZE, SIZE)
            oval.filled = True
            oval.fill_color = 'white'
            window.add(oval, x=i*oval.width, y=j*oval.height)
    for i in range(int(window.width/SIZE)):
        for j in range(int(window.height/SIZE)):
            if (i+j)%2 != 0:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.fill_color = 'black'
                window.add(oval, x=i*oval.width, y=j*oval.height)

    # following are graph which used double for loop to assemble rect into circle, oval and semiellipse
    # mickyface
    for i in range(-16,16,1):
        for j in range(-16,16,1):
            if i**2+j**2 <= 16**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width/SIZE/2)*SIZE+i*oval.width, y=int(window.height/SIZE
                                                                                     /2)*SIZE+j*oval.height)
    #micky ears
    for i in range(-8,8,1):
        for j in range(-8,8,1):
            if i**2+j**2 <= 8**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width/SIZE/4)*SIZE+i*oval.width,
                           y=int(window.height/SIZE/100)*SIZE+j*oval.height)
    for i in range(-8, 8, 1):
        for j in range(-8, 8, 1):
            if i ** 2 + j ** 2 <= 8 ** 2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width / SIZE * 170 / 1550) * SIZE+i*oval.width,
                           y=int(window.height/SIZE/2)*SIZE+j*oval.height)

    # micky inner face
    for i in range(-11,11,1):
        for j in range(-11,11,1):
            if i**2+j**2 <= 9 **2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'white'
                window.add(oval, x=int(window.width / SIZE * 9.5 / 16) * SIZE+i*oval.width,
                           y=int(window.height/SIZE*3/8)*SIZE+j*oval.height)
    for i in range(-11,11,1):
        for j in range(-11,11,1):
            if i**2+j**2 <= 11**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'white'
                window.add(oval, x=int(window.width / SIZE / 2) * SIZE + i * oval.width,
                           y=int(window.height / SIZE * 6 / 8) * SIZE + j * oval.height)
    # micky eyes
    for i in range(-5,5,1):
        for j in range(-5,5,1):
            if 4*i**2+j**2 <= 3**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width / SIZE * 9/ 16) * SIZE + i * oval.width,
                           y=int(window.height / SIZE /2.5) * SIZE + j * oval.height)
    for i in range(-5,5,1):
        for j in range(-5,5,1):
            if 4*i**2+j**2 <= 3**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width / SIZE * 11/ 16) * SIZE + i * oval.width,
                           y=int(window.height / SIZE /2.5) * SIZE + j * oval.height)
# micky nose
    for i in range(-7, 7, 1):
        for j in range(-7, 7, 1):
            if i ** 2 + 2 * j ** 2 <= 7 ** 2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'white'
                window.add(oval, x=int(window.width / SIZE * 11.5/ 16) * SIZE + i * oval.width,
                           y=int(window.height / SIZE* 5/8) * SIZE + j * oval.height)
    for i in range(-5,5,1):
        for j in range(-3,3,1):
            if i**2+5*j**2 <= 5**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width / SIZE * 13/ 16) * SIZE + i * oval.width,
                           y=int(window.height / SIZE*3 /5) * SIZE + j * oval.height)
# micky mouth
    for i in range(-6,6,1):
        for j in range(0,6,1):
            if i**2+2*j**2 <= 6**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'black'
                window.add(oval, x=int(window.width / SIZE * 9/ 16) * SIZE + i * oval.width,
                           y=int(window.height / SIZE*4 /5) * SIZE + j * oval.height)
    for i in range(-6,6,1):
        for j in range(0,6,1):
            if i**2+2*j**2 <= 3**2:
                oval = GRect(SIZE, SIZE)
                oval.filled = True
                oval.color = 'black'
                oval.fill_color = 'grey'
                window.add(oval, x=int(window.width / SIZE * 9/ 16) * SIZE + i * oval.width,
                           y=int(window.height / SIZE*4 /5) * SIZE + j * oval.height)


if __name__ == '__main__':
    main()
