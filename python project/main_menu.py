#********************************************************
# Program Author: Jodie Tan
# Revision Date: Jan. 23, 2022
# Program Name: Main Menu
# Description: This program contains subprograms for the
# main menu and its options: lesson, quiz, quiz results
# and game
#********************************************************

import pygame
pygame.init()
from animation import *
from quit import *
from variables import *
from text import *

# multiple button functions due to the need for different information needed to be passed from part to part
# draws buttons, directs user to different sections depending on the button pressed
def main_button(msg, x, y, length, height, border, radius, border_colour, button_colour, action, font_size, font_colour, score, done_quiz):
    
    #draws button
    pygame.draw.rect(game_display, button_colour, (x, y, length, height), width = 0, border_radius = radius)
    
    #defines some variables related to the mouse
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #if the mouse is hovering on the button draw a border 
    if x + length > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_display, border_colour, (x, y, length, height), width = border, border_radius = radius)
        
        if click[0] == 1:
            #checks and plays which part should happen next
            if action == "main menu":
                main_menu(score, done_quiz)
                
            if action == "game":
                animation(score, done_quiz)
                
            if action == "lesson":
                lesson(1, score, done_quiz)
            
            if action == "lesson 2":
                lesson(2, score, done_quiz)
            
            if action == "lesson 3":
                lesson(3, score, done_quiz)
            
            if action == "lesson 4":
                lesson(4, score, done_quiz)
            
            if action == "quiz":
                quiz(0, score, done_quiz)
                
            if action == "results":
                quiz_results(score, done_quiz)
            
            if action == "quit":
                quit_program()
                
    #renders text
    text = render_text(msg, font_file, font_colour, font_size)
    
    #centers the text on the button
    text_pos = text_rect(text)
    text_pos.center = ( (x + (length/2)), (y + (height/2)))
    
    #blits text on the button
    game_display.blit(text, text_pos)
    

def game_button(msg, x, y, length, height, border, radius, border_colour, button_colour, action, font_size, font_colour, goodwill, score, done_quiz):
    
    #draws button
    pygame.draw.rect(game_display, button_colour, (x, y, length, height), width = 0, border_radius = radius)
    
    #defines some variables related to the mouse
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #if the mouse is hovering on the button draw a border 
    if x + length > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_display, border_colour, (x, y, length, height), width = border, border_radius = radius)
        
        if click[0] == 1:
            #checks and plays which part should happen next
            if action == "main menu":
                main_menu(score, done_quiz)
                
            if action == "prologue":
                prologue(score, done_quiz)
                
            if action == "part 1":
                part_1(score, done_quiz)
                
            if action == "part 2":
                part_2(goodwill, score, done_quiz)
            
            if action == "part 2.1":
                part_2_1(goodwill, score, done_quiz)
                
            if action == "part 3 a":
                part_3("a", goodwill, score, done_quiz)
           
            if action == "part 3 b":
                part_3("b", goodwill, score, done_quiz)
            
            if action == "part 4":
                part_4(goodwill, score, done_quiz)
            
            if action == "part 4.1":
                part_4_1(goodwill, score, done_quiz)
            
            if action == "part 5 a":
                part_5("a", goodwill, score, done_quiz)
                
            if action == "part 5 b":
                part_5("b", goodwill, score, done_quiz)
                
            if action == "part 5 c":
                part_5("c", goodwill, score, done_quiz)
            
            if action == "part 5.1a":
                part_5_1("a", goodwill, score, done_quiz)
                
            if action == "part 5.1b":
                part_5_1("b", goodwill, score, done_quiz)
                
            if action == "part 5.1c":
                part_5_1("c", goodwill, score, done_quiz)
                
            if action == "part 6":
                part_6(goodwill, score, done_quiz)
            
            if action == "part 7 a":
                part_7("a", goodwill, score, done_quiz)
            
            if action == "part 7 b":
                part_7("b", goodwill, score, done_quiz)
            
            if action == "part 7.1":
                part_7_1(goodwill, score, done_quiz)
            
            if action == "part 7.2":
                part_7_2(goodwill, score, done_quiz)
            
            if action == "part 8 a":
                part_8("a", goodwill, score, done_quiz)
            
            if action == "part 8 b":
                part_8("b", goodwill, score, done_quiz)
            
            if action == "part 8.1 a":
                part_8_1("a", goodwill, score, done_quiz)
            
            if action == "part 8.1 b":
                part_8_1("b", goodwill, score, done_quiz)
                
            if action == "part 9 a":
                part_9("a", goodwill, score, done_quiz)
           
            if action == "part 9 b":
                part_9("b", goodwill, score, done_quiz)
            
            if action == "part 10":
                part_10(goodwill, score, done_quiz)
            
            if action == "part 10.1a":
                part_10_1("a", goodwill, score, done_quiz)
            
            if action == "part 10.1b":
                part_10_1("b", goodwill, score, done_quiz)
            
            if action == "part 10.1c":
                part_10_1("c", goodwill, score, done_quiz)
            
            if action == "part 10.2":
                part_10_2(goodwill, score, done_quiz)
            
            if action == "part 10.3a":
                part_10_3("a", goodwill, score, done_quiz)
            
            if action == "part 10.3b":
                part_10_3("b", goodwill, score, done_quiz)
            
            if action == "part 10.3c":
                part_10_3("c", goodwill, score, done_quiz)
            
            if action == "part 10.4":
                part_10_4(goodwill, score, done_quiz)
            
            if action == "part 10.5a":
                part_10_5("a", goodwill, score, done_quiz)
            
            if action == "part 10.5b":
                part_10_5("b", goodwill, score, done_quiz)
            
            if action == "part 10.5c":
                part_10_5("c", goodwill, score, done_quiz)
                
            if action == "part 11":
                part_11(goodwill, score, done_quiz)
            
            if action == "part 11.1":
                part_11_1(goodwill, score, done_quiz)
            
            if action == "part 12 a":
                part_12("a", goodwill, score, done_quiz)
                
            if action == "part 12 b":
                part_12("b", goodwill, score, done_quiz)
        
            if action == "part 13":
                part_13(goodwill, score, done_quiz)
            
            if action == "part 13.1a":
                part_13_1("a", goodwill, score, done_quiz)
            
            if action == "part 13.1b":
                part_13_1("b", goodwill, score, done_quiz)
                
            if action == "part 14":
                part_14(goodwill, score, done_quiz)
                
            if action == "ending 1":
                ending_1(goodwill, score, done_quiz)
            
            if action == "ending 2":
                ending_2(goodwill, score, done_quiz)
            
            if action == "ending 3":
                ending_3(goodwill, score, done_quiz)
            
            if action == "ending 4":
                ending_4(goodwill, score, done_quiz)
            
            if action == "ending 5":
                ending_5(goodwill, score, done_quiz)
            
            
    #renders text
    text = render_text(msg, font_file, font_colour, font_size)
    
    #centers the text on the button
    text_pos = text_rect(text)
    text_pos.center = ( (x + (length/2)), (y + (height/2)))
    
    #blits text on the button
    game_display.blit(text, text_pos)
    
