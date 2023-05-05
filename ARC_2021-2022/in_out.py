import os
import sys

def readWaypointFile(filename):

    waypoints = []

    with open(filename, 'r') as file:
        for line in file:
            # Split the line into components
            components = line.strip().split()

            print("components", components)

            # Extract latitude and longitude
            latitude = float(components[0]) * (1 if components[1].upper() == 'N' else -1)
            longitude = float(components[2]) * (1 if components[3].upper() == 'E' else -1)

            # Add the coordinates as a tuple to the waypoints list
            waypoints.append((latitude, longitude))

    return waypoints


