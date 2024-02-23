import sys

class Errors():
    """Contains many errors relating to the FakeFinch Robots"""
    def __init(self, message):
        self.message = message
        
    def print_error(message):
        print("\033[91m" + f"{message}" + "\033[0m")  # ANSI escape code for red text
        sys.exit()

    def RGBValueError():
        Errors.print_error("ValueError: invalid RGB range, must be between 1-255")

    def checkIfInvalidRGBValue(R, G, B):

        if R < 0 or R > 255:
            Errors.RGBValueError()
        if G < 0 or G > 255: 
            Errors.RGBValueError()
        if B < 0 or B > 255:
            Errors.RGBValueError()

    def directionError():
        Errors.print_error("Invalid direction; must be 'F' or 'B'.")
        
    
    def MissingRobotError():
        Errors.print_error("No robot detected; please specify a robot.")
    
    def SpeedValueError():
        Errors.print_error("ValueError: Speed must be between 1-100")
    
class Robot(Errors):
    """Constructor that creates an object corresponding to a Robot"""
    
    def __init__(robot, name):
        robot.name = name 

        
    def getVals(robot): 
        return robot.name

class RobotLights(Robot):
    """Sets a tri-color LED in the Finch beak to a given color by setting the intensities of the red, green, and blue elements inside it.
    The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off."""
    def __init__(robot, name):
        super().__init__(name)
    
    def BeakLight(R, G,B):
        Errors.checkIfInvalidRGBValue(R,G,B)
        
        BeakLight = [R,G,B]
        return BeakLight

class RobotController(Robot, Errors):
    def __init__(self, robot, direction, distance, speed):
        self.robot = robot
        self.direction = direction
        self.distance = distance
        self.speed = speed
        
    def setMove(direction=str, distance=int, speed=int):
        """Moves the robot forward 'F', or backwards 'B', followed by a distance in cm and a speed from 1-100"""
        
        if direction != 'F' and 'B':
            Errors.print_error(f"SyntaxError: invalid movement direction {direction}")
            
        if speed < 0 or speed > 100:
            Errors.SpeedValueError()
        
        if distance < 1: 
            Errors.print_error("ValueError: distance cannot be below one (1)")
        
        return direction, distance, speed, 
    
    
    
robot = Robot("Finch")

RobotLights.BeakLight(0,0,0)

print(robot.name)

movement = RobotController.setMove('F', 1 , 200)

print(movement)