def quiz_button(msg, x, y, length, height, border, radius, border_colour, button_colour, action, font_size, font_colour, next_question, score, done_quiz):
    
    #draws button
    pygame.draw.rect(game_display, button_colour, (x, y, length, height), width = 0, border_radius = radius)
    
    #defines some variables related to the mouse
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #if the mouse is hovering on the button draw a border 
    if x + length > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_display, border_colour, (x, y, length, height), width = border, border_radius = radius)
        
        if click[0] == 1:
            #checks and runs which part should happen next
            if action == "correct":
                correct(next_question, score, done_quiz)
                
            if action == "incorrect":
                incorrect(next_question, score, done_quiz)
            
            if action == "next question":
                quiz(next_question, score, done_quiz)
      
    #renders text
    text = render_text(msg, font_file, font_colour, font_size)
    
    #centers the text on the button
    text_pos = text_rect(text)
    text_pos.center = ( (x + (length/2)), (y + (height/2)))
    
    #blits text on the button
    game_display.blit(text, text_pos)



            

# title screen subprogram
def title_screen():
    running = True   
    while running:
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption("Title Screen")
        
        # displays background
        game_display.fill(white)
        game_display.blit(title_bg, (0,0))

        # displays title of project
        game_display.blit(project,(400,175))   
        game_display.blit(name,(400,225))  
        game_display.blit(date,(400,275))  
        game_display.blit(course,(400,325)) 
        
        main_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, score, done_quiz)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update() 


# main menu subprogram
def main_menu(score, done_quiz):
    running = True   
    while running:
        pygame.display.set_caption("Main Menu")
        
        # displays background
        game_display.fill(white)
        game_display.blit(menu_bg, (0,0))
        
        # draws buttons
        main_button("Start Game", 100, 150, 150, 50, 2, 30, black, pink, "game", 18, white, score, done_quiz)  
        main_button("Lesson", 100, 225, 150, 50, 2, 30, black, pink, "lesson", 18, white, score, done_quiz)  
        main_button("Quiz", 100, 300, 150, 50, 2, 30, black, pink, "quiz", 18, white, score, done_quiz)  
        main_button("Quiz Results", 100, 375, 150, 50, 2, 30, black, pink, "results", 18, white, score, done_quiz)  
        main_button("Quit", 100, 450, 150, 50, 2, 30, black, pink, "quit", 18, white, score, done_quiz)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        # Update display
        pygame.display.update() 



