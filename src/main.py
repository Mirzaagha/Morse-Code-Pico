<<<<<<< HEAD

=======
import machine
import utime
import sys
from morse import text_to_morse, morse_to_text

def main():
    while True:
        print("Enter text (or Morse code) to convert: ")
        user_input = sys.stdin.readline().strip()

        if '-' in user_input or '.' in user_input:
            print(f"Decoded text: {morse_to_text(user_input)}")
        else:
            print(f"Morse Code: {text_to_morse(user_input)}")

        utime.sleep(1)

if _name_ == "_main_":
    main()
>>>>>>> 07d7ea1 (Initial commit)
