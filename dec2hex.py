# DEC2HEX WiiTeo Program

# DEC2HEX PROGRAM BY WIITEO

try:
    ask = int(input("Decimal : "))

    ask_result = hex(ask)

    print(ask_result)
except ValueError:
    print("dec2hex: String can not be converted.")
except TypeError:
        print("dec2hex: STR Error.")