#*******************************************************************************************************
# LESSON SUBPROGRAMS
def lesson(part, score, done_quiz):
    running = True   
    while running:
        pygame.display.set_caption("Lesson")
        game_display.fill(white)
        
        # displays a different part of the lesson, based on what button was pressed
        if part == 1:
            game_display.blit(behavior_bg, (0,0))
        
            main_button("Next", 450, 570, 120, 40, 2, 30, black, cream, "lesson 2", 18, black, score, done_quiz)  
        
        if part == 2:
            game_display.blit(care_needs_bg, (0,0))
        
            main_button("Next", 650, 615, 120, 40, 2, 30, black, cream, "lesson 3", 18, black, score, done_quiz)  
            main_button("Back", 100, 615, 120, 40, 2, 30, black, cream, "lesson", 18, black, score, done_quiz) 
    
        if part == 3:
            game_display.blit(history1_bg, (0,0))
        
            main_button("Next", 450, 600, 120, 40, 2, 30, black, cream, "lesson 4", 18, black, score, done_quiz)  
            main_button("Back", 250, 600, 120, 40, 2, 30, black, cream, "lesson 2", 16, black, score, done_quiz)
        
        if part == 4:
            game_display.blit(history2_bg, (0,0))
                
            main_button("Back", 100, 600, 120, 40, 2, 30, black, cream, "lesson 3", 16, black, score, done_quiz)         
        
        main_button("Back to main menu", 400, 15, 300, 30, 2, 30, black, cream, "main menu", 16, black, score, done_quiz)
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        # Update display
        pygame.display.update() 


#*******************************************************************************************************
# QUIZ RELATED SUBPROGRAMS
# subprogram for quiz
def quiz(question, score, done_quiz):
    running = True
    while running:
        game_display.fill(blue)
        
        # displays different part of quiz depending on which question the user is on
        if question == 0:
            game_display.blit(quiz_instructions_bg, (0, 0))
            quiz_button("Next", 550, 550, 150, 50, 2, 30, black, cream, "next question", 18, black, 1, score, False)
            
        if question == 1:
            text = render_text(q1, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q1a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 2, score, done_quiz)
            quiz_button(q1b, 125, 200, 500, 40, 2, 30, black, cream, "correct", 18, black, 2, score, done_quiz)
            quiz_button(q1c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 2, score, done_quiz)
            quiz_button(q1d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 2, score, done_quiz)
            quiz_button(q1e, 125, 350, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 2, score, done_quiz)
        
        if question == 2:
            text = render_text(q2, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q2a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 3, score, done_quiz)
            quiz_button(q2b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 3, score, done_quiz)
            quiz_button(q2c, 125, 250, 500, 40, 2, 30, black, cream, "correct", 18, black, 3, score, done_quiz)
            quiz_button(q2d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 3, score, done_quiz)
        
        if question == 3:
            text = render_text(q3, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q3a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 4, score, done_quiz)
            quiz_button(q3b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 4, score, done_quiz)
            quiz_button(q3c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 4, score, done_quiz)
            quiz_button(q3d, 125, 300, 500, 40, 2, 30, black, cream, "correct", 18, black, 4, score, done_quiz)
        
        if question == 4:
            text = render_text(q4, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q4a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 5, score, done_quiz)
            quiz_button(q4b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 5, score, done_quiz)
            quiz_button(q4c, 125, 250, 500, 40, 2, 30, black, cream, "correct", 18, black, 5, score, done_quiz)
            quiz_button(q4d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 5, score, done_quiz)
        
        if question == 5:
            text = render_text(q5, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q5a, 125, 150, 500, 40, 2, 30, black, cream, "correct", 18, black, 6, score, done_quiz)
            quiz_button(q5b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 6, score, done_quiz)
            quiz_button(q5c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 6, score, done_quiz)
            quiz_button(q5d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 6, score, done_quiz)
        
        if question == 6:
            text = render_text(q6, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q6a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 7, score, done_quiz)
            quiz_button(q6b, 125, 200, 500, 40, 2, 30, black, cream, "correct", 18, black, 7, score, done_quiz)
            quiz_button(q6c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 7, score, done_quiz)
            quiz_button(q6d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 7, score, done_quiz)
            
        if question == 7:
            text = render_text(q7, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q7a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 8, score, done_quiz)
            quiz_button(q7b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 8, score, done_quiz)
            quiz_button(q7c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 8, score, done_quiz)
            quiz_button(q7d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 8, score, done_quiz)
            quiz_button(q7e, 125, 350, 500, 40, 2, 30, black, cream, "correct", 18, black, 8, score, done_quiz)
        
        if question == 8:
            text = render_text(q8, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q8a, 125, 150, 500, 40, 2, 30, black, cream, "correct", 18, black, 9, score, done_quiz)
            quiz_button(q8b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 9, score, done_quiz)
            quiz_button(q8c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 9, score, done_quiz)
            quiz_button(q8d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 9, score, done_quiz)
            quiz_button(q8e, 125, 350, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 9, score, done_quiz)
        
        if question == 9:
            text = render_text(q9, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q9a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 10, score, done_quiz)
            quiz_button(q9b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 10, score, done_quiz)
            quiz_button(q9c, 125, 250, 500, 40, 2, 30, black, cream, "correct", 18, black, 10, score, done_quiz)
            quiz_button(q9d, 125, 300, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 10, score, done_quiz)
            quiz_button(q9e, 125, 350, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 10, score, done_quiz)
        
        if question == 10:
            text = render_text(q10, font_file, black, 20)
            game_display.blit(text, (100, 100))
            
            quiz_button(q10a, 125, 150, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 11, score, done_quiz)
            quiz_button(q10b, 125, 200, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 11, score, done_quiz)
            quiz_button(q10c, 125, 250, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 11, score, done_quiz)
            quiz_button(q10d, 125, 300, 500, 40, 2, 30, black, cream, "correct", 18, black, 11, score, done_quiz)
            quiz_button(q10e, 125, 350, 500, 40, 2, 30, black, cream, "incorrect", 18, black, 11, score, done_quiz)
            
        main_button("Back to main menu", 20, 20, 200, 30, 2, 30, black, cream, "main menu", 16, black, score, done_quiz)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
    
        pygame.display.update()           


