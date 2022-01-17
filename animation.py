#imports and initializes modules
import pygame
pygame.init()
import random
from menu import

#declares and initializes variables for displaying the window
window_size = (800, 650)
game_display = pygame.display.set_mode(window_size)

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
part7_line4 = dialogues.readline()

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

citations = pygame.image.load("credits.png")

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
def game_button(msg, x, y, length, height, border, radius, border_colour, button_colour, action, font_size, font_colour, goodwill):
    
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
                g.curr_menu.display_menu()
                 
            if action == "part 1":
                part_1()
                
            if action == "part 2":
                part_2(goodwill)
            
            if action == "part 2.1":
                part_2_1(goodwill)
                
            if action == "part 3 a":
                part_3("a", goodwill)
           
            if action == "part 3 b":
                part_3("b", goodwill)
            
            if action == "part 4":
                part_4(goodwill)
            
            if action == "part 4.1":
                part_4_1(goodwill)
            
            if action == "part 5 a":
                part_5("a", goodwill)
                
            if action == "part 5 b":
                part_5("b", goodwill)
                
            if action == "part 5 c":
                part_5("c", goodwill)
            
            if action == "part 5.1a":
                part_5_1("a", goodwill)
                
            if action == "part 5.1b":
                part_5_1("b", goodwill)
                
            if action == "part 5.1c":
                part_5_1("c", goodwill)
                
            if action == "part 6":
                part_6(goodwill)
            
            if action == "part 7 a":
                part_7("a", goodwill)
            
            if action == "part 7 b":
                part_7("b", goodwill)
            
            if action == "part 7.1":
                part_7_1(goodwill)
            
            if action == "part 7.2":
                part_7_2(goodwill)
            
            if action == "part 7.3":
                part_7_3(goodwill)
            
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
            
            if action == "part 11.1":
                part_11_1(goodwill)
            
            if action == "part 12 a":
                part_12("a", goodwill)
                
            if action == "part 12 b":
                part_12("b", goodwill)
        
            if action == "part 13":
                part_13(goodwill)
            
            if action == "part 13.1a":
                part_13_1("a", goodwill)
            
            if action == "part 13.1b":
                part_13_1("b", goodwill)
                
            if action == "part 14":
                part_14(goodwill)
                
            if action == "ending 1":
                ending_1(goodwill)
            
            if action == "ending 2":
                ending_2(goodwill)
            
            if action == "ending 3":
                ending_3(goodwill)
            
            if action == "ending 4":
                ending_4(goodwill)
            
            if action == "ending 5":
                ending_5(goodwill)
            
      
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
        pygame.draw.rect(game_display, white, (x, y, (filled*2), height), border_radius = 30)
    
    #draws border
    pygame.draw.rect(game_display, pink, (x, y, length, height), width = 2, border_radius = 30)



#displays citations and exits the program
def quit_program():
    
    #displays citations
    game_display.blit(citations, (0, 0))
    
    #updates screen
    pygame.display.update()

    #displays credits for 10 seconds
    pygame.time.delay(10000)
    
    pygame.quit()
    quit()    


#code for the instructions section called animation for simplicity when being called in the main menu
def animation():
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(instructions_bg, (0, 0))
    
        game_button("Next", 300, 570, 150, 50, 2, 30, black, pink, "prologue", 20, white, 0)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()



