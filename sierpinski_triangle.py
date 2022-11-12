"""sierpinski_triangle drawing."""

import random

from coordinates import Coordinate as coord
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt

TRIANGLE = (coord((2000,1000), order='xy'),
           coord((8000,900), order='xy'),
           coord((500,8000), order='xy')
           )
XMAX = 10000
YMAX = 10000
ROUNDS = 3000


def get_random_start(triangle) -> coord:
    """ Returns coordinates of a random point within the traingle.

    Args:
        triangle: A tuple of 3 coord of the vertices.

    Returns:
        coord of the point within the triangle.
    """
    t1, t2, t3 = triangle
    v2, v3  = t2 - t1, t3 - t1
    try_again = True
    while try_again:
        a = random.random()
        b = random.random()
        if a + b < 1:
            try_again = False
    new_coord =  t1 + a * v2 + b * v3
    return new_coord


def get_next_point(triangle, last_coord) -> coord:
    """ Returns coordinates of the next point.

    Takes random vertex of the triangle and returns point
    half distance between last_coord and the vertex.

    Args:
        triangle: A tuple of 3 coord coordinates.
        last_coord: A coordinate of a point within the traingle.

    Returns:
        coord of the point half distance between
        last_coord and random vertex.
    """
    corner = triangle[random.randint(0,2)]
    new_coord = last_coord + (corner - last_coord)/2
    return new_coord


def new_striangle():
    """ Returns all points of a Sierpinski triangle."""
    new_points = []
    new_points.extend(TRIANGLE)
    last_coord = get_random_start(TRIANGLE)
    for _ in range(ROUNDS):
        last_coord = get_next_point(TRIANGLE, last_coord)
        new_points.append(last_coord)
    return new_points

def init():
    ax.set_visible(False)
    ax.set_xlim(0, XMAX)
    ax.set_ylim(0, YMAX)
    return ln,

def update(crd):
    x_data.append(crd.x)
    y_data.append(crd.y)
    ln.set_data(x_data, y_data)
    return ln,


if __name__ == "__main__":

    random.seed()
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    ln, = plt.plot([], [], 'ro', markersize=1)

    all_points = new_striangle()
    ani = FuncAnimation(fig, update, frames=all_points,
                    init_func=init, interval=1, blit=True)

    plt.show()
