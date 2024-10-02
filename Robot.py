import sys

class Errors:
    """Contains many errors relating to Pseudofinch Robots"""
    
     
    def printError(message):
        print("\033[91m" + f"{message}" + "\033[0m")  # ANSI escape code for red text
        sys.exit()

     
    def RGBValueError():
        Errors.printError("ValueError: invalid RGB range, must be between 0-255")

     
    def isInvalidRGBValue(R, G, B):
        
        if R not in range(0,256):
            return True, Errors.RGBValueError() # return True because the value IS invalid, and return a RGBValueError.
        elif G not in range(0,256):
            return True, Errors.RGBValueError()
        elif B not in range(0,256):
            return True, Errors.RGBValueError() 
        else:
            return False # as in the RGB values are NOT invalid

     
    def directionError():
        Errors.printError("Invalid direction; must be 'F' or 'B'.")
     
    def MissingRobotError():
        Errors.printError("No robot detected; please specify a robot.")
    
    def SpeedValueError():
        Errors.printError("ValueError: Speed must be between 1-100")

class Robot:
    
    """Constructor that creates an object corresponding to a Robot, as well as a corresponding ID"""
    
    def __init__(robot, name, id):
        robot.name = name
        robot.id = id 
        if not robot.name:
            Errors.MissingRobotError()
     
    def BeakLight(self,R, G, B):
        """Sets a tri-color LED in the Robot beak to a given color by setting the intensities of the red, green, and blue elements inside it.
    The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off.
        Example: Robot.setBeak(0,100,0)"""
        Errors.isInvalidRGBValue(R,G,B) #checks if the values are invalid
        
        BeakLight = (R,G,B)
        
        return BeakLight
     
    def setMove(self,direction=str, distance=int, speed=int):
        
        """Moves the robot forward 'F', or backwards 'B', followed by a distance in cm and a speed from 1-100.
        Example: Robot.setMove(‘F’,10,50)"""
        direction = direction.upper()
        if direction not in ('F','B'):
            
            Errors.printError(f"SyntaxError: invalid movement direction {direction}")
            
        if speed not in range(1,101):
           
            Errors.SpeedValueError()
        
        if distance < 1: 
            
            Errors.printError("ValueError: distance cannot be below one (1)")
        
        return direction, distance, speed
     
    def setTurn(self,direction=str, angle=int, speed=int):
        """Turns the Robot right or left for a specified angle at a specified speed.
        The method requires a direction (‘R’ for right or ‘L’ for left), an angle in degrees, and a speed from 0-100.
        Example: Robot.setTurn(‘R’,90,50)"""
        direction = direction.upper()
        if direction not in ('L','R'): 
            Errors.printError(f"SyntaxError: invalid direction '{direction}'")
        
        if speed not in range (0,101):
            Errors.printError("ValueError: invalid speed, must be between 0-100")
            
        if not angle in range(1,361): # 360 degree limit per command 
            Errors.printError("ValueError: Angle out of range; must be 1-360")

        if direction == 'L':
            invertedangle = -1  * angle
            return direction, invertedangle, speed
        
        return direction, angle, speed
     
    def setMotors(self, L: int, R: int):
        """Sets the Robot wheels to spin at the given speeds.
        Requires two speeds between -100 and 100 for the left and right wheels.
        Setting the speed to 0 turns the motor off.
        Example: Robot.setMotors(-50, 50)
        """
        if not (-100 <= L <= 100) or not (-100 <= R <= 100):
            Errors.printError("Speed must be between -100 and 100")
    
        return [L, R]
    
    def setTail(self,port, r, g, b):
        """Sets a tri-color LED in the Robot tail to a given color by setting the intensities of the red, green, and blue elements inside it.
        The method requires the port number of the LED (1, 2, 3, 4, or “all”) and three intensity values from 0-100. 
        Setting all three intensity values to 0 turns the LED off.
        Example: Robot.setTail(“all”,0,100,0)"""
    
        if port != 1 or 2 or 3 or 4 or 'all':
            Errors.printError("SyntaxError: invalid selection; check docstring for instructions")

        Errors.isInvalidRGBValue(r,g,b)

        tailvaluesRGB = [port,r,g,b]
        
        return tailvaluesRGB
    
     
    def playNote(self,note: int,beats: int):
        """Plays a note using the buzzer on the Robot.
        The method requires an integer representing the note (32-135) and a number giving the number of beats (0-16). 
        One beat corresponds to one second.
        Example: Robot.playNote(60,0.5)"""
        
        if note not in range(31,136):
            Errors.printError("ValueError: note must be in range 32-135")
        
        
        if beats not in range(0,17):
            Errors.printError("ValueError: beat must be in range 0-16")

        options = [note,beats]

        return options
    
     
    def setDisplay(self, LEDlist):
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

     
    def setPoint(self, LEDlist, row, column, value):
        """Turn on or off a single LED on the micro:bit display. The position of the LED is given by the row and column parameters, which should both be between 1 and 5.
        The value of the LED must be 0 (off) or 1 (on).
        Example:  robot.setPoint(3,3,1)"""
        # Validate row and column
        #if row and column not in (1, 2, 3, 4, 5):
        #    raise ValueError("Row and column values must be between 1 and 5")
        
        if row not in (1,2,3,4,5):
            raise ValueError("Row value must be between 1 and 5")

        if column not in (1, 2, 3, 4, 5):
            raise ValueError("Column value must be between 1 and 5")
        # Convert row and column to index in LED array
        index = (row - 1) * 5 + (column - 1)

        # Validate value
        if value not in (0, 1):
            raise ValueError("Value must be 0 (off) or 1 (on)")

        # Update LED array
        LEDlist[index] = value
        return LEDlist
     
    def digiPrint(self, message):
        """Print a string on the micro:bit LED array.
        The string must contain onlyEnglish letters. strings will default to uppercase if lowercase.
        Example: robot.digiPrint("Hello World")
        input string = 'Hello World'
        interpreted string = 'HELLO WORLD'
        *will break and glitch after 20 chars, including whitespace.
        """
        
        if len(message) > 20: 
            Errors.printError("message length cannot be more than 20.") # Because it glitches out past 20 chars. dont know why yet. 
        
        message.upper
        alphabet = {
            'A': ['   1 1     ', ' 1     1   ', ' 1     1   ', ' 1 1 1 1   ', ' 1     1   '],
            'B': [' 1 1 1     ', ' 1     1   ', ' 1 1 1     ', ' 1     1   ', ' 1 1 1     '],
            'C': ['   1 1     ', ' 1     1   ', ' 1         ', ' 1     1   ', '   1 1     '],
            'D': [' 1 1 1     ', ' 1     1   ', ' 1     1   ', ' 1     1   ', ' 1 1 1     '],
            'E': [' 1 1 1 1   ', ' 1         ', ' 1 1 1     ', ' 1         ', ' 1 1 1 1   '],
            'F': [' 1 1 1 1   ', ' 1         ', ' 1 1 1     ', ' 1         ', ' 1         '],
            'G': [' 1 1 1 1   ', ' 1         ', ' 1   1 1   ', ' 1     1   ', ' 1 1 1 1   '],
            'H': [' 1     1   ', ' 1     1   ', ' 1 1 1 1   ', ' 1     1   ', ' 1     1   '],
            'I': ['   1 1 1 1 ', '     1 1   ', '     1 1   ', '     1 1   ', '   1 1 1 1 '],
            'J': ['     1 1   ', '       1   ', '       1   ', ' 1     1   ', '   1 1     '],
            'K': [' 1     1   ', ' 1   1     ', ' 1 1       ', ' 1   1     ', ' 1     1   '],
            'L': [' 1         ', ' 1         ', ' 1         ', ' 1         ', ' 1 1 1 1   '],
            'M': [' 1       1 ', ' 1 1   1 1 ', ' 1   1   1 ', ' 1       1 ', ' 1       1 '],
            'N': [' 1       1 ', ' 1 1     1 ', ' 1   1   1 ', ' 1     1 1 ', ' 1       1 '],
            'O': [' 1 1 1 1 1 ', ' 1       1 ', ' 1       1 ', ' 1       1 ', ' 1 1 1 1 1 '],
            'P': [' 1 1 1 1   ', ' 1     1   ', ' 1 1 1 1   ', ' 1         ', ' 1         '],
            'Q': ['   1 1 1   ', ' 1       1 ', ' 1   1   1 ', ' 1     1   ', '   1 1   1 '],
            'R': [' 1 1 1     ', ' 1     1   ', ' 1 1 1     ', ' 1   1     ', ' 1     1   '],
            'S': ['   1 1 1   ', ' 1         ', '   1 1     ', '       1   ', ' 1 1 1     '],
            'T': [' 1 1 1 1 1 ', '     1     ', '     1     ', '     1     ', '     1     '],
            'U': [' 1       1 ', ' 1       1 ', ' 1       1 ', ' 1       1 ', '   1 1 1   '],
            'V': [' 1       1 ', ' 1       1 ', ' 1       1 ', '   1   1   ', '     1     '],
            'W': [' 1   1   1 ', ' 1   1   1 ', ' 1   1   1 ', ' 1   1   1 ', ' 1 1 1 1 1 '],
            'X': [' 1       1 ', '   1   1   ', '     1     ', '   1   1   ', ' 1       1 '],
            'Y': [' 1       1 ', '   1   1   ', '     1     ', '     1     ', '     1     '],
            'Z': [' 1 1 1 1 1 ', '       1   ', '     1     ', '   1       ', ' 1 1 1 1 1 '],
            '0': ['   1 1     ', ' 1     1   ', ' 1     1   ', ' 1     1   ', '   1 1     '],
            '1': ['     1     ', '   1 1     ', '     1     ', '     1     ', ' 1 1 1 1 1 '],
            '2': ['   1 1     ', ' 1     1   ', '     1     ', '   1       ', ' 1 1 1 1   '],
            '3': ['   1 1     ', ' 1     1   ', '     1     ', ' 1     1   ', '   1 1     '],
            '4': [' 1     1   ', ' 1     1   ', ' 1 1 1 1 1 ', '       1   ', '       1   '],
            '5': [' 1 1 1 1   ', ' 1         ', ' 1 1 1 1   ', '         1 ', ' 1 1 1 1   '],
            '6': ['   1 1 1   ', ' 1         ', ' 1 1 1     ', ' 1     1   ', '   1 1     '],
            '7': [' 1 1 1 1 1 ', '       1   ', '     1     ', '   1       ', ' 1         '],
            '8': ['   1 1     ', ' 1     1   ', '   1 1     ', ' 1     1   ', '   1 1     '],
            '9': ['   1 1     ', ' 1     1   ', '   1 1 1   ', '       1   ', '   1 1     '],
            '-': ['           ', '           ', ' 1 1 1 1 1 ', '           ', '           '],
            '+': ['     1     ', '     1     ', ' 1 1 1 1 1 ', '     1     ', '     1     '],
            '/': ['         11', '       11  ', '     11    ', '   11      ', ' 11        '],
            '*': ['     1     ', '   1 1 1   ', '     1     ', '           ', '           '],
            '=': ['           ', ' 1 1 1 1 1 ', '           ', ' 1 1 1 1 1 ', '           '],
            
            
            
        }
    
        for row in range(5):
            for char in message:
                if char.upper() in alphabet:
                    print(alphabet[char.upper()][row], end=' ')
                else:
                    print('     ', end=' ') # optional to replace whitespace with 0's 
            print()
        return True, "message printed"


