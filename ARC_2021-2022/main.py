import math
from algo import *
from in_out import *

def main(filename):
    # Example usage
    waypoints = readWaypointFile(filename)
    print(waypoints)

    # Determine path
    bestPath = determinePath(waypoints)

    print("Best Path:", bestPath)

if __name__ == '__main__':
	main("waypoint_1.txt")