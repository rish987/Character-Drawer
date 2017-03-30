"""
Filename: character_drawer.py

Author: Rishikesh Vaishnav

Created:
24/03/2017

Last Modified:
Wed 29 Mar 2017 11:53:13 PM PDT

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

# window size (both width and height)
WINDOW_SIZE = 300;

# padding of all components inside of window
PADDING = 20

# minimum and maximum drawing canvas sizes
DC_MIN_SIZE = 10;
DC_MAX_SIZE = 100;

# drawing canvas size (both width and height)
# NOTE: must evenly divide DC_SIZE_PX
DC_SIZE = 20;

# drawing canvas size in pixels (both width and height)
DC_SIZE_PX = 200;

def main ():
    """
    Sets up the canvas for drawing and using this program.
    """
    # set up the window with TODO appropriate dimensions 
    window = Tk();
    window.wm_title( "Character Drawer" );
    window.resizable( width=False, height=False );
    window.geometry( '{}x{}'.format( WINDOW_SIZE, WINDOW_SIZE ) );
    window.configure( background='white' );

    # --- TODO create the drawing canvas with its grid ---

    # initialize the canvas with constant dimensions
    drawing_canvas = Canvas( window, width=DC_SIZE_PX, height=DC_SIZE_PX,
        background='white', highlightbackground='black', 
        highlightcolor='black' );
    
    # load the drawing canvas
    drawing_canvas.pack( padx=PADDING, pady=PADDING );

    # number of lines to draw on the grid
    num_lines = DC_SIZE - 1;

    # offset of lines to draw on the grid
    lines_offset = DC_SIZE_PX / DC_SIZE;

    # go through all gridlines to be drawn
    for line_i in range( 0, num_lines ):
        # the x and y pixel position of the line to be drawn
        pos = ( line_i + 1 ) * lines_offset;

        # draw the x and y gridlines
        drawing_canvas.create_line( 0, pos, DC_SIZE_PX, pos,
            fill='light grey' );
        drawing_canvas.create_line( pos, 0, pos, DC_SIZE_PX, 
            fill='light grey' );

    # ---

    # TODO add field to: enter text
    # TODO make sure that field only accepts one character
    # TODO add buttons to: save image, clear canvas
    # TODO set up event listeners
    # TODO set up the necessary folders
    # TODO TODO anymore setup that needs to be done

    # begin window loop
    window.mainloop();

    # end program TODO remove?
    # window.destroy();

# TODO TODO write event listeners
def press_mouse ( event ):
    """
    Handles pressing the mouse button by turning on a boolean that lets the
    program know that a mouse button is being pressed.

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
    Handles the user pressing the clear button by clearing their drawing
    from the screen.

    Parameters:
    event - the event that triggered this method
    """
    # TODO TODO clear the drawing

def save_button ( event ):
    """
    Handles the user pressing the save button by saving their drawing's image
    and data to file.

    Parameters:
    event - the event that triggered this method
    """
    # TODO check that the text field has one character in it to associate with
    # this drawing
    # TODO TODO save the drawing's data
    # TODO TODO save the drawing's image

# start the program
main();
