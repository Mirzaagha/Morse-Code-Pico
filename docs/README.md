# Morse Code Encoder/Decoder for Raspberry Pi Pico

This project implements a Morse Code Encoder and Decoder using the Raspberry Pi Pico and MicroPython. It allows users to **convert text into Morse code and decode Morse code back into text using the serial console.

## Features
✅ Convert text to Morse code  
✅ Convert Morse code to text  
✅ Works entirely in software, no additional hardware required  
✅ Runs on Raspberry Pi Pico using MicroPython  

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Usage](#example-usage)
- [Morse Code Reference](#morse-code-reference)
---

## Installation
### 1. Install MicroPython on Raspberry Pi Pico
If you haven’t installed MicroPython, follow these steps:
1. Download the latest MicroPython UF2 file from the [official site](https://micropython.org/download/rp2-pico/).
2. Connect Raspberry Pi Pico to your computer while holding the BOOTSEL button.
3. Drag and drop the UF2 file onto the Pico.

### 2. Install Thonny (Python IDE)
- Download [Thonny](https://thonny.org/).
- Select MicroPython (Raspberry Pi Pico) as the interpreter.

### 3. Clone the Repository
sh
git clone https://github.com/Mirzaagha/Morse-Code-Pico.git
cd Morse-Code-Pico


### 4. Upload the Code to Pico
1. Open Thonny.
2. Copy the files to the Raspberry Pi Pico:
   - src/main.py
   - src/morse.py
3. Run main.py on the Pico.

---

## Usage
1. Open Thonny and run main.py on the Pico.
2. Enter text to convert it into Morse code.
3. Enter Morse code (dots and dashes) to convert it back into text.

### Running via Serial (Alternative)
1. Open a serial terminal (like PuTTY or screen):
   sh
   screen /dev/ttyUSB0 115200
## *Project Structure*
```sh
Morse-Code-Pico/
│── src/
│   ├── main.py            # Main script (handles user input/output)
│   ├── morse.py           # Morse code logic (encoding/decoding)
│── docs/
│   ├── README.md          # Project documentation
│── .gitignore             # Ignore unnecessary files
│── LICENSE                # Open-source license
```
## Example Usage
sh
Enter text (or Morse code) to convert:
> SOS
Morse Code: ... --- ...

Enter text (or Morse code) to convert:
> ... --- ...
Decoded Text: SOS

---

## *Morse Code Reference*
```sh
Character | Morse Code
----------------------
A         | .-
B         | -...
C         | -.-.
D         | -..
E         | .
S         | ...
O         | ---
1         | .----
2         | ..---
3         | ...--
```
---

### Author
```sh
Mirzaagha Guliyev
GitHub: @Mirzaagha (https://github.com/Mirzaagha)
