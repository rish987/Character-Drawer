"""
Filename: character_drawer.py

Author: Rishikesh Vaishnav

Created:
24/03/2017

Last Modified:
Fri 24 Mar 2017 11:42:41 PM PDT

Description:
This program provides an easy-to-use environment where a user can draw a symbol
that represents an ASCII character, enter what character they drew, and save
the data representing their drawing and the number it is associated with it, as
well as a .png image file of their drawing.

These files will be saved in a folder in this program's directory called:
num_data/[character drawn]_saved

'character drawn' refers to the ASCII character the user associated this
character to when creating the file.

The data and pictures will be saved in this folder's subdirectories called:
data/ 
pics/

Data files will be named:
[num]_[character drawn]_data.dat

Picture files will be named:
[num]_[character drawn]_pic.png

'num' refers to the next number after the maximum numbered file already in that
folder. Think of it as the ID number of this drawn character.

The data file will contain the following:
- On the first line, the ASCII character this number represents
- On the second line, the list of pixel values drawn on the screen, represented
as 0s (not drawn) and 1s (drawn), starting from the upper left corner and going
from left to right and top to bottom.
"""
from Tkinter import *

def main ():
"""
Sets up the canvas for drawing and using this program.
"""
    # TODO create the canvas with appropriate dimensions
    # TODO add field to: enter text
    # TODO make sure that field only accepts one character
    # TODO add buttons to: save image, clear canvas
    # TODO set up event listeners
    # TODO set up the necessary folders
    # TODO TODO anymore setup that needs to be done
    # TODO begin canvas loop

# TODO TODO write event listeners
def press_mouse ( event ):
"""
Handles pressing the mouse button by turning on a boolean that lets the program
know that a mouse button is being pressed.

Parameters:
event - the event that triggered this method
"""
    # TODO turn on mouse pressed indicator boolean

def release_mouse ( event ):
"""
Handles releasing the mouse button by turning off a boolean that lets the
program know that a mouse button is being pressed.

Parameters:
event - the event that triggered this method
"""
    # TODO turn off mouse pressed indicator boolean

def clear_button ( event ):
"""
Handles the user pressing the clear button by clearing their drawing from the
screen.

Parameters:
event - the event that triggered this method
"""
    # TODO TODO clear the drawing

def save_button ( event ):
"""
Handles the user pressing the clear button by clearing their drawing from the
screen.

Parameters:
event - the event that triggered this method
"""
    # TODO check that the text field has one character in it to associate with
    # this drawing
    # TODO TODO save the drawing's data
    # TODO TODO save the drawing's image

# start the program
main();
