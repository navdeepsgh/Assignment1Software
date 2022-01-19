import unittest
from Class_Detect_Theft import DetectTheft


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.test_bicycle = DetectTheft()

    def tearDown(self) -> None:
        pass

    def test_distance(self):
        # for same coordinates distance should be zero
        self.assertEqual(self.test_bicycle.calculate_distance((30.84277846, 75.97808147), (30.84277846, 75.97808147)), 0.0)
        # even for slight difference distance should not be zero
        self.assertNotEqual(self.test_bicycle.calculate_distance((30.84277846, 75.97808147), (30.84277847, 75.97808147)), 0.0)
        # distance value returned by function should not be None
        self.assertIsNotNone(self.test_bicycle.calculate_distance((30.84268538, 75.97806326), (30.84270465, 75.97809515)))

    def test_input_latitude_limit(self):
        # latitude value should be between -90 degrees to +90 degrees
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, (-99.115, 56.2516), (35.615, 74.511))
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, (45.34232, 34.32121), (90.00001, 127.2212))

    def test_input_longitude_limit(self):
        # longitude value should be between -180 degrees to +180 degrees
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, (45.56555, 180.0001), (-52.11651, -74.161))
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, (65.42323, 12.21216), (-47.16516, -180.161))

    def test_input_values_format(self):
        # only latitude and longitude should be there in coordinates, calculating distance for different altitudes is
        # beyond scope of this function
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, (55.323, 18.121), (-47.16516, -18.161, 23.214))
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, (34.4322, -74.4332, 27.323), (-67.516, 112.168, 15.561))

    def test_input_datatype(self):
        # coordinates should be given as input in form of tuple or list, any other datatype like dictionary (in python)
        # is not taken as valid input
        self.assertRaises(ValueError, self.test_bicycle.calculate_distance, {'lat': -35.9996543, 'long': 75.9785236}, {'lat': -35.99999, 'long': 75.97808147})

    def test_set_theft_alert_for_True(self):
        # testing set_theft_alert and theft_alert_status functions for distance > 11.0
        self.test_bicycle.calculate_distance((45.56555, 23.44516), (-52.11651, -74.161))
        self.assertTrue(self.test_bicycle.set_theft_alert())
        self.assertTrue(self.test_bicycle.theft_alert_status())
        self.test_bicycle.calculate_distance((30.84277846, 75.97808147), (30.84277847, 75.97808147))
        self.assertFalse(self.test_bicycle.set_theft_alert())
        self.assertFalse(self.test_bicycle.theft_alert_status())


if __name__ == '__main__':
    unittest.main()