#code for the prologue section
def prologue():
    running = True
    while running:
        #displays backgroudn
        game_display.fill(white)
        game_display.blit(prologue_bg, (0, 0))
       
        game_button("Next", 475, 570, 150, 50, 2, 30, black, pink, "part 1", 20, white, 0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
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
        game_button("Yes, I am.", 410, 230, 340, 40, 2, 30, black, pink, "part 2", 16, white, filled_amount)
        game_button("Sorry, I think you have the wrong person.", 410, 280, 340, 40, 2, 30, black, pink, "ending 1", 16, white, filled_amount)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()                                 
        
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
        display_dialogue(part2_line1)
        
        goodwill_meter(filled_amount)

        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 2.1", 18, white, filled_amount)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                           
        pygame.display.update()




def part_2_1(goodwill):
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
        game_button("Try to escape", 450, 230, 300, 40, 2, 30, black, pink, "part 3 a", 16, white, goodwill)
        game_button("Follow instructions", 450, 280, 300, 40, 2, 30, black, pink, "part 3 b", 16, white, goodwill)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
               
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
            #displays background
            game_display.fill(black)
            
            #displays text
            text = render_text(uniform_instructions, font_file, white, 20)
            game_display.blit(text, (125, 560))
            
            #displays uniform images
            game_display.blit(uniform1, (160, 160))
            game_display.blit(uniform2, (450, 160))
            
            goodwill_meter(goodwill)
            
            game_button("uniform 1", 163, 100, 220, 50, 2, 30, white, pink, "part 4", 18, white, goodwill)
            game_button("uniform 2", 452, 100, 220, 50, 2, 30, white, pink, "part 4", 18, white, goodwill)        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()
        
        
        
        
def part_4(goodwill):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        #displays other components
        dialogue_box()
        display_dialogue(part4_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 4.1", 18, white, goodwill)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()




def part_4_1(goodwill):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(bedroom_bg, (0, 0))
        
        #displays other componenents        
        dialogue_box()
        display_dialogue(part4_line2)
        
        goodwill_meter(goodwill)
        
        game_button("sing a song", 400, 215, 350, 40, 2, 30, black, pink, "part 5 a", 16, white, goodwill)
        game_button("tap his shoulder gently", 400, 260, 350, 40, 2, 30, black, pink, "part 5 b", 16, white, goodwill)
        game_button("ignore him", 400, 305, 350, 40, 2, 30, black, pink, "part 5 c", 16, white, goodwill)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()
        
        
        
def part_5(part, goodwill):
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
                
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, action, 18, white, goodwill)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
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
        #displays background
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
                
        game_button("Next", 350, 560, 150, 50, 2, 30, black, pink, "part 6", 18, white, filled_amount)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
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
        
        game_button("Stop and help", 400, 230, 350, 40, 2, 30, black, pink, "part 7 a", 16, white, goodwill)
        game_button("Continue walking", 400, 280, 350, 40, 2, 30, black, pink, "part 7 b", 16, white, goodwill)    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_7(part, goodwill):
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
            action = "part 9 b"
        
        goodwill_meter(filled_amount)

        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, action, 18, white, filled_amount)            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()

def part_7_1(goodwill):
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
        
        game_button("Yes that would be lovely.", 400, 230, 350, 40, 2, 30, black, pink, "part 7.2", 16, white, goodwill)
        game_button("No, thank you.", 400, 280, 350, 40, 2, 30, black, pink, "part 8 b", 16, white, goodwill)   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()
        
        
        
