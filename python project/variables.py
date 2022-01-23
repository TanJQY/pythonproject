#********************************************************
# Program Author: Jodie Tan
# Revision Date: Jan. 23, 2022
# Program Name: Variables
# Description: This program declares, initializes and 
# assigns values to variables to be used in other programs
#********************************************************

import pygame
pygame.init()
from text import *


# declares and initializes variables for displaying the window
window_size = (800, 650)
game_display = pygame.display.set_mode(window_size)

#defines some colours
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 0, 85)
darker_pink = (255, 0, 50)
red = (255, 102, 102)
green = (191, 255, 128)
blue = (179, 204, 255)
cream = (255, 255, 204)

game_icon = pygame.image.load("game icon.png")
game_icon = pygame.transform.scale(game_icon, (8, 8))

font_file = "PlayfairDisplayRegular.ttf"
#*****************************************************************************
#title screen components
# declares variables for text and opens text file
title_info = open("main menu info.txt","r")
project = title_info.readline() 
name = title_info.readline()
date = title_info.readline()
course = title_info.readline()

# gets rid of new line character
project = project[0:-1]
name = name[0:-1]
date = date[0:-1]

project = render_text(project, font_file, black, 20)
name = render_text(name, font_file, black, 20)
date = render_text(date, font_file, black, 20)
course = render_text(course, font_file, black, 20)

title_bg = pygame.image.load("title screen.png")

#*****************************************************************************
# main menu components
menu_bg = pygame.image.load("main menu bg.png")

#*****************************************************************************
# quit components
citations = pygame.image.load("credits.png")

#*****************************************************************************
# lesson components
# loads lesson background images
behavior_bg = pygame.image.load("Behavior.png")
behavior_bg = pygame.transform.scale(behavior_bg, (800, 650))
care_needs_bg = pygame.image.load("care_needs.png")
care_needs_bg = pygame.transform.scale(care_needs_bg, (800, 650))
history1_bg = pygame.image.load("History.png")
history1_bg = pygame.transform.scale(history1_bg, (800, 650))
history2_bg = pygame.image.load("History_part_2.png")
history2_bg = pygame.transform.scale(history2_bg, (800, 650))

#******************************************************************************
# quiz components
done_quiz = False
score = int(0)

quiz_instructions_bg = pygame.image.load("quiz instructions.png")
# questions and answers
quiz_text = open("quiz text.txt","r")
q1 = quiz_text.readline()

q1a = quiz_text.readline()
q1b = quiz_text.readline()
q1c = quiz_text.readline()
q1d = quiz_text.readline()
q1e = quiz_text.readline()


q2 = quiz_text.readline()

q2a = quiz_text.readline()
q2b = quiz_text.readline()
q2c = quiz_text.readline()
q2d = quiz_text.readline()


q3 = quiz_text.readline()

q3a = quiz_text.readline()
q3b = quiz_text.readline()
q3c = quiz_text.readline()
q3d = quiz_text.readline()


q4 = quiz_text.readline()

q4a = quiz_text.readline()
q4b = quiz_text.readline()
q4c = quiz_text.readline()
q4d = quiz_text.readline()


q5 = quiz_text.readline()

q5a = quiz_text.readline()
q5b = quiz_text.readline()
q5c = quiz_text.readline()
q5d = quiz_text.readline()


q6 = quiz_text.readline()

q6a = quiz_text.readline()
q6b = quiz_text.readline()
q6c = quiz_text.readline()
q6d = quiz_text.readline()

q7 = quiz_text.readline()

q7a = quiz_text.readline()
q7b = quiz_text.readline()
q7c = quiz_text.readline()
q7d = quiz_text.readline()
q7e = quiz_text.readline()


q8 = quiz_text.readline()

q8a = quiz_text.readline()
q8b = quiz_text.readline()
q8c = quiz_text.readline()
q8d = quiz_text.readline()
q8e = quiz_text.readline()


q9 = quiz_text.readline()

