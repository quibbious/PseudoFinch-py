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
        if not (0 <= R <= 255) or not (0 <= G <= 255) or not (0 <= B <= 255):
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
    
    def __init__(self, name=None):
        self.name = name
    
    def setBeak(self, R: int = 0, G: int = 0, B: int = 0):
        """Sets a tri-color LED in the Robot beak to a given color by setting the intensities of the red, green, and blue elements inside it.
        The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off.
        Example: Robot.setBeak(0,100,0)"""
        Errors.checkIfInvalidRGBValue(R, G, B)
        return (R, G, B)
    
    def setMove(self, direction: str, distance: int, speed: int):
        """Moves the robot forward 'F', or backwards 'B', followed by a distance in cm and a speed from 1-100.
        Example: Robot.setMove(‘F’,10,50)"""
        if direction not in ('F', 'B'):
            Errors.directionError()
        if not speed in range(0,101):
            Errors.SpeedValueError()
        if distance < 1: 
            Errors.printError("ValueError: distance cannot be below one (1)")
        return direction, distance, speed
    
    def setTurn(self, direction=str, angle=int, speed=int):
        """Turns the Robot right or left for a specified angle at a specified speed.
        The method requires a direction (‘R’ for right or ‘L’ for left), an angle in degrees, and a speed from 0-100.
        Example: Robot.setTurn(‘R’,90,50)"""
        if direction not in ('R', 'L'): 
            Errors.printError(f"SyntaxError: invalid direction '{direction}'")
        if not speed in range(0,101):
            Errors.SpeedValueError()
        if not speed in range(0,101):  # 360 degree limit per command 
            Errors.printError("ValueError: Angle out of range; must be 1-360")
        if direction == 'L':
            invertedangle = -1 * angle
            return direction, invertedangle, speed
        return direction, angle, speed
    
    def setMotors(self, L=int, R=int):
        """Sets the Robot wheels to spin at the given speeds. The method requires two speeds between -100 and 100 for the left and right wheels.
        Setting the speed to 0 turns the motor off.
        Example: Robot.setMotors(-50,50)"""
        if not L in range(-100,101):
            Errors.printError("Speed must be between -100 and 100")
        if not R in range(-100,101):
            Errors.printError("Speed must be between -100 and 100")
        return [L, R]
    
    def stop(self):
        self.setMotors(0, 0)
    
    def setTail(self, port, r, g, b):
        """Sets a tri-color LED in the Robot tail to a given color by setting the intensities of the red, green, and blue elements inside it.
        The method requires the port number of the LED (1, 2, 3, 4, or “all”) and three intensity values from 0-100. 
        Setting all three intensity values to 0 turns the LED off.
        Example: Robot.setTail(“all”,0,100,0)"""
        if port not in (1, 2, 3, 4, 'all'):
            Errors.printError("SyntaxError: invalid selection")
        Errors.checkIfInvalidRGBValue(r, g, b)
        return (port, r, g, b)
    
    def playNote(self, note, beats):
        """Plays a note using the buzzer on the Robot.
        The method requires an integer representing the note (32-135) and a number giving the number of beats (0-16). 
        The number of beats can be a decimal number. One beat corresponds to one second.
        Example: Robot.playNote(60,0.5)"""
        if not (31 < note < 136):
            Errors.printError("ValueError: note is not in range")
        if not (0 < beats <= 16):
            Errors.printError("ValueError: beat is not in range")
        return (note, beats)
    
    def setDisplay(self, LEDlist):
        """Sets the LED array of the micro:bit to display a pattern defined by a list of length 25. 
        Each value in the list must be 0 (off) or 1 (on). 
        The first five values in the array correspond to the five LEDs in the first row, the next five values to the second row, etc.
        Example: robot.setDisplay([1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1])"""
        if len(LEDlist) != 25:
            Errors.printError("LEDlist must have a length of 25")
        for value in LEDlist:
            if value not in (0, 1):
                Errors.printError("Each value in LEDlist must be 0 (off) or 1 (on)")
        return LEDlist
    
    def setPoint(self, LEDlist, row, column, value):
        """Turn on or off a single LED on the micro:bit display. The position of the LED is given by the row and column parameters, which should both be between 1 and 5.
        The value of the LED must be 0 (off) or 1 (on).
        Example:  robot.setPoint(3,3,1)"""
        if not (1 <= row <= 5) or not (1 <= column <= 5):
            Errors.printError("Row and column values must be between 1 and 5")
        index = (row - 1) * 5 + (column - 1)
        if value not in (0, 1):
            Errors.printError("Value must be 0 (off) or 1 (on)")
        LEDlist[index] = value
        return LEDlist
    
    def digiPrint(self, message: str):
        """Print a string on the micro:bit LED array.
        The string must contain only English letters. strings will default to uppercase if lowercase.
        Example: robot.digiPrint("Hello World")
        input string = 'Hello World'
        interpreted string = 'HELLO WORLD'
        """
        message = message.upper()
        alphabet = {
            'A': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 0 ', ' 1 0 0 1 0 '],
            'B': [' 1 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 1 1 0 0 '],
            'C': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 0 0 0 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            'D': [' 1 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 0 0 '],
            'E': [' 1 1 1 1 0 ', ' 1 0 0 0 0 ', ' 1 1 1 0 0 ', ' 1 0 0 0 0 ', ' 1 1 1 1 0 '],
            'F': [' 1 1 1 1 0 ', ' 1 0 0 0 0 ', ' 1 1 1 0 0 ', ' 1 0 0 0 0 ', ' 1 0 0 0 0 '],
            'G': [' 0 1 1 0 0 ', ' 1 0 0 0 0 ', ' 1 0 1 1 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            'H': [' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 '],
            'I': [' 1 1 1 0 0 ', ' 0 1 0 0 0 ', ' 0 1 0 0 0 ', ' 0 1 0 0 0 ', ' 1 1 1 0 0 '],
            'J': [' 0 0 1 1 0 ', ' 0 0 0 1 0 ', ' 0 0 0 1 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            'K': [' 1 0 0 1 0 ', ' 1 0 1 0 0 ', ' 1 1 0 0 0 ', ' 1 0 1 0 0 ', ' 1 0 0 1 0 '],
            'L': [' 1 0 0 0 0 ', ' 1 0 0 0 0 ', ' 1 0 0 0 0 ', ' 1 0 0 0 0 ', ' 1 1 1 1 0 '],
            'M': [' 1 0 0 0 1 ', ' 1 1 0 1 1 ', ' 1 0 1 0 1 ', ' 1 0 0 0 1 ', ' 1 0 0 0 1 '],
            'N': [' 1 0 0 0 1 ', ' 1 1 0 0 1 ', ' 1 0 1 0 1 ', ' 1 0 0 1 1 ', ' 1 0 0 0 1 '],
            'O': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            'P': [' 1 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 1 1 0 0 ', ' 1 0 0 0 0 ', ' 1 0 0 0 0 '],
            'Q': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 0 1 0 0 ', ' 0 1 0 1 1 '],
            'R': [' 1 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 1 1 0 0 ', ' 1 0 1 0 0 ', ' 1 0 0 1 0 '],
            'S': [' 0 1 1 1 0 ', ' 1 0 0 0 0 ', ' 0 1 1 0 0 ', ' 0 0 0 1 0 ', ' 1 1 1 0 0 '],
            'T': [' 1 1 1 1 1 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 '],
            'U': [' 1 0 0 0 1 ', ' 1 0 0 0 1 ', ' 1 0 0 0 1 ', ' 1 0 0 0 1 ', ' 0 1 1 1 0 '],
            'V': [' 1 0 0 0 1 ', ' 1 0 0 0 1 ', ' 1 0 0 0 1 ', ' 0 1 0 1 0 ', ' 0 0 1 0 0 '],
            'W': [' 1 0 0 0 1 ', ' 1 0 0 0 1 ', ' 1 0 1 0 1 ', ' 1 1 0 1 1 ', ' 1 0 0 0 1 '],
            'X': [' 1 0 0 0 1 ', ' 0 1 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 1 0 ', ' 1 0 0 0 1 '],
            'Y': [' 1 0 0 0 1 ', ' 0 1 0 1 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 '],
            'Z': [' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 1 1 1 1 0 '],
            ' ': [' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 '],
            '1': [' 0 1 1 0 0 ', ' 1 1 1 0 0 ', ' 0 1 1 0 0 ', ' 0 1 1 0 0 ', ' 1 1 1 1 0 '],
            '2': [' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 1 1 0 0 ', ' 1 0 0 0 0 ', ' 1 1 1 1 0 '],
            '3': [' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 1 1 0 0 ', ' 0 0 0 1 0 ', ' 1 1 1 1 0 '],
            '4': [' 0 0 1 0 0 ', ' 0 1 1 0 0 ', ' 1 0 1 0 0 ', ' 1 1 1 1 0 ', ' 0 0 1 0 0 '],
            '5': [' 1 1 1 1 0 ', ' 1 0 0 0 0 ', ' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 1 1 1 1 0 '],
            '6': [' 1 1 1 1 0 ', ' 1 0 0 0 0 ', ' 1 1 1 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 0 '],
            '7': [' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 1 0 0 0 0 '],
            '8': [' 1 1 1 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 0 '],
            '9': [' 1 1 1 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 '],
            '0': [' 0 1 1 1 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 0 1 1 1 0 '],
            '.': [' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 1 1 0 0 '],
            ',': [' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 1 0 0 0 '],
            '!': [' 0 1 1 0 0 ', ' 0 1 1 0 0 ', ' 0 1 1 0 0 ', ' 0 0 0 0 0 ', ' 0 1 1 0 0 '],
            '?': [' 1 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 0 0 0 0 ', ' 0 0 1 0 0 '],
            "'": [' 0 1 0 0 0 ', ' 0 1 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 '],
            '(': [' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 0 1 0 0 0 ', ' 0 1 0 0 0 ', ' 0 0 1 0 0 '],
            ')': [' 0 1 0 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 '],
            '/': [' 0 0 0 1 0 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 1 0 0 0 0 '],
            '\\': [' 1 0 0 0 0 ', ' 0 1 0 0 0 ', ' 0 0 1 0 0 ', ' 0 0 0 1 0 ', ' 0 0 0 0 1 '],
            '-': [' 0 0 0 0 0 ', ' 0 0 0 0 0 ', ' 1 1 1 1 0 ', ' 0 0 0 0 0 ', ' 0 0 0 0 0 '],
            '+': [' 0 0 0 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 1 1 1 1 0 ', ' 0 0 1 0 0 '],
            '*': [' 0 0 0 0 0 ', ' 0 1 0 1 0 ', ' 0 0 1 0 0 ', ' 1 0 0 0 1 ', ' 0 0 0 0 0 '],
            '#': [' 0 1 0 1 0 ', ' 1 1 1 1 1 ', ' 0 1 0 1 0 ', ' 1 1 1 1 1 ', ' 0 1 0 1 0 '],
            '@': [' 0 1 1 1 0 ', ' 1 0 0 0 1 ', ' 1 0 1 1 1 ', ' 1 0 1 0 1 ', ' 0 1 1 1 0 ']
        }
        for line in range(5):
            for character in message:
                print(alphabet[character][line], end=' ')
            print()
