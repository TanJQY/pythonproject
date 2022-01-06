#imports and initializes modules
import pygame
pygame.init()
import random


#declares and initializes variables for displaying the window
window_size = (800, 650)
game_display = pygame.display.set_mode(window_size)

#declares variables for text and opens text file
dialogues = open("dialogues.txt","r")
part1_line = dialogues.readline()

part2_line1 = dialogues.readline()
part2_line2 = dialogues.readline()

part3_line1 = dialogues.readline()

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

riddle = dialogues.readline()

#loads images
instructions_bg = pygame.image.load("instructions.png")
prologue_bg = pygame.image.load("prologue.png")
hallway_bg = pygame.image.load("hallway4.jpg")
hallway_bg = pygame.transform.scale(hallway_bg, window_size)
bedroom_bg = pygame.image.load("bedroom.jpg")
bedroom_bg = pygame.transform.scale(bedroom_bg, window_size)
throne_room_bg = pygame.image.load("throne room.jpg")
throne_room_bg = pygame.transform.scale(throne_room_bg, window_size)

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

#defines some colours
white = (255, 255, 255)
black = (0, 0, 0)
off_white = (239, 222, 205)
pink = (255, 0, 85)
darker_pink = (255, 0, 50)

#defines some variables for displaying dialogue
dialogue_box_x = 50
dialogue_box_y = 445
dialogue_box_length = 700
dialogue_box_height = 200

#defines variables used for goodwill meter
filled_amount = int(50)

#defines some variables for displaying text
font_file = "PlayfairDisplayRegular.ttf"
font_size = 24

#function to render text
def render_text(text, font_file, font_colour, font_size):
    font = pygame.font.Font(font_file, font_size)   
    text = font.render(text, True, font_colour)
    return text

#function that gets text rectangle for positioning purposes
def text_rect(text):
    text_rect = text.get_rect()
    return text_rect



#draws buttons, directs user to different sections depending on the button pressed
#goodwill paramater needed to pass on information about the goodwill meter from part to part
def button(msg, x, y, length, height, border, radius, border_colour, button_colour, action, font_size, font_colour, goodwill):
    
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
            if action == "part 1":
                part_1()
                
            if action == "part 2":
                part_2(goodwill)
           
            if action == "part 3 a":
                part_3("a", goodwill)
           
            if action == "part 3 b":
                part_3("b", goodwill)
            
            if action == "part 4":
                part_4(goodwill)
            
            if action == "part 5 a":
                part_5("a", goodwill)
                
            if action == "part 5 b":
                part_5("b", goodwill)
                
            if action == "part 5 c":
                part_5("c", goodwill)
                
            if action == "part 6":
                part_6(goodwill)
            
            if action == "part 7 a":
                part_7("a", goodwill)
            
            if action == "part 7 b":
                part_7("b", goodwill)
            
            if action == "part 8 a":
                part_8("a", goodwill)
            
            if action == "part 8 b":
                part_8("b", goodwill)
            
            if action == "part 9 a":
                part_9("a", goodwill)
           
            if action == "part 9 b":
                part_9("b", goodwill)
            
            if action == "part 10":
                part_10(goodwill)
            
            if action == "part 10.1a":
                part_10_1("a", goodwill)
            
            if action == "part 10.1b":
                part_10_1("b", goodwill)
            
            if action == "part 10.1c":
                part_10_1("c", goodwill)
            
            if action == "part 10.2":
                part_10_2(goodwill)
            
            if action == "part 10.3a":
                part_10_3("a", goodwill)
            
            if action == "part 10.3b":
                part_10_3("b", goodwill)
            
            if action == "part 10.3c":
                part_10_3("c", goodwill)
            
            if action == "part 10.4":
                part_10_4(goodwill)
            
            if action == "part 10.5a":
                part_10_5("a", goodwill)
            
            if action == "part 10.5b":
                part_10_5("b", goodwill)
            
            if action == "part 10.5c":
                part_10_5("c", goodwill)
                
            if action == "part 11":
                part_11(goodwill)
            
            if action == "part 12 a":
                part_12("a", goodwill)
                
            if action == "part 12 b":
                part_12("b", goodwill)
                
            if action == "part 12 c":
                part_12("c", goodwill)
                
            if action == "part 12 d":
                part_12("d", goodwill)
            
            if action == "part 13":
                part_13(goodwill)
            
            if action == "part 14":
                part_14(goodwill)
                
            if action == "ending 1":
                ending_1(goodwill)
            
            if action == "ending 2":
                ending_2(goodwill)
            
            if action == "ending 3":
                ending_3(goodwill)
            
      
    #renders text
    text = render_text(msg, font_file, font_colour, font_size)
    
    #centers the text on the button
    text_pos = text_rect(text)
    text_pos.center = ( (x + (length/2)), (y + (height/2)))
    
    #blits text on the button
    game_display.blit(text, text_pos)




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
    pygame.draw.rect(game_display, off_white, (dialogue_box_x, dialogue_box_y, dialogue_box_length, dialogue_box_height), border_radius = 30)
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
    if who == "You":
        length = 75
    if who == "King":
        length = 100
    
    #draws rectangle and border
    pygame.draw.rect(game_display, off_white, (x, y, length, height), border_radius = 12)
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
    
    #displays text
    text = "Goodwill: " + str(filled)
    text = render_text(text, font_file, white, 18)
    game_display.blit(text, (text_x, text_y))    
    
    #draws goodwill meter
    pygame.draw.rect(game_display, black, (x, y, length, height), border_radius = 30)    
    #draws filled portion
    #filled portion is mutliplied by 2 since 1% of the bar is 2 pixels
    pygame.draw.rect(game_display, white, (x, y, (filled*2), height), border_radius = 30)
    #draws border
    pygame.draw.rect(game_display, pink, (x, y, length, height), width = 2, border_radius = 30)


