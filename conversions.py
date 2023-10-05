import os
import time
import platform
import getpass
import sys
import base64
from rich.tree import Tree
from rich import print
from rich.console import Console

class main_logo:
    def logo():
        print(" [red1]___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |[/red1]\n")

class MySexyVariables:
    user = getpass.getuser()
    curdir = os.getcwd()
    #video_dir = os.path.join(os.path.expanduser("~"), "Videos")
    #audio_dir = os.path.join(os.path.expanduser("~"), "Music")
    #desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    #pics_dir = os.path.join(os.path.expanduser("~"), "Pictures")
    calls_list = [
                " The pit of Hades: bitwise operations",
                " Occult DataPsynce: datamancy",
                " The Voiceless Realm: string conversions",
                " One can not exit the place of the dead: exit"
                ]
    
    bitwise_calls_list = [ 
                " AND",
                " OR",
                " XOR",
                " NOT",
                " RIGHT SHIFT",
                " LEFT SHIFT"
                ]

class calls:
    @staticmethod
    def call_list():
        tree = Tree("[bright_black]" + " Levels of Hell", guide_style="purple")
        for i in MySexyVariables.calls_list:
            tree.add("[bright_black]" + str(i))
        print(" ", tree)

    @staticmethod
    def bitwise_list():
        tree = Tree("[bright_black]" + " Levels of Hell", guide_style="purple")
        for i in MySexyVariables.bitwise_calls_list:
            tree.add("[bright_black]" + str(i))
        print(" ", tree)

class Input:
    @staticmethod
    def get_string_input():
        console = Console()
        return console.input(" [bright_black]_______________________________________________[/bright_black]" + "[bright_black]\n  _ [/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (__ [/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black] __: [/bright_black]")
    
    @staticmethod
    def get_integer_input():
        console = Console()
        return int(console.input(" [bright_black]_______________________________________________[/bright_black]" + "[bright_black]\n  _ [/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (__ [/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black] __: [/bright_black]"))

    @staticmethod
    def get_float_input():
        console = Console()
        return float(console.input(" [bright_black]_______________________________________________[/bright_black]" + "[bright_black]\n  _ [/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (__ [/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black] __: [/bright_black]"))

def Bitwise_is_hard_af():
    time.sleep(2)
    os.system('clear')
    main_logo.logo()
    print(" [bright_black]Bitwise Sublevels: Hell\'s Calculator\n bitwise number or exit[/bright_black]")
    while True:
        calls.bitwise_list()
        print(' [red1]Enter an operator[/red1]')
        operation = Input.get_string_input()
        if operation.upper() == "MAIN HALL":
            print(" [bright_black]Exiting Bitwise Sublevels: Hell\'s Calculator")
            main()
        if operation.upper() == "EXIT":
            print(" [bright_black]Exiting Bitwise Sublevels: Hell\'s Calculator")
            sys.exit()
        if operation.upper() == "NOT":
            print(' Enter an number')
            num1 = Input.get_integer_input()
            # Convert numbers to binary and remove the '0b' prefix
            num1_bin = bin(num1)[2:]
            # Get the length of the binary numbers
            len_num1 = len(num1_bin)

            result = ~num1
            # Convert result to binary and remove the prefix
            result_bin_2_comp = bin((result & ((1 << len_num1) - 1)) + 1)[2:]
            # Convert result to binary and remove the prefix
            result_bin = '-' + bin(abs(result))[2:] if result < 0 else bin(result)[2:]
            new_result_2_comp = result_bin_2_comp
            if len(result_bin) > len(result_bin_2_comp):
                new_result_2_comp = result_bin_2_comp.zfill(len(num1_bin))
            if result < 0:
                print(' If a bit is 1, it becomes 0.\n If a bit is 0, it becomes 1.')
                print('  ' + num1_bin)
            else:
                print(' If a bit is 1, it becomes 0.\n If a bit is 0, it becomes 1. With 2\'s complement')
                print(' ' + num1_bin)
            print('  ' + new_result_2_comp)
            print(' ' + result_bin)  # print result_bin directly
            print(f" Result: {result}")

        else:
            print(' Enter an number')
            num1 = Input.get_integer_input()
            print(' Enter an second number')
            num2 = Input.get_integer_input()

            # Convert numbers to binary and remove the '0b' prefix
            num1_bin = bin(num1)[2:]
            num2_bin = bin(num2)[2:]

            # Get the length of the binary numbers
            len_num1 = len(num1_bin)
            len_num2 = len(num2_bin)

            # If the binary numbers have different lengths, pad the shorter one with zeros on the left
            if len_num1 > len_num2:
                num2_bin = num2_bin.zfill(len_num1)
            elif len_num2 > len_num1:
                num1_bin = num1_bin.zfill(len_num2)

            if operation.upper() == "AND":
                print(' 1 matching 1 is 1 everthing else is 0')
                result = num1 & num2
            elif operation.upper() == "OR":
                print(' 0 matching 0 is 0 everything else is 1')
                result = num1 | num2
            elif operation.upper() == "XOR":
                print(' eather 1 matching 0 is 1 xor 0 matching 1 is 1\n everything else is 0')
                result = num1 ^ num2
            elif operation.upper() == "RIGHT SHIFT":
                print(' floor-dividing the number by 2\n raised to the power of the number of positions to shift.\n Zeros added on the left.')
                result = num1 >> num2
            elif operation.upper() == "LEFT SHIFT":
                print(' multiplying the number by 2 \nraised to the power of the number of positions to shift.')
                result = num1 << num2
            else:
                print(" Invalid operation!")
                return

            print(' ' + num1_bin + ' first number in binary')
            print(' ' + num2_bin + ' second number in binary')
            print(' ' + bin(result)[2:].zfill(max(len_num1, len_num2)) + ' binary result')
            print(f" Result: {result}")
            continue

