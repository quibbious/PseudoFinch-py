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
    
    @staticmethod
    def BeakLight(R, G, B):
        """Sets a tri-color LED in the Robot beak to a given color by setting the intensities of the red, green, and blue elements inside it.
    The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off.
        Example: Robot.setBeak(0,100,0)"""
        Errors.checkIfInvalidRGBValue(R,G,B)
        
        BeakLight = [R,G,B]
        
        return BeakLight
    @staticmethod
    def setMove(direction=str, distance=int, speed=int):
        
        """Moves the robot forward 'F', or backwards 'B', followed by a distance in cm and a speed from 1-100.
        Example: Robot.setMove(‘F’,10,50)"""
        
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
        """Turns the Robot right or left for a specified angle at a specified speed.
        The method requires a direction (‘R’ for right or ‘L’ for left), an angle in degrees, and a speed from 0-100.
        Example: Robot.setTurn(‘R’,90,50)"""
        if direction != 'R' and direction != 'L': 
            
            Errors.printError(f"SyntaxError: invalid direction '{direction}'")
            
        if speed < 0 or speed > 100:
            
            Errors.SpeedValueError()
            
        if not angle in range(1,361): # 360 degree limit per command 
            
            Errors.printError("ValueError: Angle out of range; must be 1-360")

        if direction == 'L':
            invertedangle = -1  * angle
            return direction, invertedangle, speed
        
        return direction, angle, speed
    @staticmethod
    def setMotors(L=int,R=int):
        """Sets the Robot wheels to spin at the given speeds. The method requires two speeds between -100 and 100 for the left and right wheels.
        Setting the speed to 0 turns the motor off.
        Example: Robot.setMotors(-50,50)
        """
           
        if not L in range(-101,101): 
            Errors.printError("Speed must be between -100 and 100")
        if not R in range(-101,101):
            Errors.printError("Speed must be between -100 and 100")
        Motors = [L,R]
        return Motors
    @staticmethod
    def stop():
        Robot.setMotors(0,0)
    
    @staticmethod
    
    def setTail(port, r, g, b):
        """Sets a tri-color LED in the Robot tail to a given color by setting the intensities of the red, green, and blue elements inside it.
        The method requires the port number of the LED (1, 2, 3, 4, or “all”) and three intensity values from 0-100. 
        Setting all three intensity values to 0 turns the LED off.
        Example: Robot.setTail(“all”,0,100,0)"""
    
        if not (port == 1 or 2 or 3 or 4 or 'all'):
            Errors.printError("SyntaxError: invalid selection")

        Errors.checkIfInvalidRGBValue(r,g,b)

        tailvaluesRGB = [port,r,g,b]
        
        return tailvaluesRGB
    
    @staticmethod
    def playNote(note,beats):
        """Plays a note using the buzzer on the Robot.
        The method requires an integer representing the note (32-135) and a number giving the number of beats (0-16). 
        The number of beats can be a decimal number. One beat corresponds to one second.
        Example: Robot.playNote(60,0.5)"""
        
        if not note in range(31,136):
            Errors.printError("ValueError: note is not in range")
        
        if beats < 1 or beats > 16:
            Errors.printError("ValueError: beat is not in range")

        options = [note,beats]

        return options
        
        
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

turn1 = robot.setTurn('R', 360, 100) # turn R

print(turn1)
print(beaklight)

robot.setMotors(50,50) # set motors L and R to 50% 

tailLights = robot.setTail(1,100,200,100) # set port 1 to r=100, g=200, b=100

print(tailLights)

music = robot.playNote(132, 16) # play note 132 at beat 16

print(music)