# subprogram to be run when user gets a correct answer
def correct(next_question, score, done_quiz):
    running = True
    while running:
        # displays background
        game_display.fill(green)
        
        # displays other components
        game_display.blit(king_happy, (100, 100))
        pygame.draw.rect(game_display, black, (100, 100, 250, 372), width = 10)
        
        text = render_text("Correct", font_file, black, 40)
        game_display.blit(text, (450, 100))        
        
        # if the question answered was the last question
        if next_question == 11:
            main_button("Back to main menu", 20, 20, 200, 30, 2, 30, black, cream, "main menu", 18, black, (score + 1), True )
        
        else:
            quiz_button("Next", 550, 550, 150, 50, 2, 30, black, cream, "next question", 18, black, next_question, (score + 1), False)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
    
        pygame.display.update()           
    
# subprogram to be run when user gets an incorrect answer
def incorrect(next_question, score, done_quiz):
    running = True
    while running:  
        # displays background
        game_display.fill(red)
        
        # displays other components
        game_display.blit(king_angry, (100, 100))
        pygame.draw.rect(game_display, black, (100, 100, 250, 372), width = 10)
        
        text = render_text("Incorrect", font_file, black, 40)
        game_display.blit(text, (450, 100))         
        
        # if the question answered was the last question
        if next_question == 11:
            main_button("Back to main menu", 20, 20, 200, 30, 2, 30, black, cream, "main menu", 18, black, score, True)
        
        else:
            quiz_button("Next", 550, 550, 150, 50, 2, 30, black, cream, "next question", 18, black, next_question, score, False)          
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
    
        pygame.display.update()           

def quiz_results(score, done_quiz):
    running = True
    
    remark = ""
    
    percent = str()
    # score is out of ten thus simply multiply by ten for the percentage
    percent = str(score * 10) + "%"
    
    fraction = str()
    fraction = str(score) + " / 10"
    
    while running:
        game_display.fill(black)
        
        # checks whether quiz has been done
        if not done_quiz:
            game_display.blit(king_angry, (100, 100))
            remark = not_done
            
        else:
            # displays score
            text = render_text("Results", font_file, white, 30)
            game_display.blit(text, (500, 100))        
            
            text = render_text(fraction, font_file, white, 30)
            game_display.blit(text, (525, 200))
            
            text = render_text(percent, font_file, white, 30)
            game_display.blit(text, (525, 300))
            
            if score == 10:
                game_display.blit(king_happy, (100, 100))
                remark = perfect
                
            # if score is 8 - 9
            elif score > 7:
                game_display.blit(king_neutral, (100, 100))
                remark = almost_perfect
                
            # if score is 5 - 7
            elif score > 4:
                game_display.blit(king_neutral, (100, 100))
                remark = mediocre 
                
            # if score is under 5
            else:
                game_display.blit(king_angry, (100, 100))
                remark = failed
        
        speaker_box("King")
        dialogue_box()     
        display_dialogue(remark)
        
        main_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, black, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
    
        pygame.display.update()        

