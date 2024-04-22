import sys

class Errors:
    """Contains many errors relating to the FakeFinch Robots"""
    
     
    def printError(message):
        print("\033[91m" + f"{message}" + "\033[0m")  # ANSI escape code for red text
        sys.exit()

     
    def RGBValueError():
        Errors.printError("ValueError: invalid RGB range, must be between 0-255")

     
    def checkIfInvalidRGBValue(R, G, B):
        
        if not R in range(0,256):
            Errors.RGBValueError()
        if not G in range(0,256):
            Errors.RGBValueError()
        if not B in range(0,256):
            Errors.RGBValueError()

     
    def directionError():
        Errors.printError("Invalid direction; must be 'F' or 'B'.")
        
    
     
    def MissingRobotError():
        Errors.printError("No robot detected; please specify a robot.")
    
     
    def SpeedValueError():
        Errors.printError("ValueError: Speed must be between 1-100")

class Robot:
    
    
    
    """Constructor that creates an object corresponding to a Robot"""
    i = 1
    def __init__(robot, name):
        robot.name = name 
    
    
     
    def BeakLight(R, G, B):
        """Sets a tri-color LED in the Robot beak to a given color by setting the intensities of the red, green, and blue elements inside it.
    The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off.
        Example: Robot.setBeak(0,100,0)"""
        Errors.checkIfInvalidRGBValue(R,G,B)
        
        BeakLight = (R,G,B)
        
        return BeakLight
     
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
     
    def stop():
        Robot.setMotors(0,0)
    
     
    
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
    
     
    def setDisplay(LEDlist):
        """Sets the LED array of the micro:bit to display a pattern defined by a list of length 25. 
        Each value in the list must be 0 (off) or 1 (on). 
        The first five values in the array correspond to the five LEDs in the first row, the next five values to the second row, etc.
        Example: robot.setDisplay([1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1])"""
        # Validate input LEDlist
        if len(LEDlist) != 25:
            raise ValueError("LEDlist must have a length of 25")
        for value in LEDlist:
            if value not in (0, 1):
                raise ValueError("Each value in LEDlist must be 0 (off) or 1 (on)")

        return LEDlist

     
    def setPoint(LEDlist, row, column, value):
        """Turn on or off a single LED on the micro:bit display. The position of the LED is given by the row and column parameters, which should both be between 1 and 5.
        The value of the LED must be 0 (off) or 1 (on).
        Example:  robot.setPoint(3,3,1)"""
        # Validate row and column
        if not 1 <= row <= 5 or not 1 <= column <= 5:
            raise ValueError("Row and column values must be between 1 and 5")

        # Convert row and column to index in LED array
        index = (row - 1) * 5 + (column - 1)

        # Validate value
        if value not in (0, 1):
            raise ValueError("Value must be 0 (off) or 1 (on)")

        # Update LED array
        LEDlist[index] = value
        return LEDlist
     
    def digiPrint(message):
        """Print a string on the micro:bit LED array.
        The string must contain onlyEnglish letters. strings will default to uppercase if lowercase.
        Example: robot.digiPrint("Hello World")
        input string = 'Hello World'
        interpreted string = 'HELLO WORLD'
        """
        message.upper
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
            'Z': [' 1 1 1 1 1 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 1 1 1 1 1 '],
            '0': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            '1': [' 0 0 1 0 0 ', ' 0 1 1 0 0 ', ' 0 0 1 0 0 ', ' 0 0 1 0 0 ', ' 1 1 1 1 1 '],
            '2': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 1 1 1 1 0 '],
            '3': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 0 0 1 0 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            '4': [' 1 0 0 1 0 ', ' 1 0 0 1 0 ', ' 1 1 1 1 1 ', ' 0 0 0 1 0 ', ' 0 0 0 1 0 '],
            '5': [' 1 1 1 1 0 ', ' 1 0 0 0 0 ', ' 1 1 1 1 0 ', ' 0 0 0 0 1 ', ' 1 1 1 1 0 '],
            '6': [' 0 1 1 1 0 ', ' 1 0 0 0 0 ', ' 1 1 1 0 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            '7': [' 1 1 1 1 1 ', ' 0 0 0 1 0 ', ' 0 0 1 0 0 ', ' 0 1 0 0 0 ', ' 1 0 0 0 0 '],
            '8': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 0 1 1 0 0 '],
            '9': [' 0 1 1 0 0 ', ' 1 0 0 1 0 ', ' 0 1 1 1 0 ', ' 0 0 0 1 0 ', ' 0 1 1 0 0 ']
        }

        for row in range(5):
            for char in message:
                if char.upper() in alphabet:
                    print(alphabet[char.upper()][row], end=' ')
                else:
                    print('00000', end=' ')
            print()

     
    def display(LEDlist):
        # Print LED array in a 5x5 grid format
        for i in range(5):
            print(" ".join(str(x) for x in LEDlist[i * 5: (i + 1) * 5]))            
    
     
    def getVals(robot):
        """returns name of specified robot"""
        id = 1  
        return robot
