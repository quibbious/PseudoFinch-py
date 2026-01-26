import os

class Errors:
    """handles errors experienced by the pseudofinch Finches"""

    @staticmethod
    def printError(message):
        # generic error printing
        print("\033[91m" + message + "\033[0m")  # ANSI escape code for red text (GPT code)
        

    @staticmethod
    def isValidRGB(RED: int = 0, GREEN: int = 0, BLUE: int = 0):
        # no need for hard-coding a list for no reason, just use some basic IF statements instead.

        if (RED > 0 or RED < 255): Errors.printError(f"RED is not 0-255.")
            return False
        if (GREEN > 0 or GREEN < 255): Errors.printError(f"GREEN is not 0-255.") 
            return False
        if (BLUE > 0 or BLUE < 255): Errors.printError(f"BLUE is not 0-255.")
            return False

class Finch:
    """Main class for the MANY functions of a pseudofinch Finch"""
    global beakColor, tailColor
    global logFile
    beakColor = []
    tailColor = []
    if os.path.exists("actions.log"):
        os.remove("actions.log")
    logFile = open("actions.log", "a")

    def __init__(self, name: str = None, Finch_id: int = None) -> None:
        self.name = name
        self.Finch_id = Finch_id
        logFile.write(f"Finch '{name}' with id '{Finch_id}' initiated.\n")
        if not name:
            Errors.printError("No Finch name; please specify a Finch.")

    def beakLight(self, RED: int = 0, GREEN: int = 0, BLUE: int = 0):
        """Sets a tri-color LED in the Finch beak to a given color by setting the intensities of the red, green, and blue elements inside it. The method requires three intensity values from 0-255. Setting all three intensity values to 0 turns the beak off.
        \n Example: Finch.setBeak(0,100,0)"""

        Errors.isValidRGB()
        logFile.write(f"Finch.beakLight({RED}, {GREEN}, {BLUE}).\n")
        beakColor = [RED, GREEN, BLUE]
        return [RED, GREEN, BLUE]

    def setMove(self, direction: str = 'F', distance: int = 0, speed: int = 0):
        """Moves the Finch forward 'F', or backwards 'B', followed by a distance in cm and a speed from 1-100.
        \n Example: Finch.setMove(‘F’,10,50)"""

        direction = direction.upper()

        if direction not in ('F', 'B'): Errors.printError("Invalid direction; must be 'F' or 'B'.")
        if speed not in range(101): Errors.printError("Speed must be 1-100")
        if distance < 1: Errors.printError("Distance cannot be below one")
        logFile.write(f"Finch.setMove({direction},{distance},{speed})\n")
        return direction, distance, speed

    def setTurn(self, direction: str = 'R', angle: int = 0, speed: int = 0):
        """Turns the Finch right or left for a specified angle at a specified speed. The method requires a direction (‘R’ for right or ‘L’ for left), an angle in degrees, and a speed from 0-100.
        \n Example: Finch.setTurn(‘R’,90,50)"""

        direction = direction.upper()

        if speed not in range(101): Errors.printError("Invalid speed, must be 0-100")
        if angle not in range(1, 361): Errors.printError("Angle out of range; must be 1-360")

        match direction:
            case ('L'):
                return direction, -angle, speed
            case ('R'):
                return direction, angle, speed
            case _:
                return Errors.printError(f"invalid direction '{direction}'")
        logFile.write(f"Finch.setMove({direction},{angle},{speed}).\n")

    def setMotors(self, LEFT: int = 0, RIGHT: int = 0):
        """Sets the Finch wheels to spin at the given speeds. Requires two speeds between -100 and 100 for the left and right wheels. Setting the speed to 0 turns the motor off.
        \n Example: Finch.setMotors(-100, 100)"""
        if not all(-100 <= speed <= 100 for speed in (LEFT, RIGHT)): Errors.printError(
            "Speed must be between -100 and 100")
        logFile.write(f"Finch.setMotors({LEFT},{RIGHT}).\n")
        return [LEFT, RIGHT]

    def setTail(self, port, RED: int = 0, GREEN: int = 0, BLUE: int = 0):
        """Sets a tri-color LED in the Finch tail to a given color by setting the intensities of the red, green, and blue elements inside it. The method requires the port number of the LED (1, 2, 3, 4, or “all”) and three intensity values from 0-100.  Setting all three intensity values to 0 turns the LED off.
        \n Example: Finch.setTail(“all”,0,100,0)"""
        if port not in (1, 2, 3, 4, 'all'):
            Errors.printError(f"invalid port {port}; check docstring for instructions")

        Errors.isValidRGB(RED, GREEN, BLUE)
        logFile.write(f"Finch.setTail({port}, {RED}, {GREEN}, {BLUE}).\n")
        tailColor = [port, RED, GREEN, BLUE]
        return [port, RED, GREEN, BLUE]

    def playNote(self, note, beats):
        """Plays a note using the buzzer on the Finch. The method requires an integer representing the note (32-135) and a number giving the number of beats (0-16). One beat corresponds to one second.
        \n Example: Finch.playNote(60,0.5)"""
        if note not in range(32, 136):
            Errors.printError(f"playNote: note ({note}) must be in range 32-135")
        if beats not in range(1, 17):
            Errors.printError(f"playNote: beats ({beats}) must be in range 0-16")
        logFile.write(f"Finch.playNote({note}, {beats}).\n")
        return [note, beats]

    def setDisplay(self, LEDlist: list = None):
        """Sets the LED array of the micro:bit to display a pattern defined by a list of length 25.  Each value in the list must be 0 (off) or 1 (on). The first five values in the array correspond to the five LEDs in the first row, the next five values to the second row, etc.
        \n Example: Finch.setDisplay([1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1])"""
        if len(LEDlist) == 25 and (state_led in (0, 1) for state_led in LEDlist):
            logFile.write(f"Finch.setDisplay({LEDlist}).\n")
            return LEDlist
        else:
            Errors.printError("setDisplay: list is either not 25 in length or not 0s and 1s")

    def setPoint(self, row, column, value):
        """Turn on or off a single LED on the micro:bit display. The position of the LED is given by the row and column parameters, which should both be between 1 and 5. The value of the LED must be 0 (off) or 1 (on).
        \n Example:  robot.setPoint(3,3,1)"""
        if not (1 <= row <= 5) or not (1 <= column <= 5):
            raise ValueError("Row and column values must be between 1 and 5")
        if value not in (0, 1):
            raise ValueError("Value must be 0 (off) or 1 (on)")

        index = (row - 1) * 5 + (column - 1)
        LEDlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # completely empty list
        LEDlist[index] = value
        logFile.write(f"Robot.setPoint({row}, {column} ,{value}).\n")
        return LEDlist

    def digiPrint(self, message):
        """Print a string on the micro:bit LED array. The string must contain only English letters. strings will default to uppercase if lowercase. *will break and glitch after 20 chars, including whitespace.
        \n Example: robot.digiPrint("Hello World")"""
        if len(message) > 20:
            Errors.printError("Message length cannot be more than 20.")

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
            for char in message.upper():
                print(alphabet.get(char, ['     '])[row], end=' ')
            print()
        logFile.write(f"Robot.digiPrint({message}).\n")
        return True  # for tests