#*******************************************************************************************************
# GAME SUBPROGRAMS
#code for the instructions section called animation for simplicity when being called in the main menu
def animation(score, done_quiz):
    running = True
    while running:
        pygame.display.set_caption("King Shiba")
        
        #displays background
        game_display.fill(white)
        game_display.blit(instructions_bg, (0, 0))
    
        game_button("Back", 30, 30, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 300, 570, 150, 50, 2, 30, black, pink, "prologue", 20, white, 0, score, done_quiz)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()



def prologue(score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(prologue_bg, (0, 0))
      
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz) 
        game_button("Next", 475, 570, 150, 50, 2, 30, black, pink, "part 1", 20, white, 0, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()




def part_1(score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays hachiko sprite, dialogue box and speaker
        game_display.blit(hachiko_neutral, (100, 100))
        
        dialogue_box()
        speaker_box("Hachiko")
        
        #displays goodwill meter
        goodwill_meter(filled_amount)
        
        #displays dialogue
        display_dialogue(part1_line)
        
        #draws buttons
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Yes, I am.", 410, 230, 340, 40, 2, 30, black, pink, "part 2", 16, white, filled_amount, score, done_quiz)
        game_button("Sorry, I think you have the wrong person.", 410, 280, 340, 40, 2, 30, black, pink, "ending 1", 16, white, filled_amount, score, done_quiz)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()                                 
        
        pygame.display.update()
    
    
    
def part_2(goodwill, score, done_quiz):
    running = True
    
    #calculates how much goodwill meter goes up
    filled_amount = goodwill 
    filled_amount += random.randint(1, 5)
    
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays hachiko sprite, dialogue box and other components
        game_display.blit(hachiko_neutral, (100, 100))
        
        dialogue_box()
        display_dialogue(part2_line1)
        
        goodwill_meter(filled_amount)

        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 2.1", 18, white, filled_amount, score, done_quiz)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                           
        pygame.display.update()




def part_2_1(goodwill, score, done_quiz):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays hachiko sprite and other components
        game_display.blit(hachiko_neutral, (100, 100))                
        
        speaker_box("Hachiko")
        
        dialogue_box()
        display_dialogue(part2_line2)
        
        goodwill_meter(goodwill)
        
        #draws buttons
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Try to escape", 450, 230, 300, 40, 2, 30, black, pink, "part 3 a", 16, white, goodwill, score, done_quiz)
        game_button("Follow instructions", 450, 280, 300, 40, 2, 30, black, pink, "part 3 b", 16, white, goodwill, score, done_quiz)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
               
        pygame.display.update()
        
        
        
def part_3(part, goodwill, score, done_quiz):
    running = True
    while running:
        
        if part == "a":
            outcome = random_num(100)
            
            if outcome == "outcome 2":
                ending_2(goodwill, score, done_quiz)
            else:
                ending_3(goodwill, score, done_quiz)
                        
        else:
            #displays background
            game_display.fill(black)
            
            #displays text
            text = render_text(uniform_instructions, font_file, white, 20)
            game_display.blit(text, (125, 560))
            
            #displays uniform images
            game_display.blit(uniform1, (160, 160))
            game_display.blit(uniform2, (450, 160))
            
            goodwill_meter(goodwill)

            game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)            
            game_button("Uniform 1", 163, 100, 220, 50, 2, 30, white, pink, "part 4", 18, white, goodwill, score, done_quiz)
            game_button("Uniform 2", 452, 100, 220, 50, 2, 30, white, pink, "part 4", 18, white, goodwill, score, done_quiz)        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()
        
        
        
        
def part_4(goodwill, score, done_quiz):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays other components
        dialogue_box()
        display_dialogue(part4_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 4.1", 18, white, goodwill, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()




def part_4_1(goodwill, score, done_quiz):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
        
        #displays other componenents        
        dialogue_box()
        display_dialogue(part4_line2)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Sing a song", 400, 215, 350, 40, 2, 30, black, pink, "part 5 a", 16, white, goodwill, score, done_quiz)
        game_button("Tap his shoulder gently", 400, 260, 350, 40, 2, 30, black, pink, "part 5 b", 16, white, goodwill, score, done_quiz)
        game_button("Ignore him", 400, 305, 350, 40, 2, 30, black, pink, "part 5 c", 16, white, goodwill, score, done_quiz)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()
        
        
        
def part_5(part, goodwill, score, done_quiz):
    running = True
    action = ""
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
          
        #displays hachiko sprite and other components              
        dialogue_box()
        goodwill_meter(goodwill)
        
        if part == "a":
            display_dialogue(part5a_line1)
            action = "part 5.1a"
            
        elif part == "b":
            display_dialogue(part5b_line1)
            action = "part 5.1b"
                    
        else:
            display_dialogue(part5c_line1)
            action = "part 5.1c"
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, action, 18, white, goodwill, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()

    
def part_5_1(part, goodwill, score, done_quiz):
    
    #calculates how much goodwill meter goes up or down
    filled_amount = goodwill
    
    if part == "a":
        outcome = random_num(16)
        if outcome == "outcome 1":    
            filled_amount += random.randint(1, 15)
        else:
            filled_amount -= random.randint(1, 15)
    
    elif part == "b":
        filled_amount -= random.randint(15, 30)
    
    else:
        outcome = random_num(36)
        if outcome == "outcome 1":    
            filled_amount += random.randint(8, 20)
        else:
            filled_amount -= random.randint(8, 20)    

    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
          
        goodwill_meter(filled_amount)
        
        if part == "a":
            if outcome == "outcome 1":
                game_display.blit(pj_king_happy, (100, 100))                
                dialogue_box()
                speaker_box("King")                
                display_dialogue(part5a_line2)
            else:
                game_display.blit(pj_king_angry, (100, 100))                
                dialogue_box()
                speaker_box("King")
                display_dialogue(part5a_line3)
        
        elif part == "b":
            game_display.blit(pj_king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part5b_line2)
        
        else:
            if outcome == "outcome 1":
                game_display.blit(pj_king_happy, (100, 100))                
                dialogue_box()
                speaker_box("King")                
                display_dialogue(part5c_line2)
                
            else:
                game_display.blit(pj_king_angry, (100, 100))
                dialogue_box()
                speaker_box("King")
                display_dialogue(part5c_line3)
                
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 350, 560, 150, 50, 2, 30, black, pink, "part 6", 18, white, filled_amount, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_6(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays narration         
        dialogue_box()
        display_dialogue(part6_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Stop and help", 400, 230, 350, 40, 2, 30, black, pink, "part 7 a", 16, white, goodwill, score, done_quiz)
        game_button("Continue walking", 400, 280, 350, 40, 2, 30, black, pink, "part 7 b", 16, white, goodwill, score, done_quiz)    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_7(part, goodwill, score, done_quiz):
    running = True
    action = ""
    
    filled_amount = goodwill
    if part == "a":
        filled_amount += random.randint(5, 10)
    
    else:
        filled_amount -= random.randint(5, 10)
    
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
                
        if part == "a":
            dialogue_box()
            display_dialogue(part7_line1)
            action = "part 7.1"
            
        else:
            dialogue_box()
            display_dialogue(part7_line3)
            action = "part 8.1 b"
        
        goodwill_meter(filled_amount)

        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 350, 570, 150, 50, 2, 30, black, pink, action, 18, white, filled_amount, score, done_quiz)            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_7_1(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        game_display.blit(hachiko_neutral, (100, 100))
        dialogue_box()
        speaker_box("Hachiko")
        display_dialogue(part7_line2)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Yes that would be lovely.", 400, 230, 350, 40, 2, 30, black, pink, "part 7.2", 16, white, goodwill, score, done_quiz)
        game_button("No, thank you.", 400, 280, 350, 40, 2, 30, black, pink, "part 8 b", 16, white, goodwill, score, done_quiz)   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()
        
        
        
def part_7_2(goodwill, score, done_quiz):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(story_bg, (0, 0))
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 300, 570, 150, 50, 2, 30, black, pink, "part 8 a", 20, white, goodwill, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update() 
    
    
    
def part_8(part, goodwill, score, done_quiz):
    running = True
    filled_amount = goodwill
    if part == "a":
        filled_amount += random.randint(1, 5)
    
    else:
        filled_amount -= random.randint(5, 10)
    
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0)) 
        
        if part == "a":
            game_display.blit(hachiko_neutral, (100, 100))
            dialogue_box()
            speaker_box("Hachiko")
            display_dialogue(part8_line1)

        else:
            game_display.blit(hachiko_angry, (100, 100))
            dialogue_box()
            speaker_box("Hachiko")
            display_dialogue(part8_line2)            
            
        goodwill_meter(filled_amount)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 350, 530, 100, 50, 2, 30, black, pink, "part 8.1 a", 18, white, filled_amount, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_8_1(part, goodwill, score, done_quiz):
    running = True
    action = ""
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        dialogue_box()
        
        if part == "a":
            display_dialogue(part8_line3)
            action = "part 9 a"
            
        else:
            display_dialogue(part8_line4)
            action = "part 9 b"
            
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 100, 570, 150, 50, 2, 30, black, pink, action, 20, white, goodwill, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()   



def part_9(part, goodwill, score, done_quiz):
    running = True
    
    filled_amount = goodwill
    if part == "a":
        filled_amount -= random.randint(5, 10)
        
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))        
        
        if part == "a":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part9_line1)
        
        else:
            game_display.blit(king_neutral, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part9_line2)
            
        goodwill_meter(filled_amount)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 10", 18, white, filled_amount, score, done_quiz)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_10(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        dialogue_box()
        display_dialogue(card_instructions)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        
        #displays cards and card buttons
        game_button("card 1", 50, 100, 200, 50, 3, 30, black, pink, "part 10.1a", 18, white, goodwill, score, done_quiz)
        game_button("card 2", 300, 100, 200, 50, 3, 30, black, pink, "part 10.1b", 18, white, goodwill, score, done_quiz)
        game_button("card 3", 550, 100, 200, 50, 3, 30, black, pink, "part 10.1c", 18, white, goodwill, score, done_quiz)
        
        game_display.blit(poisoned_card, (50, 175))
        game_display.blit(haunted_card, (300, 175))
        game_display.blit(jousting_card, (550, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                    
        pygame.display.update()



def part_10_1(part, goodwill, score, done_quiz):
    running = True
    
    filled_amount = goodwill
    if part == "a":
        filled_amount -= 10
    
    elif part == "b":
        filled_amount -= 15
    
    else:
        filled_amount += 10

    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        if part == "a":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line1)
        
        elif part == "b":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line2)
            
        else:
            game_display.blit(king_happy, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line3)
        
        goodwill_meter(filled_amount)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 10.2", 18, white, filled_amount, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()

