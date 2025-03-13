import pygame
import pygame_gui
import sys
import time
import dot
import random

#------------------------------------ACHTUNG! WARNING! VAROITUS!-----------------------------------------------
#Currently has a memoryleak due to maybe not deinitializing dot objects that were made from previous iteration(s).
#13.3 Fixed issue of memleaks
#--------------------------------------------------------------------------------------------------------------

pygame.init()



pygame.display.set_caption("Circles")

window_height = 600
window_width = 1200

screen = pygame.display.set_mode((window_width,window_height))
window_surface = pygame.Surface((window_width,window_height))
manager = pygame_gui.UIManager((window_width, window_height))

is_running = True
windowHeight = screen.get_height()
windowWidth = screen.get_width()
center = (windowWidth / 2), (windowHeight / 2)

fps = 60
clock = pygame.time.Clock()
dotti = dot.Dot(screen, center, "red", 1, 20)



dottilista = []

def randomColor():
    return((random.randint(0,255), random.randint(0,255), random.randint(0, 255)))

#Default Values

randomDistanceMin = 10
randomDistanceMax = 20
randomPaddingMin = 10
randomPaddingMax = 20

#@profile
def GenerateDots():
    tempX = 0
    tempY = 0
    
    #padding = dotti.distance

    #---------------------DrawingVariables-------------------------------
    global randomDistanceMin
    global randomDistanceMax
    global randomPaddingMin
    global randomPaddingMax
    #--------------------------------------------------------------------
    
    padding = random.randint(randomPaddingMin, randomPaddingMax)
    
    #adding = random.randint(1, 100)
    
    amountToDrawX = int(screen.get_width() / (padding * 2))
    amountToDrawY = int(screen.get_height() / (padding * 2))
    
    randomColor1 = randomColor()
    randomDistance1 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor2 = randomColor()    
    randomDistance2 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor3 = randomColor()  
    randomDistance3 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor4 = randomColor()  
    randomDistance4 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor5 = randomColor()  
    randomDistance5 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor6 = randomColor()  
    randomDistance6 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor7 = randomColor()  
    randomDistance7 = random.randint(randomDistanceMin, randomDistanceMax)

    randomColor8 = randomColor()  
    randomDistance8 = random.randint(randomDistanceMin, randomDistanceMax)
    #-------------------------------------------------------------
    for j in range(amountToDrawY):
        for i in range(amountToDrawX):            
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor1, 1, randomDistance1))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor2, 1, randomDistance2))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor3, 1, randomDistance3))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor4, 1, randomDistance4))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor5, 1, randomDistance5))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor6, 1, randomDistance6))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor7, 1, randomDistance7))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor8, 1, randomDistance8))
            dottilista.append(dot.Dot(screen, (tempX + padding + dotti.radius, tempY + padding + dotti.radius), randomColor8, 1, randomDistance8))
            tempX += padding * 2
        tempX = 0
        tempY += padding * 2

  

#buttons / sliders
generate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 275), (100, 50)), text='Generate!', manager=manager)
minimum_dist_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 25), (200, 25)), start_value=10, value_range=(1,500), click_increment=1, manager=manager)
maximum_dist_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 75), (200, 25)), start_value=20, value_range=(1,500), click_increment=1, manager=manager)
minimum_pad_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 175), (200, 25)), start_value=10, value_range=(5,100), click_increment=1, manager=manager)
maximum_pad_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 225), (200, 25)), start_value=20, value_range=(5,100), click_increment=1, manager=manager)


def fadeAndGenerate():
    #Todo fade and bring in screen after dots have been generated
    GenerateDots()
    for x in dottilista:
        x.draw()
    print(f"Drawing finished. Objects in list: {len(dottilista)}")

#Main program
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(dottilista) > 1:
                    dottilista.clear()
                    screen.fill((0,0,0))
                    fadeAndGenerate()
                else:
                    fadeAndGenerate()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == generate_button:
                if len(dottilista) > 1:
                    dottilista.clear()
                    screen.fill((0,0,0))
                    fadeAndGenerate()
                else:
                    fadeAndGenerate()
                    
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == minimum_dist_slider:
                randomDistanceMin = event.value
                pygame_gui.elements.UITextBox(html_text="Minimum distance " + str(randomDistanceMin), relative_rect=pygame.Rect((0,0), (200,35)), manager=manager)
            if event.ui_element == maximum_dist_slider:
                randomDistanceMax = event.value
                pygame_gui.elements.UITextBox(html_text="Maximum distance " + str(randomDistanceMax), relative_rect=pygame.Rect((0,50), (200,35)), manager=manager)
            if event.ui_element == minimum_pad_slider:
                randomPaddingMin = event.value
                pygame_gui.elements.UITextBox(html_text="Minimum padding " + str(randomPaddingMin), relative_rect=pygame.Rect((0,150), (200,35)), manager=manager)
            if event.ui_element == maximum_pad_slider:
                randomPaddingMax = event.value
                maximumPadSlider = pygame_gui.elements.UITextBox(html_text="maximum padding" + str(randomPaddingMax), relative_rect=pygame.Rect((0,200), (200,35)), manager=manager)
       
        

    #-----Slider values-----
    #DONT PUT THESE HERE! THEY CAUSE MEMLEAKS OH CRAP
    #Moved them inside the event list, no more mem leaks
    #pygame_gui.elements.UITextBox(html_text="Minimum distance " + str(randomDistanceMin), relative_rect=pygame.Rect((0,0), (200,35)), manager=manager)
    #pygame_gui.elements.UITextBox(html_text="Maximum distance " + str(randomDistanceMax), relative_rect=pygame.Rect((0,50), (200,35)), manager=manager)
    #pygame_gui.elements.UITextBox(html_text="Minimum padding " + str(randomPaddingMin), relative_rect=pygame.Rect((0,150), (200,35)), manager=manager)
    #pygame_gui.elements.UITextBox(html_text="maximum padding" + str(randomPaddingMax), relative_rect=pygame.Rect((0,200), (200,35)), manager=manager)
    #print(f"minDist: {randomDistanceMin}. distMax: {randomDistanceMax}. padMin: {randomPaddingMin}, padMax: {randomPaddingMax}")
    #--------------------

    
    
    #------Updates and refreshes-------
    manager.process_events(event)
    manager.update(time_delta)           
    window_surface.blit(screen, (0, 0))
    clock.tick(fps)
    manager.draw_ui(screen)
    pygame.display.update()