#code for the instructions section
def instructions():
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(instructions_bg, (0, 0))
        
        #displays some text
        text = render_text("click anywhere to continue", font_file, black, 24)
        game_display.blit(text, (250, 575))
        
        
        #button("next", 325, 570, 150, 50, 2, pink, off_white, "prologue", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if pygame.mouse.get_pressed() == (1, 0, 0):
                prologue()
        
        pygame.display.update()

#code for the prologue section
def prologue():
    running = True
    while running:
        game_display.fill(white)
        game_display.blit(prologue_bg, (0, 0))
       
        #button("next", 425, 400, 150, 50, 2, pink, off_white, "part 1", 20, black)
        text = render_text("click anywhere to continue", font_file, black, 24)
        game_display.blit(text, (370, 575))        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                part_1()            
        
        pygame.display.update()

def part_1():
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
        button("Yes, I am.", 100, 530, 600, 40, 2, 30, black, pink, "part 2", 18, white, filled_amount)
        button("Sorry, I think you have the wrong person.", 100, 575, 600, 40, 2, 30, black, pink, "ending 1", 18, white, filled_amount)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                                    
        
        pygame.display.update()
    
def part_2(goodwill):
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
        speaker_box("You")
        display_dialogue(part2_line1)
        goodwill_meter(filled_amount)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        if pygame.mouse.get_pressed() == (1, 0, 0):            
            part_2_1(filled_amount)        
        
        pygame.display.update()

def part_2_1(goodwill):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays hachiko sprite and other components
        game_display.blit(hachiko_neutral, (100, 100))                
        dialogue_box()
        speaker_box("Hachiko")
        display_dialogue(part2_line2)
        
        goodwill_meter(goodwill)
        
        #draws buttons
        button("Try to escape", 100, 545, 600, 40, 2, 30, black, pink, "part 3 a", 18, white, filled_amount)
        button("Follow instructions", 100, 590, 600, 40, 2, 30, black, pink, "part 3 b", 18, white, filled_amount)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        