def part_10_2(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
                
        dialogue_box()
        display_dialogue(card_instructions)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        
        game_button("card 1", 50, 100, 200, 50, 3, 30, black, pink, "part 10.3a", 18, white, goodwill, score, done_quiz)
        game_button("card 2", 300, 100, 200, 50, 3, 30, black, pink, "part 10.3b", 18, white, goodwill, score, done_quiz)
        game_button("card 3", 550, 100, 200, 50, 3, 30, black, pink, "part 10.3c", 18, white, goodwill, score, done_quiz)
        
        game_display.blit(mom_card, (50, 175))
        game_display.blit(kitchen_card, (300, 175))
        game_display.blit(murders_card, (550, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()
        
        
        
def part_10_3(part, goodwill, score, done_quiz):
    running = True
    
    filled_amount = goodwill
    if part == "a":
        filled_amount += 8
    
    elif part == "b":
        filled_amount -= 10
    
    else:
        filled_amount += 8

    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        if part == "a":
            game_display.blit(king_happy, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line4)
        
        elif part == "b":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line5)
            
        else:
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line6)
        
        goodwill_meter(filled_amount)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 10.4", 18, white, filled_amount, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_10_4(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        dialogue_box()
        display_dialogue(card_instructions)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        
        game_button("card 1", 50, 100, 200, 50, 3, 30, black, pink, "part 10.5a", 18, white, goodwill, score, done_quiz)
        game_button("card 2", 300, 100, 200, 50, 3, 30, black, pink, "part 10.5b", 18, white, goodwill, score, done_quiz)
        game_button("card 3", 550, 100, 200, 50, 3, 30, black, pink, "part 10.5c", 18, white, goodwill, score, done_quiz)
        
        game_display.blit(witch_card, (50, 175))
        game_display.blit(taxes_card, (300, 175))
        game_display.blit(painter_card, (550, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()
        
def part_10_5(part, goodwill, score, done_quiz):
    running = True
    
    filled_amount = goodwill
    if part == "a":
        filled_amount -= 8
    
    elif part == "b":
        filled_amount -= 10
    
    else:
        filled_amount += 8

    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        if part == "a":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line7)
        
        elif part == "b":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line8)
            
        else:
            game_display.blit(king_happy, (100, 100))
            dialogue_box()
            speaker_box("King")
            display_dialogue(part10_line9)
        
        goodwill_meter(filled_amount)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 11", 18, white, filled_amount, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()  
    
        pygame.display.update()



def part_11(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        game_display.blit(hachiko_neutral, (100, 100))
        dialogue_box()
        speaker_box("Hachiko")
        display_dialogue(part11_line1)
    
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 350, 550, 100, 50, 2, 30, black, pink, "part 11.1", 18, white, goodwill, score, done_quiz)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_11_1(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(dining_hall_bg, (0, 0))   
        
        dialogue_box()
        display_dialogue(riddle)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        
        game_button("pheasant", 50, 100, 200, 50, 3, 30, pink, white, "part 12 a", 18, black, goodwill, score, done_quiz)
        game_button("pickle", 300, 100, 200, 50, 3, 30, pink, white, "part 12 b", 18, black, goodwill, score, done_quiz)
        game_button("prosciutto", 550, 100, 200, 50, 3, 30, pink, white, "part 12 a", 18, black, goodwill, score, done_quiz)
                
        game_display.blit(pheasant, (50, 175))
        game_display.blit(pickle, (300, 175))
        game_display.blit(prosciutto, (550, 175))
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()
        
        
        
def part_12(part, goodwill, score, done_quiz):
    running = True
    
    filled_amount = goodwill
    if part == "a":
        filled_amount -= random.randint(10, 30)
    
    else:
        filled_amount += random.randint(10, 25)
    
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(dining_hall_bg, (0, 0))   
        
        if part == "a":
            game_display.blit(king_angry, (100, 100))
            dialogue_box
            display_dialogue(part12_line1)
            
        else:
            game_display.blit(king_happy, (100, 100))
            dialogue_box()
            display_dialogue(part12_line2)
            
        speaker_box("King")
        goodwill_meter(filled_amount)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 13", 18, white, filled_amount, score, done_quiz)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_13(goodwill, score, done_quiz):
    running = True
    
    #randomly chooses the correct answer
    action1 = "part 13.1a"
    action2 = "part 13.1a"
    action3 = "part 13.1a"
    correct_option = random.randint(1, 3)
    
    if correct_option == 1:
        action1 = "part 13.1b"
    elif correct_option == 2:
        action2 = "part 13.1b"
    else:
        action3 = "part 13.1b"
        
    while running:
        # displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))
        
        game_display.blit(king_neutral, (100, 100))
        dialogue_box()
        speaker_box("King")
        display_dialogue(part13_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        
        game_button("Watch a play", 400, 215, 350, 40, 2, 30, black, pink, action1, 16, white, goodwill, score, done_quiz)
        game_button("Go hunting", 400, 260, 350, 40, 2, 30, black, pink, action2, 16, white, goodwill, score, done_quiz)
        game_button("Take a nap", 400, 305, 350, 40, 2, 30, black, pink, action3, 16, white, goodwill, score, done_quiz)   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_13_1(part, goodwill, score, done_quiz):
    running = True
    
    filled_amount = goodwill
    if part == "a":
        filled_amount -= 10
    else:
        filled_amount += 10
        
    while running:    
        # displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))
        
        if part == "a":
            game_display.blit(king_angry, (100, 100))
            dialogue_box()
            display_dialogue(part13_line2)
            
        else:
            game_display.blit(king_happy, (100, 100))
            dialogue_box()
            display_dialogue(part13_line3)
            
        speaker_box("King")
        goodwill_meter(filled_amount)

        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 14", 18, white, filled_amount, score, done_quiz) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        pygame.display.update()



def part_14(goodwill, score, done_quiz):
    running = True
    action = ""
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        game_display.blit(hachiko_neutral, (100, 100))
        dialogue_box()
        speaker_box("Hachiko")
        display_dialogue(part14_line1)
        
        goodwill_meter(goodwill)
        
        #decides on ending based on goodwill value
        if goodwill < 50:
            action = "ending 4"
        else:
            action = "ending 5"
        
        game_button("Back", 50, 45, 120, 30, 2, 30, black, pink, "main menu", 16, white, 0, score, done_quiz)
        game_button("Next", 350, 550, 100, 50, 2, 30, black, pink, action, 18, white, goodwill, score, done_quiz) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def ending_1(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(rose_pot, (250, 100))
        
        dialogue_box()
        display_dialogue(ending1_line1)
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount, score, done_quiz)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()    



def ending_2(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(black)

        #displays image and other components
        game_display.blit(restaurant, (240, 100))
        
        dialogue_box()
        display_dialogue(ending2_line1)
        goodwill_meter(goodwill)

        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount, score, done_quiz) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()    



def ending_3(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(guillotine, (250, 80))
        
        dialogue_box()
        display_dialogue(ending3_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount, score, done_quiz) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()
        
        

def ending_4(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(guillotine, (250, 80))
                
        dialogue_box()
        display_dialogue(ending4_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount, score, done_quiz)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()    



def ending_5(goodwill, score, done_quiz):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(bed, (200, 100))
                
        dialogue_box()
        display_dialogue(ending5_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount, score, done_quiz)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()    
