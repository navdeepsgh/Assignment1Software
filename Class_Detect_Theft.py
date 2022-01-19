from geopy.distance import geodesic


class DetectTheft:
    def __init__(self):
        self.movement_detected = False
        self.orientation_changed = False
        self.theft_alert = False
        self.distance = float

    def check_for_movement(self):
        # assuming that movement is detected by accelerometer, this variable is set True to make prototype of Task3 of
        # user story
        self.movement_detected = True
        return self.movement_detected

    def check_for_orientation_change(self):
        # this comes under task 2, assumed that variable is set to False to make prototype
        self.orientation_changed = False
        return self.orientation_changed

    # function will calculate distance between to location and return distance value
    def calculate_distance(self, reference_coordinates, current_coordinates):
        # to make sure input is in form of acceptable datatype
        if (type(reference_coordinates) not in [tuple, list]) or (type(current_coordinates) not in [tuple, list]):
            raise ValueError('Coordinates should be in form of tuple or list, in order (latitude, longitude) or '
                             '[latitude, longitude]')
        # checking only latitude and longitude values are passed in coordinates
        if len(reference_coordinates) > 2 or len(current_coordinates) > 2:
            raise ValueError('Location Coordinates should have only Latitude and Longitude values. '
                             'Calculating distance for different altitude coordinates is beyond scope of this function')

        reference_latitude, reference_longitude = reference_coordinates
        current_latitude, current_longitude = current_coordinates
        # verifying that latitude and longitude values are within range
        if (reference_latitude>90.0 or reference_latitude<-90.0) or (current_latitude>90.0 or current_latitude<-90.0):
            raise ValueError('Latitude value should be within -90.0 to 90.0')
        elif (reference_longitude>180.0 or reference_longitude<-180.0) or (current_longitude>180.0 or current_longitude<-180.0):
            raise ValueError('Longitude value should be between -180.0 to 180.0')
        else:
            # geodesic will return the distance between two geolocations
            self.distance = geodesic(reference_coordinates, current_coordinates).m
            return self.distance

    def set_theft_alert(self):
        # if distance exceeds the limit, theft_alert will be set to True
        if self.distance > 11.0:
            self.theft_alert = True
        else:
            self.theft_alert = False

        return self.theft_alert

    def theft_alert_status(self):
        # return the value of theft_alert
        return self.theft_alert

