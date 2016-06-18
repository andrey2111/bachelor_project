from cmath import rect, phase
from math import ceil

import numpy as np
from numpy import pi

sectors = 48
radius = 5
width = 3
scale = radius / 5


# np.random.seed(5)

def get_partition(n, a, b=None):
    if b is None:
        b = a
        a = 0
    sample = np.random.rand(n)
    return a + (b - a) * np.cumsum(sample / sample.sum())


def generate_map(sectors, radius, width, scale):
    """
    :param sectors: number of sectors in the map
    :param radius: average distance between 0 and inner point of map
    :param width: distance between inner and outer points of map
    :param scale: scale of radius variation, as in np.random.normal(loc=radius, scale=scale, size=sectors)
    :return: list of tuples (`inner_point`, `outer_point`) of length :param sectors:
    """

    sector_angles = get_partition(sectors, -pi, pi)
    sector_radii = [radius] * sectors
    sector_radii = np.array(sector_radii) #np.random.normal(loc=radius, scale=scale, size=sectors)
    #sector_radii[sector_radii <= 0] = 1e-6
    inner_points = [rect(r, phi) for phi, r in zip(sector_angles, sector_radii)]
    outer_points = [rect(r, phi) for phi, r in zip(sector_angles, sector_radii + width)]
    return list(zip(inner_points, outer_points))


def generate_obstacles(num, radii, angles, step):
    obstacles = []
    for i in range(num):
        angle = angles[i] - step/100
        radius = radii[i]
        #radius = np.random.normal(loc=radius, scale=0.1, size=1)
        #obstacle_angles = get_partition(6, -pi, pi)
        obstacle_angles = [-pi+pi/4*i for i in range(8)]
        #obstacle_radii = np.random.normal(loc=radius/15, scale=0.01, size=8)
        obstacle_radii = [radius/15] * 8
        #radius = np.random.normal(loc=radius, scale=0.01, size=1)
        obstacle_center = rect(radius, angle)
        obstacle_points = [obstacle_center + rect(r, phi) for phi, r in zip(obstacle_angles, obstacle_radii)]
        obstacles.append(obstacle_points)
    return obstacles


def plot_map(m, o, screen, scale=None, color=(0, 0, 0), width=2):
    if not scale:
        xmax, ymax = np.array([(abs(outer.real), abs(outer.imag)) for inner, outer in m]).max(axis=0)
        scale = ceil(xmax) + ceil(ymax) * 1j
    size = screen.get_width(), screen.get_height()
    from cars.utils import to_px
    points = np.array([[to_px(inner, scale, size), to_px(outer, scale, size)] for inner, outer in m])
    import pygame
    pygame.draw.polygon(screen, color, points[:, 0], width)
    pygame.draw.polygon(screen, color, points[:, 1], width)
    for obstacle in o:
        points = np.array([[to_px(point, scale, size)] for point in obstacle])
        pygame.draw.polygon(screen, color, points[:, 0], width)
    return scale

#
# def plot_obstacles(m, o, screen, scale=None, color=(0, 0, 0), width=2):
#     if not scale:
#         xmax, ymax = np.array([(abs(outer.real), abs(outer.imag)) for inner, outer in m]).max(axis=0)
#         scale = ceil(xmax) + ceil(ymax) * 1j
#     size = screen.get_width(), screen.get_height()
#     from cars.utils import to_px
#     import pygame
#     for obstacle in o:
#         points = np.array([[to_px(point, scale, size)] for point in obstacle])
#         pygame.draw.polygon(screen, color, points[:, 0], width)
#     return scale
