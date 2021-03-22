from enum import Enum
import math
import time
import numpy as np


class OriginType(Enum):
    PipeSections = 0
    Sensor = 1
    Invented = 2
    InventedGround = 3


class GeoDistances:
    def __init__(self):
        self.delta_lat_to_m = 0.0
        self.delta_long_to_m = 0.0
        self.points_numpy: np.ndarray = np.zeros(10)
        self.base_lat, self.base_long = 32.0, 34.0

    @staticmethod
    def get_geo_distance_two_points_tuple(point1, point2):
        res = GeoDistances.get_geo_distance_two_points(
            point1[0], point1[1], point2[0], point2[1])
        return res

    @staticmethod
    def get_geo_distance_two_points(lat1, long1, lat2, long2):
        earth_radius = 6371000  # [m]
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        long1_rad = math.radians(long1)
        long2_rad = math.radians(long2)
        delta_long_rad = (long2_rad - long1_rad)
        delta_lat_rad = (lat2_rad - lat1_rad)
        a = math.sin(delta_lat_rad / 2) * math.sin(delta_lat_rad / 2) + \
            math.cos(lat1_rad) * math.cos(lat2_rad) * \
            math.sin(delta_long_rad / 2) * math.sin(delta_long_rad / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return earth_radius * c

    def pre_calculate(self):
        max_lat_long = np.amax(self.points_numpy, axis=0)
        max_lat, max_long = float(max_lat_long[0]), float(max_lat_long[1])
        min_lat_long = np.amin(self.points_numpy, axis=0)
        min_lat, min_long = float(min_lat_long[0]), float(min_lat_long[1])
        center_lat, center_long = \
            (max_lat + min_lat) / 2.0, (max_long + min_long) / 2.0
        self.delta_lat_to_m = self.get_geo_distance_two_points_tuple(
            (center_lat-0.5, center_long), (center_lat+0.5, center_long))
        self.delta_long_to_m = self.get_geo_distance_two_points_tuple(
            (center_lat, center_long-0.5), (center_lat, center_long+0.5))

    def generate_data(self, samples_num):
        points_geo_lat = np.full(samples_num, self.base_lat)
        points_geo_long = np.full(samples_num, self.base_long)
        noise_lat = (np.random.rand(samples_num) - 0.5) / 10000.0
        noise_long = (np.random.rand(samples_num) - 0.5) / 10000.0
        points = np.zeros((samples_num, 4))
        points[:, 0] = points_geo_lat + noise_lat
        points[:, 1] = points_geo_long + noise_long
        points[:, 2] = np.arange(0, samples_num)                # point id
        points[:, 3] = np.random.randint(0, 3, samples_num)     # source
        self.points_numpy = points

    def find_estimated_geo_distance_vectors(self, point_vect1: list, point_vect2: list):
        delta = np.abs(np.array(point_vect1) - np.array(point_vect2))
        delta_m = np.sqrt(np.power(delta[:, 0] * self.delta_lat_to_m, 2.0) +
                          np.power(delta[:, 1] * self.delta_long_to_m, 2.0))
        return delta_m

    def get_points_in_range(self, point:tuple, distance_m:float, origin_type: OriginType = None):
        if origin_type is None:
            points = self.points_numpy
        else:
            origins = self.points_numpy[:, 3]
            points = self.points_numpy[np.where(origins == origin_type.value)]
        distance = distance_m * 0.7
        delta_lat, delta_long = distance / self.delta_lat_to_m, distance / self.delta_long_to_m
        lat_min, lat_max = point[0]-delta_lat, point[0]+delta_lat
        long_min, long_max = point[1]-delta_long, point[1]+delta_long
        cond1 = (points[:, 0] >= lat_min) & (points[:, 0] <= lat_max)
        cond2 = (points[:, 1] >= long_min) & (points[:, 1] <= long_max)
        condition = cond1 & cond2
        points = points[np.where(condition)]
        if np.shape(points)[0] == 0:
            points_distance_m = np.zeros(0)
        else:
            point_lat_long = point[0:2]
            points_lat_long = points[:, 0:2]
            points_distance = np.abs(points_lat_long - point_lat_long) * \
                              np.array([self.delta_lat_to_m, self.delta_long_to_m])
            points_distance_m = np.sqrt(np.power(points_distance[:, 0], 2.0) +
                                        np.power(points_distance[:, 1], 2.0))
        return points, points_distance_m


if __name__ == '__main__':
    worker = GeoDistances()
    samples_num = 100000
    worker.generate_data(samples_num)
    worker.pre_calculate()
    point = (worker.base_lat, worker.base_long)
    start_time = time.time()
    res1_points, res1_dist = worker.get_points_in_range(point, 5.0)
    step1_time = time.time()
    res2_points, res2_dist = worker.get_points_in_range(point, 5.0, OriginType.PipeSections)
    step2_time = time.time()
    print(f'samples_num:{samples_num}, '
          f'res1: {res1_dist.size} elapsed {(step1_time-start_time)*1000:.1f}[mSec], '
          f'res2: {res2_dist.size} elapsed {(step2_time-step1_time)*1000:.1f}[mSec]')

