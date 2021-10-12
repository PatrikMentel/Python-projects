class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    counter = 1
    def __init__(self, motor_speed = 0, sensor_range = 10, direction = 180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        self.id = DriveBot.counter
        DriveBot.counter += 1
    
    def control_bot(self, new_speed, new_direction):
        self. motor_speed = new_speed
        self.direction = new_direction
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.sensor_range)
print(robot_1.direction)

robot_2 = DriveBot(35, 25, 75)

print(robot_2.motor_speed)
print(robot_2.sensor_range)
print(robot_2.direction)

robot_3 = DriveBot()
DriveBot.all_disabled = True
DriveBot.latitude = -50.0
DriveBot.longitude = 50.0

print(robot_1.all_disabled)
print(robot_2.latitude)
print(robot_3.longitude)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)