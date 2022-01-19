from Reference_Location import reference_location
from GPS_Emulator import current_location
import time
from Class_Detect_Theft import DetectTheft

# object of Detect Theft class
bicycle = DetectTheft()


if bicycle.check_for_movement() or bicycle.check_for_orientation_change():

    # movement detected variable is set to True to implement functionality of calculate distance function

    # checking the distance for two minutes
    for i in range(40):
        # displaying distance to check that loop will actually break when distance > 11.0
        print('Distance (in metres): ', bicycle.calculate_distance(reference_location(), current_location()))
        # if distance > 11.0, it will set theft alert and break two minutes loop
        if bicycle.set_theft_alert():
            break
        else:
            # if distance < 11.0 it will continue loop for two minutes
            time.sleep(3.0)
            continue

# if theft alert is True then it will give theft alert
if bicycle.theft_alert_status():
    print("THEFT ALERT!!!")
else:
    # if theft alert is False it will again set these variables to false
    print('No Theft')
    bicycle.movement_detected = False
    bicycle.orientation_changed = False

# To continue the whole process until the user turns off theft detection control we can write the above code in while
# loop;  while theft_detection_control and not bicycle.theft_alert:
# By writing this while statement at line 9, code will run until user turns off theft detection control or until
# theft is detected. It will implement Task 4 of corresponding User Story
