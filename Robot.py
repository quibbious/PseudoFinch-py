import sys

class Errors:
    """Contains many errors relating to the FakeFinch Robots"""
    
    @staticmethod
    def printError(message):
        print("\033[91m" + f"{message}" + "\033[0m")  # ANSI escape code for red text
        sys.exit()

    @staticmethod
    def RGBValueError():
        Errors.printError("ValueError: invalid RGB range, must be between 0-255")

    @staticmethod
    def checkIfInvalidRGBValue(R, G, B):
        
        if not R in range(0,256):
            Errors.RGBValueError()
        if not G in range(0,256):
            Errors.RGBValueError()
        if not B in range(0,256):
            Errors.RGBValueError()

    @staticmethod
    def directionError():
        Errors.printError("Invalid direction; must be 'F' or 'B'.")
        
    
    @staticmethod
    def MissingRobotError():
        Errors.printError("No robot detected; please specify a robot.")
    
    @staticmethod
    def SpeedValueError():
        Errors.printError("ValueError: Speed must be between 1-100")

class Robot:
    """Constructor that creates an object corresponding to a Robot"""
    i = 1
    def __init__(robot, name):
        robot.name = name 
    
    """Sets a tri-color LED in the Robot beak to a given color by setting the intensities of the red, green, and blue elements inside it.
    The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off."""
    @staticmethod
    def BeakLight(R, G, B):
        
        Errors.checkIfInvalidRGBValue(R,G,B)
        
        BeakLight = [R,G,B]
        
        return BeakLight
    @staticmethod
    def setMove(direction=str, distance=int, speed=int):
        
        """Moves the robot forward 'F', or backwards 'B', followed by a distance in cm and a speed from 1-100"""
        
        if direction != 'F' and direction != 'B':
            
            Errors.printError(f"SyntaxError: invalid movement direction {direction}")
            
        if speed < 0 or speed > 100:
            
            Errors.SpeedValueError()
        
        if distance < 1: 
            
            Errors.printError("ValueError: distance cannot be below one (1)")
            
        #info for pygame to use 
        
        return direction, distance, speed
    @staticmethod
    def setTurn(direction=str, angle=int, speed=int):
        """Turns the Finch right or left for a specified angle at a specified speed.
        The method requires a direction (‘R’ for right or ‘L’ for left), an angle in degrees, and a speed from 0-100."""
        if direction != 'R' and 'L': 
            
            Errors.printError(f"SyntaxError: invalid direction '{direction}'")
            
        if speed < 0 or speed > 100:
            
            Errors.SpeedValueError()
            
        if not angle in range(1,361): # 360 degree limit per command 
            
            Errors.printError("ValueError: Angle out of range; must be 1-360")
            
        return direction, angle, speed
    @staticmethod
    def setMotors(L=int,R=int):
        
        if not L in range(0,255): 
            Errors.printError("Speed must be between -100 and 100")
    @staticmethod    
    def getVals(robot):
        """returns name of specified robot"""
        id = 1  
        return robot

# example usage

robot = Robot("Finch") # define robot

robot.setMove('F',100,50) # move the robot forward 100 cm, at 50% speed

getvals = Robot.getVals(robot.name) # get the robot's name and put it in a getvals variable

beaklight = robot.BeakLight(100,255,100) # change the beakLight color to blue=100, red=255, green=100, and put it into "beaklight"

robot.setTurn('R', 360, 100)

print(beaklight) # print the beaklight color
