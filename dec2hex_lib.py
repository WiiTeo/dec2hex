# This file can be used in other Python file.
# just type this : from dec2hex import *

# DEC2HEX LIBRARY BY WIITEO

def DEC2HEX(dec):
    try:
        result = hex(dec)
        return result
    except ValueError:
        print("dec2hex_lib: String can not be converted.")
    except TypeError:
        print("dec2hex_lib: STR Error.")

# END OF DEC2HEX LIBRARY