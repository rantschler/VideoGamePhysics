#
# Logic Lights
# In-Class Assignment 5
#

#
# Import Modules
#

import gameclass as gc
import pygame as pg
from pygame.locals import *
from sys import exit

#
# Global Constants
#

HEIGHT = 650
WIDTH = 950
SCREEN_SIZE = (WIDTH,HEIGHT)

#
# CLASSES
#

#
# FUNCTIONS
#

def draw_background(background):
    """ Draws analagous wiring onto the background.

        background is a gameclass Background object."""
    
    #
    # Create a field to draw
    #
    
    field = pg.Surface(background.get_size())
    field.convert()
    field.fill(gc.BLACK)
    
    #
    # Draw analogy here:
    #
    
    pg.draw.line(field,gc.WHITE,(250,375),(250,325),2)
    pg.draw.line(field,gc.WHITE,(175,175),(175,550),2)
    
    pg.draw.line(field,gc.WHITE,(400,375),(400,250),2)
 #   pg.draw.line(field,gc.WHITE,(550,250),(550,325),2)
    pg.draw.line(field,gc.WHITE,(175,325),(475,325),2)
    pg.draw.line(field,gc.WHITE,(400,250),(550,250),2)
    pg.draw.line(field,gc.WHITE,(325,300),(325,175),2)
    
 #   pg.draw.line(field,gc.WHITE,(475,375),(400,375),2)
    pg.draw.line(field,gc.WHITE,(475,500),(475,325),2)
    pg.draw.line(field,gc.WHITE,(475,225),(475,175),2)
    pg.draw.line(field,gc.WHITE,(550,250),(550,375),2)
    
    
    pg.draw.line(field,gc.WHITE,(550,250),(850,250),2)
    pg.draw.line(field,gc.WHITE,(700,250),(700,500),2)
    pg.draw.line(field,gc.WHITE,(475,500),(700,500),2)
    pg.draw.line(field,gc.WHITE,(600,175),(850,175),2)
    pg.draw.line(field,gc.WHITE,(850,550),(850,175),2)
    pg.draw.line(field,gc.WHITE,(175,550),(850,550),2)
    pg.draw.line(field,gc.WHITE,(700,400),(850,400),2)
    
    gc.draw_not(field,(150,236),50)
    gc.draw_not(field,(600,225),50)
    gc.draw_not(field,(675,300),50)
    gc.draw_not(field,(750,225),50)
    gc.draw_not(field,(825,300),50)
    gc.draw_or(field,(300,300),50)
    gc.draw_or(field,(675,225),50)
    gc.draw_or(field,(825,225),50)
    gc.draw_and(field,(825,375),50)
    gc.draw_and(field,(450,225),50)
    
    
    gc.screenprint(field,"not-A",[150,120])
    gc.screenprint(field,"A or B",[300,120])
    gc.screenprint(field,"B and C",[440,120])
    gc.screenprint(field ,"not-(B and C)",[575,70])
    gc.screenprint(field ,"and",[610,95])
    gc.screenprint(field ,"not-(not-B or not-C)",[550,120])
    
    pg.draw.circle(field,gc.BLACK,[175,175],25)
    pg.draw.circle(field,gc.BLACK,[325,175],25)
    pg.draw.circle(field,gc.BLACK,[475,175],25)
    pg.draw.circle(field,gc.BLACK,[625,175],25)
    
    pg.draw.circle(field,gc.WHITE,[175,175],25,3)
    pg.draw.circle(field,gc.WHITE,[325,175],25,3)
    pg.draw.circle(field,gc.WHITE,[475,175],25,3)
    pg.draw.circle(field,gc.WHITE,[625,175],25,3)


    gc.screenprint(field,"2",[170,165])
    gc.screenprint(field,"4a",[315,165])
    gc.screenprint(field,"4b",[465,165])
    gc.screenprint(field,"5",[620,165])
    
    
    gc.screenprint(field,"A",[245,410])
    gc.screenprint(field,"B",[395,410])
    gc.screenprint(field,"C",[545,410])

    #
    # Draw onto the background.
    #
    
    background.detail(field,(0,0))
    
    pass
    

# 
# MVC FUNCTIONS
#

def engine(objects,interval):
    ''' The engine models the physics of your game by updating object
    positions, checking for collisions, and resolving them. '''
        
    return None

def view(screen,background,objects = None,foreground = None):
    ''' The view function draws things to the screen. '''
    
    background.draw(screen)
    
    #
    # Draw all objects below.
    #
    
    
    for object in objects:
        object.draw(screen)
    
    #
    # Draw all objects above.
    #
        
    pg.display.update()
    
    
    pass
    
def control(events,lights = None, buttons = None):
    ''' Evaluates player input and sends messages to the avatar. '''
    
    for event in events:
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            for i in range(len(buttons)):
                if buttons[i].is_clicked(pos):
                    lights[i].toggle()

    pass
    

def main():
    ''' Function that controls the game.
        Includes: (1) Initialization of variables, objects and lists
                  (2) Game model
                  (3) Calls to view function
                  (4) Calls to control function.'''    
    
    #
    # Initialize screen and clock
    #
    
    screen = pg.display.set_mode(SCREEN_SIZE,0,32)
    background = gc.Background(screen.get_size(),gc.BLACK)
    
    clock = pg.time.Clock()
    
    #
    # Initialize game objects and loop variables
    #
    
    draw_background(background)
    
    lightA = gc.Light([225,350],25,[gc.YELLOW,gc.GRAY])
    lightB = gc.Light([375,350],25,[gc.YELLOW,gc.GRAY])
    lightC = gc.Light([525,350],25,[gc.YELLOW,gc.GRAY])
    
    lights = [lightA,lightB,lightC]
    
    
    
    buttons = []
    
    
    results = []
    
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
        ## other 
        #
        
        
        result = engine([],interval)
        
        #
        # View: Draw all objects
        ## Send objects to the view function.
        #
        
        view(screen,background,lights+buttons+results)
        
        #
        # Control: Give commands to the player's avatar.
        ##
        #
        
        control(pg.event.get(),lights,buttons)

    pass
    
#
# INITIALIZATION
#

pg.init()

main()