q9a = quiz_text.readline()
q9b = quiz_text.readline()
q9c = quiz_text.readline()
q9d = quiz_text.readline()
q9e = quiz_text.readline()


q10 = quiz_text.readline()

q10a = quiz_text.readline()
q10b = quiz_text.readline()
q10c = quiz_text.readline()
q10d = quiz_text.readline()
q10e = quiz_text.readline()


q1 = q1[0:-1]
q1a = q1a[0:-1]
q1b = q1b[0:-1]
q1c = q1c[0:-1]
q1d = q1d[0:-1]
q1e = q1e[0:-1]

q2 = q2[0:-1]
q2a = q2a[0:-1]
q2b = q2b[0:-1]
q2c = q2c[0:-1]
q2d = q2d[0:-1]

q3 = q3[0:-1]
q3a = q3a[0:-1]
q3b = q3b[0:-1]
q3c = q3c[0:-1]
q3d = q3d[0:-1]

q4 = q4[0:-1]
q4a = q4a[0:-1]
q4b = q4b[0:-1]
q4c = q4c[0:-1]
q4d = q4d[0:-1]

q5 = q5[0:-1]
q5a = q5a[0:-1]
q5b = q5b[0:-1]
q5c = q5c[0:-1]
q5d = q5d[0:-1]

q6 = q6[0:-1]
q6a = q6a[0:-1]
q6b = q6b[0:-1]
q6c = q6c[0:-1]
q6d = q6d[0:-1]

q7 = q7[0:-1]
q7a = q7a[0:-1]
q7b = q7b[0:-1]
q7c = q7c[0:-1]
q7d = q7d[0:-1]
q7e = q7e[0:-1]

q8 = q8[0:-1]
q8a = q8a[0:-1]
q8b = q8b[0:-1]
q8c = q8c[0:-1]
q8d = q8d[0:-1]
q8e = q8e[0:-1]

q9 = q9[0:-1]
q9a = q9a[0:-1]
q9b = q9b[0:-1]
q9c = q9c[0:-1]
q9d = q9d[0:-1]
q9e = q9e[0:-1]

q10 = q10[0:-1]
q10a = q10a[0:-1]
q10b = q10b[0:-1]
q10c = q10c[0:-1]
q10d = q10d[0:-1]
q10e = q10e[0:-1]



# loads remarks for quiz result
remarks = open("result remarks.txt","r")
perfect = remarks.readline()
almost_perfect = remarks.readline()
mediocre = remarks.readline()
failed = remarks.readline()
not_done = remarks.readline()

#******************************************************************************
# game components
#declares variables for text and opens text file
dialogues = open("dialogues.txt","r")
part1_line = dialogues.readline()

part2_line1 = dialogues.readline()
part2_line2 = dialogues.readline()

part4_line1 = dialogues.readline()
part4_line2 = dialogues.readline()

part5a_line1 = dialogues.readline()
part5a_line2 = dialogues.readline()
part5a_line3 = dialogues.readline()
part5b_line1 = dialogues.readline()
part5b_line2 = dialogues.readline()
part5c_line1 = dialogues.readline()
part5c_line2 = dialogues.readline()
part5c_line3 = dialogues.readline()

part6_line1 = dialogues.readline()

part7_line1 = dialogues.readline()
part7_line2 = dialogues.readline()
part7_line3 = dialogues.readline()

part8_line1 = dialogues.readline()
part8_line2 = dialogues.readline()
part8_line3 = dialogues.readline()
part8_line4 = dialogues.readline()

part9_line1 = dialogues.readline()
part9_line2 = dialogues.readline()

part10_line1 = dialogues.readline()
part10_line2 = dialogues.readline()
part10_line3 = dialogues.readline()
part10_line4 = dialogues.readline()
part10_line5 = dialogues.readline()
part10_line6 = dialogues.readline()
part10_line7 = dialogues.readline()
part10_line8 = dialogues.readline()
part10_line9 = dialogues.readline()