def part_7_2(goodwill):
    running = True
    while running:
        
        #displays background
        game_display.fill(white)
        game_display.blit(story_bg, (0, 0))
        
        game_button("Next", 300, 570, 150, 50, 2, 30, black, pink, "part 7.3", 20, white, goodwill)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_7_3(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        dialogue_box()
        display_dialogue(part7_line4)
        
        goodwill_meter(goodwill)
        
        button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 8 a", 20, white, goodwill)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
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
            
        goodwill_meter(filled_amount)
        
        game_button("next", 350, 530, 100, 50, 2, 30, black, pink, "part 9 a", 18, white, filled_amount)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
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
        
        button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 10", 18, white, filled_amount)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_10(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        dialogue_box()
        display_dialogue(card_instructions)
        
        goodwill_meter(goodwill)
        
        #displays cards and card buttons
        game_button("card 1", 50, 100, 200, 50, 3, 30, black, pink, "part 10.1a", 18, white, goodwill)
        game_button("card 2", 300, 100, 200, 50, 3, 30, black, pink, "part 10.1b", 18, white, goodwill)
        game_button("card 3", 550, 100, 200, 50, 3, 30, black, pink, "part 10.1c", 18, white, goodwill)
        
        game_display.blit(poisoned_card, (50, 175))
        game_display.blit(haunted_card, (300, 175))
        game_display.blit(jousting_card, (550, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                    
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
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 10.2", 18, white, filled_amount)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()

def part_10_2(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
                
        dialogue_box()
        display_dialogue(card_instructions)
        
        goodwill_meter(goodwill)
        
        game_button("card 1", 50, 100, 200, 50, 3, 30, black, pink, "part 10.3a", 18, white, goodwill)
        game_button("card 2", 300, 100, 200, 50, 3, 30, black, pink, "part 10.3b", 18, white, goodwill)
        game_button("card 3", 550, 100, 200, 50, 3, 30, black, pink, "part 10.3c", 18, white, goodwill)
        
        game_display.blit(mom_card, (50, 175))
        game_display.blit(kitchen_card, (300, 175))
        game_display.blit(murders_card, (550, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
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
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 10.4", 18, white, filled_amount)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_10_4(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(throne_room_bg, (0, 0))   
        
        dialogue_box()
        display_dialogue(card_instructions)
        
        goodwill_meter(goodwill)
        
        game_button("card 1", 50, 100, 200, 50, 3, 30, black, pink, "part 10.5a", 18, white, goodwill)
        game_button("card 2", 300, 100, 200, 50, 3, 30, black, pink, "part 10.5b", 18, white, goodwill)
        game_button("card 3", 550, 100, 200, 50, 3, 30, black, pink, "part 10.5c", 18, white, goodwill)
        
        game_display.blit(witch_card, (50, 175))
        game_display.blit(taxes_card, (300, 175))
        game_display.blit(painter_card, (550, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
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
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 11", 18, white, filled_amount)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()  
    
        pygame.display.update()

def part_11(goodwill):
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
        
        game_button("Next", 350, 550, 100, 50, 2, 30, black, pink, "part 11.1", 18, white, goodwill)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_11_1(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(white)
        game_display.blit(dining_hall_bg, (0, 0))   
        
        dialogue_box()
        display_dialogue(riddle)
        
        goodwill_meter(goodwill)
        
        game_button("pheasant", 50, 100, 200, 50, 3, 30, pink, white, "part 12 a", 18, black, goodwill)
        game_button("pickle", 300, 100, 200, 50, 3, 30, pink, white, "part 12 b", 18, black, goodwill)
        game_button("prosciutto", 550, 100, 200, 50, 3, 30, pink, white, "part 12 a", 18, black, goodwill)
                
        game_display.blit(pheasant, (50, 175))
        game_display.blit(pickle, (300, 175))
        game_display.blit(prosciutto, (550, 175))
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()
        
        
        
def part_12(part, goodwill):
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
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 13", 18, white, filled_amount)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_13(goodwill):
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
        
        game_button("Watch a play", 400, 215, 350, 40, 2, 30, black, pink, action1, 16, white, goodwill)
        game_button("Go hunting", 400, 260, 350, 40, 2, 30, black, pink, action2, 16, white, goodwill)
        game_button("Take a nap", 400, 305, 350, 40, 2, 30, black, pink, action3, 16, white, goodwill)   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def part_13_1(part, goodwill):
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

        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "part 14", 18, white, filled_amount)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        pygame.display.update()

def part_14(goodwill):
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
        
        game_button("Next", 350, 550, 100, 50, 2, 30, black, pink, action, 18, white, goodwill) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()



def ending_1(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(rose_pot, (250, 100))
        
        dialogue_box()
        display_dialogue(ending1_line1)
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()    



def ending_2(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(black)

        #displays image and other components
        game_display.blit(restaurant, (240, 100))
        
        dialogue_box()
        display_dialogue(ending2_line1)
        goodwill_meter(goodwill)

        button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()    



def ending_3(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(guillotine, (250, 80))
        
        dialogue_box()
        display_dialogue(ending3_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()
        
        

def ending_4(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(guillotine, (250, 80))
                
        dialogue_box()
        display_dialogue(ending4_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
        
        pygame.display.update()    



def ending_5(goodwill):
    running = True
    while running:
        #displays background
        game_display.fill(black)
        
        #displays image and other components
        game_display.blit(bed, (200, 100))
                
        dialogue_box()
        display_dialogue(ending5_line1)
        
        goodwill_meter(goodwill)
        
        game_button("Next", 550, 570, 150, 50, 2, 30, black, pink, "main menu", 18, white, filled_amount)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_program()
                
        pygame.display.update()    



        
instructions()