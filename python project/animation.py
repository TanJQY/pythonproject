#********************************************************
# Program Author: Jodie Tan
# Revision Date: Jan. 23, 2022
# Program Name: Game Subprograms
# Description: This program contains subprograms for the
# game portion of the project
#********************************************************

#imports and initializes modules
import pygame
pygame.init()
import random
from variables import *



#generates a random number and returns which outcome should happen
def random_num(probability):
    number = random.randint(1, 100)
    if number < probability:
        return("outcome 1")
    else:
        return("outcome 2")
    
    
#draws dialogue box
def dialogue_box():
    #draws box
    pygame.draw.rect(game_display, white, (dialogue_box_x, dialogue_box_y, dialogue_box_length, dialogue_box_height), border_radius = 30)
    #draws border
    pygame.draw.rect(game_display, pink, (dialogue_box_x, dialogue_box_y, dialogue_box_length, dialogue_box_height), width = 3, border_radius = 30)



#displays the dialogue in the dialogue box
def display_dialogue(msg):
    
    #max words per line, used to indicate when a new line should be made
    max_words = 13
    
    #variables for the position of text
    x = dialogue_box_x + (dialogue_box_length/2)
    y = dialogue_box_y + 30
    
    #separates the dialogue into words
    words = msg.split()
    
    line = ""
    
    #finds how many lines there should be
    num_of_lines = len(words) // max_words
    
    #adds on an extra line for extra words
    if len(words) % max_words != 0:
        num_of_lines += 1
    
    for i in range(num_of_lines):
        for j in range(max_words): 
        
        #adds words to the current line and pops them out of the words list
            line += " " + words[0]
            words.pop(0)
            
            if len(words) == 0:
                break
            
        #displays the line of text    
        text = render_text(line, font_file, pink, 18)
        text_pos = text_rect(text)
        text_pos.center = (x , y)
        game_display.blit(text, text_pos)
        
        #updates y for the position of the next line, resets the words for the next line
        y += 25
        line = "" 
   
        

#displays a label for who is speaking
def speaker_box(who):
    x = 50
    y = 395
    height = 40
    length = int()
    
    #adjusts length depending on the name
    if who == "Hachiko":
        length = 115
    if who == "King":
        length = 100
    
    #draws rectangle and border
    pygame.draw.rect(game_display, white, (x, y, length, height), border_radius = 12)
    pygame.draw.rect(game_display, pink, (x, y, length, height), width = 3, border_radius = 12)
    
    #displays centered text 
    text = render_text(who, font_file, pink, 20)
    text_pos = text_rect(text)
    text_pos.center = ( (x + (length/2)), (y + (height/2)))
    game_display.blit(text, text_pos)



#displays the goodwill meter        
def goodwill_meter(filled):
    
    #variables for the position of goodwill meter
    x = 550
    y = 50
    length = 200
    height = 20
    
    #variables for the position of the text
    text_x = int()
    text_y = y - 10
    
    #adjusts position of text depending on the length of the value
    if len(str(filled)) == 1:
        text_x = x - 100
        
    if len(str(filled)) == 2:
        text_x = x - 120
    
    if len(str(filled)) == 3:
        text_x = x - 140
    
    #displays text
    text = "Goodwill: " + str(filled)
    text = render_text(text, font_file, white, 18)
    game_display.blit(text, (text_x, text_y))    
    
    #draws goodwill meter
    pygame.draw.rect(game_display, black, (x, y, length, height), border_radius = 30)    
    
    #draws filled portion
    if filled <= 0:
        pygame.draw.rect(game_display, white, (x, y, 0, height), border_radius = 30)
    
    elif filled > 100:
        pygame.draw.rect(game_display, white, (x, y, 200, height), border_radius = 30)        
    
    else:
        #filled portion is mutliplied by 2 since 1% of the bar is 2 pixels
        pygame.draw.rect(game_display, white, (x, y, (filled*2), height), border_radius = radius)
    
    #draws border
    pygame.draw.rect(game_display, pink, (x, y, length, height), width = 2, border_radius = 30)
    


