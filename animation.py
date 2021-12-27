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

#loads images
instructions_bg = pygame.image.load("instructions.png")
prologue_bg = pygame.image.load("prologue.png")
hallway_bg = pygame.image.load("hallway4.jpg")
hallway_bg = pygame.transform.scale(hallway_bg, window_size)
hachiko_neutral = pygame.image.load("hachiko.png")
hachiko_neutral = pygame.transform.scale(hachiko_neutral, (280, 372))

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
def button(msg, x, y, length, height, border, border_colour, button_colour, action, font_size, font_colour, goodwill):
    
    #draws button
    pygame.draw.rect(game_display, button_colour, (x, y, length, height), width = 0, border_radius = 30)
    
    #defines some variables related to the mouse
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #if the mouse is hovering on the button draw a border 
    if x + length > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_display, border_colour, (x, y, length, height), width = border, border_radius = 30)
        
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
            
            if action == "part 9":
                part_9(goodwill)
            
            if action == "part 10":
                part_10(goodwill)
            
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
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))

        game_display.blit(hachiko_neutral, (100, 100))
        dialogue_box()
        speaker_box("Hachiko")
        
        goodwill_meter(filled_amount)
        
        display_dialogue(part1_line)
        
        mouse_pos = pygame.mouse.get_pos()
        
        button("Yes, I am.", 75, 570, 200, 50, 2, black, pink, "part 2", 18, white, filled_amount)
        button("Sorry, I think you have the wrong person.", 315, 570, 375, 50, 2, black, pink, "ending 1", 18, white, filled_amount)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                                        
                                    
        
        pygame.display.update()
    
def part_2(goodwill):
    running = True
    filled_amount = goodwill 
    filled_amount += random.randint(1, 5)
    
    while running:
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        
        game_display.blit(hachiko_neutral, (100, 100))
        dialogue_box()
        speaker_box("You")
        display_dialogue(part2_line1)
        goodwill_meter(filled_amount)
        
        if pygame.mouse.get_pressed() == (1, 0, 0):
            
            part_2_1(goodwill)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()

def part_2_1(goodwill):
    running = True
    while running:
        game_display.fill(white)
        game_display.blit(hallway_bg, (0, 0))
        

        game_display.blit(hachiko_neutral, (100, 100))                
        dialogue_box()
        speaker_box("Hachiko")
        display_dialogue(part2_line2)
        
        button("escape", 500, 500, 100, 75, 1, white, (0, 0, 255), "part 3 a", 20, black, goodwill)
        button("obedience", 200, 500, 100, 75, 1, white, (0, 0, 255), "part 3 b", 20, black, goodwill)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        
def part_3(part, goodwill):
    running = True
    while running:
        if part == "a":
            game_display.fill(black)
            text = render_text("part 3a", font_file, white, font_size)
            game_display.blit(text, (50, 50))
            
            outcome = random_num(100)
            if outcome == "outcome 2":
                ending_2()
            else:
                ending_3()
                        
        else:
            game_display.fill(black)
            text = render_text("part 3b", font_file, white, font_size)
            game_display.blit(text, (50, 50))
            
            button("maid", 450, 200, 100, 250, 1, white, (0, 0, 255), "part 4", 20, black)
            button("butler", 250, 200, 100, 250, 1, white, (0, 0, 255), "part 4", 20, black)        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        
def part_4(goodwill):
    running = True
    while running:
        game_display.fill(black)
        text = render_text("part 4", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("sing", 500, 500, 100, 75, 1, white, (0, 0, 255), "part 5 a", 20, black)
        button("tap", 200, 500, 100, 75, 1, white, (0, 0, 255), "part 5 b", 20, black)
        button("ignore", 350, 500, 100, 75, 1, white, (0, 0, 255), "part 5 c", 20, black)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()

#defines instructions section
def part_5(part, goodwill):
    running = True
    while running:
        
        game_display.fill(black)
        
        text = render_text("part 5", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 6", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def part_6(goodwill):
    running = True
    while running:
        
        game_display.fill(black)
        
        text = render_text("part 6", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("help", 500, 500, 100, 75, 1, white, (0, 0, 255), "part 7 a", 20, black)
        button("walk away", 200, 500, 100, 75, 1, white, (0, 0, 255), "part 7 b", 20, black)    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_7(part, goodwill):
    running = True
    while running:
        if part == "a":
            game_display.fill(black)
            text = render_text("part 7a", font_file, white, font_size)
            game_display.blit(text, (50, 50))
            
    
            button("yes", 400, 500, 100, 75, 1, white, (0, 0, 255), "part 8 a", 20, black)
            button("no", 300, 500, 100, 75, 1, white, (0, 0, 255), "part 8 b", 20, black)   
            
        else:
            game_display.fill(black)
            
            text = render_text("part 7b", font_file, white, font_size)
            game_display.blit(text, (50, 50))
            
            button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 9", 20, black)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()


def part_8(part, goodwill):
    running = True
    while running:
        if part == "a":
            game_display.fill(black)
            
            text = render_text("part 8", font_file, white, font_size)
            game_display.blit(text, (50, 50))
            
            button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 9", 20, black)
        
        else:
            game_display.fill(black)
            
            text = render_text("part 8b", font_file, white, font_size)
            game_display.blit(text, (50, 50))
            
            button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 9", 20, black)            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_9(goodwill):
    running = True
    while running:
        game_display.fill(black)
        text = render_text("part 9", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
       
        button("next", 675, 300, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 10", 20, black)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()


def part_10(goodwill):
    running = True
    while running:
        
        game_display.fill(black)
        
        text = render_text("part 10", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 11", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def part_11(goodwill):
    running = True
    while running:
        action = ""
        score = int(1)
        game_display.fill(black)
        
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
            
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), action, 20, black)
        
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
        
       
        button("next", 675, 500, 100, 75, 1, (255, 255, 255), (0, 0, 255), "main menu", 20, black)

        
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

instructions()
