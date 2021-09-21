import numpy as np

def get_corners(xy, theta, corner1, corner2, corner3, corner4):
    """
    Get the corners of the car given the 2D pose of the car.
    TODO: Make sure that this function returns the correct position of each corner of the car relative to the world frame.

    Parameters:
        xy (2x1 np array): The xy position of the car
        theta (float): The angle the car. theta=0 corresponds to the car pointing along the x-axis
        corner1, corner2, corner3, corner4 (2x1 np array): Position of each corner of the car relative to the car's frame
    Returns:
        c1, c2, c3, c4: Position of each corner of the car relative to the world frame
    """
    
    co, si = np.cos(theta), np.sin(theta)
    rotmat = np.array(((co, -si), (si, co)))
    # Are these coordinates in the right frame?
    c1 = np.dot(rotmat, corner1) + xy
    c2 = np.dot(rotmat, corner2) + xy
    c3 = np.dot(rotmat, corner3) + xy
    c4 = np.dot(rotmat, corner4) + xy

    return c1, c2, c3, c4