def part_3(part, goodwill):
    running = True
    while running:
        
        if part == "a":
            outcome = random_num(100)
            if outcome == "outcome 2":
                ending_2(goodwill)
            else:
                ending_3(goodwill)
                        
        else:
            game_display.fill(black)
            text = render_text("Pick a uniform", font_file, white, 20)
            game_display.blit(text, (50, 50))
            
            button("maid", 450, 200, 250, 250, 2, 30, white, white, "part 4", 20, black, goodwill)
            button("butler", 100, 200, 250, 250, 2, 30, white, white, "part 4", 20, black, goodwill)        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        
def part_4(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
        
        #displays narration         
        dialogue_box()
        display_dialogue(part3_line1)
        
        goodwill_meter(goodwill)
        
        button("sing a song", 100, 525, 600, 30, 2, 30, black, pink, "part 5 a", 16, white, goodwill)
        button("tap his shoulder gently", 100, 560, 600, 30, 2, 30, black, pink, "part 5 b", 16, white, goodwill)
        button("ignore him", 100, 595, 600, 30, 2, 30, black, pink, "part 5 c", 16, white, goodwill)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        
        
def part_5(part, goodwill):
    running = True
    while running:
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
          
        #displays hachiko sprite and other components              
        dialogue_box()
        goodwill_meter(filled_amount)
        
        if part == "a":
            display_dialogue(part5a_line1)
        
        elif part == "b":
            display_dialogue(part5b_line1)
        
        else:
            display_dialogue(part5c_line1)
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                part_5_1(part, goodwill)
        pygame.display.update()

    
def part_5_1(part, goodwill):
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
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
          
        goodwill_meter(filled_amount)
        

        if part == "a":
            if outcome == "outcome 1":
                print("good")
                game_display.blit(pj_king_happy, (100, 100))                
                dialogue_box()
                speaker_box("King")                
                display_dialogue(part5a_line2)
            else:
                print("bad")
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
                
        button("next", 350, 550, 100, 50, 2, 30, black, pink, "part 6", 18, white, filled_amount)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def part_6(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays narration         
        dialogue_box()
        display_dialogue(part6_line1)
        
        goodwill_meter(goodwill)
        
        button("Stop and help", 100, 540, 600, 40, 2, 30, black, pink, "part 7 a", 18, white, goodwill)
        button("Continue walking", 100, 585, 600, 40, 2, 30, black, pink, "part 7 b", 18, white, goodwill)    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_7(part, goodwill):
    running = True
    filled_amount = goodwill
    filled_amount -= random.randint(5, 10)
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
                
        if part == "a":
            dialogue_box()
            display_dialogue(part7_line1)
                                
        else:
            dialogue_box()
            display_dialogue(part7_line3)
            goodwill_meter(filled_amount)
            button("next", 350, 500, 100, 50, 2, 30, black, pink, "part 9 b", 18, white, filled_amount)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if pygame.mouse.get_pressed() == (1, 0, 0) and part == "a":            
                part_7_1(goodwill)
        
        pygame.display.update()

def part_7_1(goodwill):
    running = True
    
    filled_amount = goodwill
    filled_amount += random.randint(10, 20)    
    
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        game_display.blit(hachiko_neutral, (100, 100))
        dialogue_box()
        speaker_box("Hachiko")
        display_dialogue(part7_line2)
        
        button("Yes that would be lovely.", 100, 530, 600, 40, 2, 30, black, pink, "part 8 a", 18, white, filled_amount)
        button("No, thank you.", 100, 575, 600, 40, 2, 30, black, pink, "part 8 b", 18, white, filled_amount)   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        pygame.display.update()
        
def part_8(part, goodwill):
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
            
        button("next", 350, 530, 100, 50, 2, 30, black, pink, "part 9 a", 18, white, filled_amount)
        
        goodwill_meter(filled_amount)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_9(part, goodwill):
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
        button("next", 350, 530, 100, 50, 2, 30, black, pink, "part 10", 18, white, filled_amount)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()


def part_10(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        pygame.draw.rect(game_display, white, (300, 30, 200, 75), width = 0, border_radius = 20)        
        text = render_text("Pick a card", font_file, black, font_size)
        game_display.blit(text, (340, 50))
        
        button("card 1", 50, 160, 200, 400, 3, 0, black, white, "part 10.1a", 18, black, goodwill)
        button("card 2", 300, 160, 200, 400, 3, 0, black, white, "part 10.1b", 18, black, goodwill)
        button("card 3", 550, 160, 200, 400, 3, 0, black, white, "part 10.1c", 18, black, goodwill)
        
        button("next", 675, 500, 100, 75, 1, 30, (255, 255, 255), (0, 0, 255), "part 11", 20, black, goodwill)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        pygame.display.update()


def part_10_1(part, goodwill):
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
        button("next", 350, 550, 100, 50, 2, 30, black, pink, "part 10.2", 18, white, filled_amount)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    
        pygame.display.update()

def part_10_2(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        pygame.draw.rect(game_display, white, (300, 30, 200, 75), width = 0, border_radius = 20)        
        text = render_text("Pick a card", font_file, black, font_size)
        game_display.blit(text, (340, 50))
        
        button("card 1", 50, 160, 200, 400, 3, 0, black, white, "part 10.3a", 18, black, goodwill)
        button("card 2", 300, 160, 200, 400, 3, 0, black, white, "part 10.3b", 18, black, goodwill)
        button("card 3", 550, 160, 200, 400, 3, 0, black, white, "part 10.3c", 18, black, goodwill)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        pygame.display.update()
        
def part_10_3(part, goodwill):
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
        button("next", 350, 550, 100, 50, 2, 30, black, pink, "part 10.4", 18, white, filled_amount)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    
        pygame.display.update()

def part_10_4(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        pygame.draw.rect(game_display, white, (300, 30, 200, 75), width = 0, border_radius = 20)        
        text = render_text("Pick a card", font_file, black, font_size)
        game_display.blit(text, (340, 50))
        
        button("card 1", 50, 160, 200, 400, 3, 0, black, white, "part 10.5a", 18, black, goodwill)
        button("card 2", 300, 160, 200, 400, 3, 0, black, white, "part 10.5b", 18, black, goodwill)
        button("card 3", 550, 160, 200, 400, 3, 0, black, white, "part 10.5c", 18, black, goodwill)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        pygame.display.update()
        
def part_10_5(part, goodwill):
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
        button("next", 350, 550, 100, 50, 2, 30, black, pink, "part 11", 18, white, filled_amount)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    
        pygame.display.update()

def part_11(goodwill):
    running = True
    action = ""
    score = int(0)    
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        text = render_text("part 11", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        if score == 0:
            action = "part 12 a"
        elif score == 1:
            action = "part 12 b"
        elif score == 2:
            action = "part 12 c"
        else:
            action = "part 12 d"
            
        button("next", 675, 500, 100, 75, 1, 30, black, pink, action, 18, white, goodwill)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_12(part, goodwill):
    running = True
    while running:
        
        game_display.fill(black)
        
        text = render_text("part 12", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("next", 675, 300, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 13", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def part_13(goodwill):
    running = True
    while running:
        
        game_display.fill(black)
        
        text = render_text("part 13", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 14", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_14(goodwill):
    running = True
    while running:
        
        game_display.fill(black)
        
        text = render_text("part 14", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("next", 675, 300, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 13", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def ending_1(goodwill):
    running = True
    while running:
        game_display.fill(black)
        text = render_text("ending 1", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
       
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "main menu", 20, black, filled_amount)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()    


def ending_2(goodwill):
    running = True
    while running:
        game_display.fill(black)
        text = render_text("ending 2", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
       
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "main menu", 20, black)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()    


def ending_3(goodwill):
    running = True
    while running:
        game_display.fill(black)
        text = render_text("ending 3", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
       
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "main menu", 20, black)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()    

part_9("a", 50)