def convert_to_codes(input_value):
    chr_string = ""
    ascii_string = ""
    binary_string = ""
    unicode_string = ""
    hexadecimal_string = ""
    octal_string = ""

    for char in input_value:
        ascii_code = ord(char)  # Convert character to ASCII
        binary_code = bin(ascii_code)[2:]  # Convert ASCII to binary
        unicode_code = "\\u" + hex(ascii_code)[2:]  # Convert ASCII to Unicode
        hexadecimal_code = hex(ascii_code)[2:]  # Convert ASCII to hexadecimal
        octal_code = oct(ascii_code)[2:]  # Convert ASCII to octal

        chr_string += char + " "
        ascii_string += str(ascii_code) + " "
        binary_string += binary_code + " "
        unicode_string += unicode_code + " "
        hexadecimal_string += hexadecimal_code + " "
        octal_string += octal_code + " "

        print(f"Character: {char} ASCII: {ascii_code} Binary: {binary_code} Unicode: {unicode_code} Unicode Decimal: {ascii_code} Hexadecimal: {hexadecimal_code} Octal: {octal_code}")

    encoded_s = base64.b64encode(input_value.encode())

    return chr_string, ascii_string, binary_string, unicode_string, hexadecimal_string, octal_string, encoded_s

def string_conversions():
    while True:
        print(' [bright_black]Input a string to convert\n or no string to exit.[/bright_black]')
        input_value = Input.get_string_input()
        if input_value == '':
            print(' Exiting current sublevel.')
            main()
        else:
            chr_string, ascii_string, binary_string, unicode_string, hexadecimal_string, octal_string, encoded_s = convert_to_codes(input_value)
            print(f"Character String: {chr_string}")
            print(f"ASCII String: {ascii_string}")
            print(f"Binary String: {binary_string}")
            print(f"Unicode String: {unicode_string}")
            print(f"Hexadecimal String: {hexadecimal_string}")
            print(f"Octal String: {octal_string}")
            print(f"Base64 Encoded String: {encoded_s.decode()}")

def main():
    if platform.system() == 'Linux':
        main_logo.logo()
        print(" [bright_black]Data Enocding Psynter[/bright_black]")
        print(" [bright_black]Welcome to Hell!\n Please choose a level to be cast into.[/bright_black]")
        while True:
            calls.call_list()
            commands = Input.get_string_input()
            if commands == "exit":
                print(" [bright_black]Exiting Hell")
                sys.exit()
            if commands == "bitwise operations":
                Bitwise_is_hard_af()
            if commands == "datamancy":
                datamancy()
            if commands == "string conversions":
                string_conversions()

if __name__ == "__main__":
    print(f" System: {platform.system()}\n Node Name: {platform.node()}\n Release: {platform.release()}")
    print(f" Version: {platform.version()}\n Machine: {platform.machine()}\n Python version: {platform.python_version()}")
    time.sleep(2)
    os.system('clear')
    main()