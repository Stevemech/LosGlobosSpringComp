import math

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371
    distance = R * c

    return distance

def determinePath(waypoints):
    remaining_waypoints = waypoints.copy()
    current_point = remaining_waypoints.pop(0)
    route = [current_point]

    while remaining_waypoints:
        next_point = min(remaining_waypoints, key=lambda point: haversine_distance(current_point[0], current_point[1], point[0], point[1]))
        remaining_waypoints.remove(next_point)
        route.append(next_point)
        current_point = next_point

    return route