part11_line1 = dialogues.readline()
riddle = dialogues.readline()

part12_line1 = dialogues.readline()
part12_line2 = dialogues.readline()

part13_line1 = dialogues.readline()
part13_line2 = dialogues.readline()
part13_line3 = dialogues.readline()

part14_line1 = dialogues.readline()

ending1_line1 = dialogues.readline()

ending2_line1 = dialogues.readline()

ending3_line1 = dialogues.readline()

ending4_line1 = dialogues.readline()

ending5_line1 = dialogues.readline()

uniform_instructions = dialogues.readline()
uniform_instructions = uniform_instructions[0: -1]

card_instructions = dialogues.readline()



#loads images
instructions_bg = pygame.image.load("instructions.png")
prologue_bg = pygame.image.load("prologue.png")

hallway_bg = pygame.image.load("hallway4.jpg")
hallway_bg = pygame.transform.scale(hallway_bg, window_size)

bedroom_bg = pygame.image.load("bedroom.jpg")
bedroom_bg = pygame.transform.scale(bedroom_bg, window_size)

throne_room_bg = pygame.image.load("throne room.jpg")
throne_room_bg = pygame.transform.scale(throne_room_bg, window_size)

dining_hall_bg = pygame.image.load("dining hall.jpg")
dining_hall_bg = pygame.transform.scale(dining_hall_bg, window_size)

hachiko_neutral = pygame.image.load("hachiko.png")
hachiko_neutral = pygame.transform.scale(hachiko_neutral, (250, 372))

hachiko_angry = pygame.image.load("angry hachiko.png")
hachiko_angry = pygame.transform.scale(hachiko_angry, (250, 372))

pj_king_angry = pygame.image.load("angry pj king.png")
pj_king_angry = pygame.transform.scale(pj_king_angry, (280, 372))

pj_king_happy = pygame.image.load("happy pj king.png")
pj_king_happy = pygame.transform.scale(pj_king_happy, (280, 372))

king_angry = pygame.image.load("angry king.png")
king_angry = pygame.transform.scale(king_angry, (250, 372))

king_neutral = pygame.image.load("king.png")
king_neutral = pygame.transform.scale(king_neutral, (250, 372))

king_happy = pygame.image.load("happy king.png")
king_happy = pygame.transform.scale(king_happy, (250, 372))

story_bg = pygame.image.load("story.png")

poisoned_card = pygame.image.load("poison card.png")
haunted_card = pygame.image.load("ghost card.png")
jousting_card = pygame.image.load("joust card.png")

mom_card = pygame.image.load("mother card.png")
kitchen_card = pygame.image.load("kitchen card.png")
murders_card = pygame.image.load("murders card.png")

witch_card = pygame.image.load("witch card.png")
taxes_card = pygame.image.load("taxes card.png")
painter_card = pygame.image.load("painter card.png")

uniform1 = pygame.image.load("butler.png")
uniform1 = pygame.transform.scale(uniform1, (223, 362))
uniform2 = pygame.image.load("maid.png")
uniform2 = pygame.transform.scale(uniform2, (220, 354))

pickle = pygame.image.load("pickle.png")
pheasant = pygame.image.load("pheasant.png")
prosciutto = pygame.image.load("prosciutto.png")

rose_pot = pygame.image.load("roses.png")
rose_pot = pygame.transform.scale(rose_pot, (300, 300))

restaurant = pygame.image.load("restaurant.png")
restaurant = pygame.transform.scale(restaurant, (366, 326))

guillotine = pygame.image.load("guillotine.png")
guillotine = pygame.transform.scale(guillotine, (301, 389))

bed = pygame.image.load("bed.png")
bed = pygame.transform.scale(bed, (440, 362))

#defines some variables for displaying dialogue
dialogue_box_x = 50
dialogue_box_y = 445
dialogue_box_length = 700
dialogue_box_height = 200

#defines variables used for goodwill meter
filled_amount = int(50)

