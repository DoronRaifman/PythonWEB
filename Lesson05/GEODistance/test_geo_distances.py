import unittest
import numpy as np
from Lesson05.GEODistance.geo_distances import GeoDistances


class GeoDistancesForTest(GeoDistances):
    def _generate_data(self, samples_num=100):
        points_geo_lat = np.full(samples_num, self.base_lat)
        points_geo_long = np.full(samples_num, self.base_long)
        noise_base = np.linspace(-1.0, 1.0, 50) / 1000.0
        noise = np.resize(noise_base, samples_num)
        points = np.zeros((samples_num, 4))
        points[:, 0] = points_geo_lat + noise
        points[:, 1] = points_geo_long + noise
        points[:, 2] = np.arange(0, samples_num)                # point id
        points[:, 3] = np.random.randint(0, 3, samples_num)     # source
        self.points_numpy = points


class TestGEODistance(unittest.TestCase):
    geo_distances = GeoDistancesForTest()
    samples_num = 100000
    geo_distances._generate_data(samples_num)
    geo_distances.pre_calculate()

    def test_demonstrate_get_points_in_range(self):
        self.geo_distances._demonstrate_get_points_in_range()

    def test_demonstrate_get_estimated_geo_distance(self):
        self.geo_distances._demonstrate_get_estimated_geo_distance()

    def test_get_points_in_range(self):
        point = [self.geo_distances.base_lat, self.geo_distances.base_long]
        points1 = self.geo_distances.points_numpy[:10, :2]
        points2 = self.geo_distances.points_numpy[10:20, :2]

        res1 = np.round(self.geo_distances.get_estimated_geo_distance_vectors(points1, point), 1)
        exp_res1 = np.array([145.8, 139.8, 133.9, 127.9, 122., 116., 110.1, 104.1, 98.2, 92.2])
        delta = np.abs(exp_res1 - res1)
        self.assertGreater(0.1, np.max(delta))

        res2 = np.round(self.geo_distances.get_estimated_geo_distance_vectors(points1, points2), 1)
        exp_res2 = np.array([59.5, 59.5, 59.5, 59.5, 59.5, 59.5, 59.5, 59.5, 59.5, 59.5])
        delta = np.abs(exp_res2 - res2)
        self.assertGreater(0.1, np.max(delta))


if __name__ == '__main__':
    unittest.main()
