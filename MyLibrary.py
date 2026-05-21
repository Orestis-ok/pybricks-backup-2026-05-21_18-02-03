######################## Pybricks library ########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


######################## Define variable ########################

pi = 3.1415926535897

WHEEL_SIZE = 62
WHEEL_SPACING = 145

PORT_LEFTDRIVE = "LD"
PORT_RIGHTDRIVE = "RD"
PORT_LEFTATTACH = "LA"
PORT_RIGHTATTACH = "RA"
# PORT_LEFTCOLOUR = "LC"
# PORT_RIGHTCOLOUR = "RC"

STR_SPEED = 400
STR_ACCEL = 400
TURN_SPEED = 300
TURN_ACCEL = 300

BLACK = 5
WHITE = 40
THRESHOLD = (WHITE - BLACK) / 2

######################## Hub & Port setup ########################

# Robot type - Laura 3
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub.system.set_stop_button([Button.BLUETOOTH])

# leftColour = ColorSensor(Port.B)
# rightColour = ColorSensor(Port.F)
leftArm = Motor(port=Port.A, positive_direction=Direction.CLOCKWISE, gears=[12,20])
rightArm = Motor(port=Port.E, positive_direction=Direction.CLOCKWISE, gears=[12,20])
leftDrive = Motor(port=Port.D, positive_direction=Direction.CLOCKWISE)
rightDrive = Motor(port=Port.C, positive_direction=Direction.COUNTERCLOCKWISE)

driveBase = DriveBase(leftDrive, rightDrive, WHEEL_SIZE, WHEEL_SPACING)



######################## My Functions ########################

def Hub_DisplayNum(number):
    hub.display.number(number)

def Hub_SpeakerBeep(frequency, duration):
    hub.speaker.beep(frequency, duration)


def PortView_Battery():
    print("---- Hub battery info ----")
    print("Hub battery voltage: ", hub.battery.voltage(), "mV")
    print("Hub battery current: ", hub.battery.current(), "mA")
    print(" ")


def MoveSteering_Seconds(speed, steering, duration):
    driveBase.drive(speed, steering) # Start driveBase to move unlimitedly
    wait(duration) # Wait for certain duration
    driveBase.brake() # Stop robot after duration ends

def MoveStraight_Distance(speed, accel, distance, useGyro, waitForComplete, stopMethod):
    # Reset gyro and driveBase value
    driveBase.reset()
    driveBase.use_gyro(useGyro)

    # Set the driveBase value
    driveBase.settings(speed, accel, TURN_SPEED, TURN_ACCEL)

    # Action !!!
    driveBase.straight(distance, stopMethod, waitForComplete)

#### Αντώνης ####

def TankDrive_Distance_mm(left_speed, right_speed, distance_mm, stopMethod=Stop.BRAKE):
    # Υπολογισμός περιφέρειας ρόδας
    wheel_circumference = pi * WHEEL_SIZE

    # Μετατροπή από mm σε μοίρες
    degrees = (distance_mm / wheel_circumference) * 360

    # Tank κίνηση σε απόσταση
    leftDrive.run_angle(left_speed, degrees, then=stopMethod, wait=False)
    rightDrive.run_angle(right_speed, degrees, then=stopMethod, wait=True)

#### Αντώνης ####

def TankDrive_Time_ms(left_speed, right_speed, time_ms, stopMethod=Stop.BRAKE):
    leftDrive.run_time(left_speed, time_ms, then=stopMethod, wait=False)
    rightDrive.run_time(right_speed, time_ms, then=stopMethod, wait=True)

#### Αντώνης ####


# ======================== AUTO ALIGN (BOTH ARMS) ========================
# Non-blocking jiggle for attachment gear alignment.
# Call AutoAlign_Start() once when entering READY state.
# Call AutoAlign_Update(...) repeatedly while waiting.
# Call AutoAlign_Stop() just before starting the route.

_auto_dir = 1
_auto_timer = StopWatch()

def AutoAlign_Start():
    # """Initialize jiggle state (call once when you enter waiting/ready mode)."""
    global _auto_dir, _auto_timer
    _auto_dir = 1
    _auto_timer = StopWatch()
    _auto_timer.reset()
    leftArm.brake()
    rightArm.brake()

def AutoAlign_Update(speed_left=30, speed_right=30, switch_ms=120):
    # Jiggle both motors with independent speeds.

    # speed_left:  deg/sec for leftArm
    # speed_right: deg/sec for rightArm
    # switch_ms:   change direction every X milliseconds
    
    global _auto_dir, _auto_timer

    if _auto_timer.time() >= switch_ms:
        _auto_dir *= -1
        _auto_timer.reset()

    leftArm.run(speed_left * _auto_dir)
    rightArm.run(speed_right * _auto_dir)

def AutoAlign_Stop(brake=True):
    # """Stop jiggle."""
    if brake:
        leftArm.brake()
        rightArm.brake()
    else:
        leftArm.stop()
        rightArm.stop()
# =======================================================================



#### Assasins ####

def MoveCurve_Angle(speed, accel, radius, angle, waitForComplete, stopMethod):
    # Reset gyro and driveBase value
    driveBase.reset()
    driveBase.use_gyro(True)

    # Set the driveBase value
    driveBase.settings(speed, accel, TURN_SPEED, TURN_ACCEL)

    # Action !!!
    driveBase.curve(radius, angle, stopMethod, waitForComplete)

def PointTurn_Angle(turnSpeed, turnAccel, angle, waitForComplete, stopMethod):
    # Reset gyro and driveBase value
    hub.imu.reset_heading(0)
    driveBase.reset()
    driveBase.use_gyro(True)

    # Set the driveBase value
    driveBase.settings(STR_SPEED, STR_ACCEL, turnSpeed, turnAccel)

    # Action !!!
    driveBase.turn(angle, stopMethod, waitForComplete)

    # ---- Print final angle ----
    final_angle = hub.imu.heading()
    print("Final turn angle:", final_angle)

def LineDetection_Colour_Steering(sensorPort, speed, steering, colour, stop, ):
    # Determine which port to scan
    if sensorPort == "LC":
        while not left_colour.color() == colour:
            driveBase.drive(speed, steering) # Repeat drive action until sensor detected
            wait(10)
    elif sensorPort == "RC":
        while not right_colour.color() == colour:
            driveBase.drive(speed, steering)
            wait(10)

    driveBase.brake() # Stop robot after detected

def LineFollow_PD_BySeconds(sensorPort, power, duration, Kp, Kd):
    # Reset value before start
    error = lastError = 0
    normalised = 50
    timerLF = StopWatch()
    timerLF.reset()

    # Repeat line follow until time up
    while timerLF.time() < duration:

        # Determine which port to line follow
        if sensorPort == "LC":
            reflected = left_colour.reflection()
        elif sensorPort == "RC":
            reflected = right_colour.reflection()

        # Perform PD calculations
        normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
        error = normalised - 50
        pd = (error * Kp) + ((error - lastError) * Kd)

        # Add value into motor power to control
        left_drive.dc(power + pd)
        right_drive.dc(power - pd)

        lastError = error # Reset lastError
    
   






