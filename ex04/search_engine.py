import os

import msvcrt
import sys
from BST import BST


def get_char():
     """Read one character from stdin without pressing Enter."""
     try:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
             tty.setraw(fd)
             ch = sys.stdin.read(1)
        finally:
             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
     except ImportError:
         # Windows fallback
         return msvcrt.getch().decode("utf-8")

def search_loop():
    bst = BST(r"C:\faculta\an 3\AI\Labs\lab2\lab02-Sebastian2710\ex04\wordlist.txt",file=True)
    prefix=""
    print("Start typing (press ESC to quit):")

    while True:
            ch = get_char()

            # Exit on ESC
            if ord(ch) == 27:
                print("\nExiting...")
                break

            # Backspace (delete last char)
            if ch in ("\b", "\x7f"):  
                prefix = prefix[:-1]
            elif ch == "\r":  # ignore Enter key
                continue
            else:
                prefix += ch.lower()

            # Clear screen for neat output
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Current input >> {prefix}")

            suggestions = bst.autocomplete(prefix)

            if suggestions:
                for s in suggestions[:5]:  # show only first 5 suggestions
                    print(s)
            else:
                print("No matches found.")