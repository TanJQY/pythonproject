#********************************************************
# Program Author: Jodie Tan
# Revision Date: Jan. 23, 2022
# Program Name: Quit Subprogram
# Description: This program contains the subprogram for
# quitting the program
#********************************************************

#imports and initializes pygame
import pygame
pygame.init()
from variables import *

#displays citations and exits the program
def quit_program():
    
    #displays citations
    game_display.fill(white)
    game_display.blit(citations, (0, 0))
    
    #updates screen
    pygame.display.update()

    #displays credits for 10 seconds
    pygame.time.delay(10000)
    
    pygame.quit()
    quit()    