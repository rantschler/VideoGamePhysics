#
# Project Title: 
#
# Author:  
#

#
# PACKAGES
#

import gameclass_0_95 as gc
import pygame as pg
from pygame.locals import *
from sys import exit

#
# CLASSES
#

#
# FUNCTIONS
#

def draw_field(field,background,color = gc.BLACK):
    """ Modfies the background to mirror the playing surface.
    
        field - the gameclass Field object that represents the physical
                playing surface.
        background - the gameclass Background object that contains the 
                background image and scaling information to draw objects
                on the screen.
        color - the color of the background.
    """
    
    #
    # Import important quantities from background and field.
    #
    
    bg = background.get_size()
    fd = field.get_size()
    sz = field.get_fill()
    of = field.get_offset()
    
    #
    # Calculate scale and offset to be stored in the background class.
    #
    
    sc = float(bg[0])*sz/float(fd[0])
    background.set_scale(sc)
    offx = int(float(bg[0]) * of[0])
    offy = int(float(bg[1]) * of[1])
    background.set_offset((offx,offy))
    
    #
    # Fill the background with a single color and calculate the field
    # size in pixels.
    #
    
    area = pg.Surface(bg)
    area.convert()
    area.fill(color)
    
    area_size = (fd[0] * sc,fd[1] * sc)
    
    #
    # Draw your background below using the quantities above.
    #
    
    
    
    #
    # Draw onto the background.
    #
    
    background.detail(area,(offx,offy))
    
    pass
    

# 
# MVC FUNCTIONS
#

def engine(interval = 0,field = None,avatar = None,objects = []):
    ''' 
    The engine models the physics of your game by updating object
    positions, checking for collisions, and resolving them. 
    
        
        interval - time from last engine() call
        field - the field object that defines the playing area
        avatar - the player object
        objects - anything the avatar can interact with
                -or- another object can interact with.
    '''
    
    return None

def view(screen,background,avatar = None,objects = [],foreground = None):
    ''' The view function draws things to the screen. 
    
        screen - The name of the screen to draw objects on.
        background - the background object containing the background
                    picture and scaling information for the objects.
        avatar - the object under the player's direct control.
        objects - other objects that need to be drawn in the game.
        foreground - a single PyGame surface to overlay on top of the 
                    objects.
    '''
    
    background.draw(screen)
    scale = background.get_scale()
    offset = background.get_offset()
    
    #
    # Draw all objects below.
    #
    
    #
    # Draw all objects above.
    #
        
    pg.display.update()
    
    
    pass
    
def control(event,avatar = None, buttons = None):
    ''' Evaluates player input and sends messages to the avatar. 
    
        events - The pygame event list.
        avatar - The player object.
        buttons - A list of buttons that can directly control the avatar.
    '''

    pass
    
#
# MAIN
#

def main():
    ''' 
    Function that controls the game.
    Includes:   (1) Initialization of variables, objects and lists
                (2) Game model, including:
                    (a) a call to your physics engine
                (3) Calls to view function
                (4) Calls to control function.
    '''    
    
    #
    # Initialize screen and clock
    #
    
    screen_size = (800,600)
    screen = pg.display.set_mode(screen_size,RESIZABLE,32)
    background = gc.Background(screen.get_size(),gc.BLACK)
    field_size = (80.0,60.0)
    field_scale = 0.5
    field_offset = (0.0,0.0)
    field = gc.Field(field_size,field_scale,field_offset)
    field.imprint(draw_field,background)
    
    clock = pg.time.Clock()
    
    #
    # Initialize game objects and loop variables
    #

    #
    # Main loop for MVC game control.
    #
    while True:
        #
        # Update the time at the beginning of the loop.
        #
        
        interval = clock.tick(30)
        
        #
        # Model: All game mechanics
        ## Send physics problems to the engine.
        ## Resolve other mechanics (scoring, etc) here or in
        ## other functions
        #
        
        result = engine(interval,field)
        
        #
        # View: Draw all objects
        ## Send objects to the view function.
        #
        
        view(screen,background)
        
        #
        # Control: Take input from the user.
        ## Provide control of game state in the event loop.
        ## Call the control() function to control the avatar.
        #
        
        events = pg.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            if event.type == VIDEORESIZE:
                new_size = event.size
                screen = pg.display.set_mode(new_size,RESIZABLE,32)
                background.resize(new_size)
                field.imprint(draw_field,background)
            control(event,None)

    pass
    
#
# START UP
#



pg.init()

main()

