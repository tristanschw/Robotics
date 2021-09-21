
""" 
Code originally from:
HW 1, Problem 6
Course: EECS C106A, Fall 2019
Written by: Valmik Prabhu 8/27/19

Modified for Fall 2021 by Jay Monga
"""

import hw1
import numpy as np
import scipy as sp
import scipy.io as sio
import matplotlib.pyplot as plt

def main():
    # Import the car path
    parking_path = sio.loadmat('parking_path.mat')
    x = parking_path['x'][0]
    y = parking_path['y'][0]
    theta = parking_path['theta'][0]

    # Car dimensions
    length = 2.54;
    bumper = 0.725;
    width = 0.865;

    corner1 = np.array([[length + bumper], [-width]]) # front right
    corner2 = np.array([[length + bumper], [width]]) # front left
    corner3 = np.array([[-bumper], [width]]) # rear left
    corner4 = np.array([[-bumper], [-width]]) # rear right

    plt.figure()
    plt.plot(x, y)

    step = 50 # Adjust step for plotting more/less rectangles on the path
    for index in np.arange(0, len(x), step):
        xy_cur = np.array([[x[index]], [y[index]]])
        theta_cur = theta[index]
        c1, c2, c3, c4 = hw1.get_corners(xy_cur, theta_cur, corner1, corner2, corner3, corner4)
        plt.plot([c1[0], c2[0]], [c1[1], c2[1]], color = 'b')
        plt.plot([c2[0], c3[0]], [c2[1], c3[1]], color = 'b')
        plt.plot([c3[0], c4[0]], [c3[1], c4[1]], color = 'b')
        plt.plot([c4[0], c1[0]], [c4[1], c1[1]], color = 'b')
        plt.plot(xy_cur[0], xy_cur[1], marker = 'o', color = 'b')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == '__main__':
    main()








