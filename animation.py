#imports and initializes modules
import pygame
pygame.init()
import random


#declares and initializes variables for displaying the window
window_size = (800, 650)
game_display = pygame.display.set_mode(window_size)


#loads images
instructions_bg = pygame.image.load("instructions.png")

#defines some colours
white = (255, 255, 255)
black = (0, 0, 0)

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
def button(msg, x, y, length, height, border, border_colour, button_colour, action, font_size, font_colour):
    
    #draws button
    pygame.draw.rect(game_display, button_colour, (x, y, length, height), width = 0, border_radius = 30)
    
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #if the mouse is hovering on the button draw a border 
    if x + length > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_display, border_colour, (x, y, length, height), width = border, border_radius = 30)
        if click[0] == 1:
            if action == "prologue":
                prologue()
                
            if action == "part 1":
                part_1()
                
            if action == "part 2":
                part_2()
           
            if action == "part 3 a":
                part_3("a")
           
            if action == "part 3 b":
                part_3("b")
            
            if action == "part 4":
                part_4()
            
            if action == "part 5 a":
                part_5("a")
                
            if action == "part 5 b":
                part_5("b")
                
            if action == "part 5 c":
                part_5("c")
                
            if action == "part 6":
                part_6()
            
            if action == "part 7 a":
                part_7("a")
            
            if action == "part 7 b":
                part_7("b")
            
            if action == "part 8 a":
                part_8("a")
            
            if action == "part 8 b":
                part_8("b")
            
            if action == "part 9":
                part_9()
            
            if action == "part 10":
                part_10()
            
            if action == "part 11":
                part_11()
            
            if action == "part 12 a":
                part_12("a")
                
            if action == "part 12 b":
                part_12("b")
                
            if action == "part 12 c":
                part_12("c")
                
            if action == "part 12 d":
                part_12("d")
                
            if action == "ending 1":
                ending_1()
            
            if action == "ending 2":
                ending_2()
            
            if action == "ending 3":
                ending_3()
            
  
    #draws text on button    
    text = render_text(msg, font_file, font_colour, font_size)
    #Centers the text on the button
    text_pos = text_rect(text)
    text_pos.center = ( (x + (length/2)), (y + (height/2)))
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
    box_x = 50
    box_y = 400
    box_length = 700
    box_height = 200
    
    pygame.draw.rect(game_display, (239, 222, 205), (box_x, box_y, box_length, box_height), border_radius = 30)
    pygame.draw.rect(game_display, (255, 0, 85), (box_x, box_y, box_length, box_height), width = 3, border_radius = 30)
    
#defines instructions section
def instructions():
    running = True
    while running:
        
        #blit background
        game_display.blit(instructions_bg, (0, 0))
        
        button("next", 350, 570, 100, 75, 1, (255, 255, 255), (0, 0, 255), "prologue", 20, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

#defines prologue section
def prologue():
    running = True
    while running:
        game_display.fill(black)
        text = render_text("prologue", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        
       
        button("next", 675, 300, 100, 75, 1, (255, 255, 255), (0, 0, 255), "part 1", 20, black)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()

def part_1():
    running = True
    while running:
        game_display.fill(black)
        dialogue_box()
        text = render_text("part 1", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        

        button("yes", 400, 500, 100, 75, 1, white, (0, 0, 255), "part 2", 20, black)
        button("no", 300, 500, 100, 75, 1, white, (0, 0, 255), "ending 1", 20, black)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
    
def part_2():
    running = True
    while running:
        game_display.fill(black)
        text = render_text("part 2", font_file, white, font_size)
        game_display.blit(text, (50, 50))
        

        button("escape", 500, 500, 100, 75, 1, white, (0, 0, 255), "part 3 a", 20, black)
        button("obedience", 200, 500, 100, 75, 1, white, (0, 0, 255), "part 3 b", 20, black)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()


def part_3(part):
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
        
def part_4():
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
def part_5(part):
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


def part_6():
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

def part_7(part):
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


def part_8(part):
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

def part_9():
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


def part_10():
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

def part_11():
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

def part_12(part):
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


def part_13():
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

def part_14():
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


def ending_1():
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


def ending_2():
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


def ending_3():
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