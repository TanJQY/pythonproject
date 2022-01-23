#********************************************************
# Program Author: Jodie Tan
# Revision Date: Jan. 23, 2022
# Program Name: Text Subprograms
# Description: This program contains subprograms used to 
# display text
#********************************************************

import pygame
pygame.init()
from variables import *

#function to render text
def render_text(text, font_file, font_colour, font_size):
    font = pygame.font.Font(font_file, font_size)   
    text = font.render(text, True, font_colour)
    return text

#function that gets text rectangle for positioning purposes
def text_rect(text):
    text_rect = text.get_rect()
    return text_rect
