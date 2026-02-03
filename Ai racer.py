import pygame
import numpy as np
import time
#track 1080 X 695  779 X501, finish width 125 PX 60, car 30x60

#Global objects and variables


pygame.init() #Initialises pygame so its functionality can be used
pygame.font.init() #Creating fonts to be displayed on screen
title_font = pygame.font.SysFont('Aptos', 140)
body_font = pygame.font.SysFont('Aptos', 25)
medium_font = pygame.font.SysFont('Aptos', 63)
screen = pygame.display.set_mode((1243, 800)) #Creates a display window with 800 horizontal pixels and 600 vertical pixels
TotalLaps = 1 #This will become a player input later
LastButtonPress = 0 #Is set equal to the current time using the system's clock
DisplayCheckpoints = False
IsSinglePlayer = True #True for single player, False for 2 player
LastResult = [0.0,0] #Array holding the time taken for the last game and the player who won


#Customising pygame window
pygame.display.set_caption("Ai racer")
icon = pygame.image.load('Racecar.png')
pygame.display.set_icon(icon)



'''Global subroutines'''
def abs(number): #returns the magnitude of a number
        if number <0:
            return number * -1
        else:
            return number
        
def get_totalLaps(): #returns the total number of laps allowed to be completed in a single game
        return TotalLaps

def set_totalLaps(newValue): #sets the total number of laps allowed to be completed in a single game to a parameter
    global TotalLaps
    TotalLaps = newValue

def get_LastButtonPress(): #returns the last time a button was pressed
    return LastButtonPress

def update_LastButtonPress(): #sets the last time a button was pressed to the current time
    global LastButtonPress
    LastButtonPress = time.perf_counter()

def switch_DisplayCheckpoints():
    global DisplayCheckpoints
    DisplayCheckpoints = not DisplayCheckpoints #Toggles the checkpoints from being displayed on screen to not

def get_DisplayCheckpoints(): #getter for the display checkpoints variable
    global DisplayCheckpoints
    return DisplayCheckpoints

def switch_GameMode():
    global IsSinglePlayer
    IsSinglePlayer = not IsSinglePlayer #Toggles the game modr from 1 players to 2 players.

def get_GameMode(): #getter for the IsSinglePlayer variable
    global IsSinglePlayer
    return IsSinglePlayer

def set_results(TimeTaken, Winner): #sets the LastResult array to new values of the time taken and the winner
    global LastResult
    LastResult = [TimeTaken,Winner]
    
def get_results(): #gets the global LastResult array
    global LastResult
    return LastResult


'''global subroutines end'''
def menu():
    running = True
    class Button(): #Class for the on screen buttons which can be pressed
        def __init__(self,width,height,x,y,text,XOffset,YOffset):
            self.Width = width
            self.Height = height
            self.XPos = x
            self.YPos = y
            self.XOffset = XOffset
            self.YOffset = YOffset

            self.Surface = pygame.Surface((self.Width,self.Height)) #Creates surface for the button
            self.Rect = pygame.Rect(self.XPos,self.YPos,self.Width,self.Height) #Creates rectangle for the button
            self.Text = text
            self.Colour = 'white'
        
        def display_button(self):
            screen.blit(self.Surface,self.Rect) #Displays the button's rectangle and surface to the screen
            screen.blit(self.Text,(self.XPos +self.XOffset,self.YPos + self.YOffset)) #draws the button's text onto the screen, adjusted by the offset
        
        def update_button(self,MousePos):
            self.Surface.fill('white') #By default the button is white
            if self.Rect.collidepoint(MousePos): #If the button and mouse collide
                self.Surface.fill('yellow') #The button is yellow
                if pygame.mouse.get_pressed(num_buttons=3)[0]: #If the mouse's left click is pressed
                    if time.perf_counter() > get_LastButtonPress() + 0.6000000000:
                        update_LastButtonPress()
                        return True #Return true meaning the button was pressed
                    
                        
            
            return False #Return False meaning the button was not pressed




    CarImage = pygame.image.load('racecar.png')
    CarImage = pygame.Surface.convert_alpha(CarImage)
    while running: #Repeated loop for the main menu
        screen.fill((30,200,0)) 
        title = title_font.render('AI Racer', False, (255,255,255)) #Displays the game's title on screen in white
        screen.blit(title,(450,60))
        
        RaceButtonText = body_font.render('Start racing', False, (0,0,0)) #Creates black text to be displayed on the button
        RaceButton = Button(200,50,530,450,RaceButtonText,52,15)
        
        SettingsButtonText = body_font.render('Settings', False, (0,0,0)) #Creates black text to be displayed on the button
        SettingsButton = Button(200,50,530,650,SettingsButtonText,62,15)

        screen.blit(CarImage,(380,70))
        screen.blit(CarImage,(880,70))
        
        MousePos = pygame.mouse.get_pos() #Gets the mouse's position
        if RaceButton.update_button(MousePos): #If button 1 was pressed
            return 'R' #Returns R to begin the race
        if SettingsButton.update_button(MousePos): #If button 2 was pressed
            return 'S' #Returns S to go to settings
        
        for event in pygame.event.get(): #If the X button is pressed, the game closes
            if event.type == pygame.QUIT:
                running = False
                
        RaceButton.display_button()
        SettingsButton.display_button()
        pygame.display.update()
    return 'Q' #returns Q to quit the game


def settings():
    class Button():#Class for the on screen buttons which can be pressed
        def __init__(self,width,height,x,y,text,XOffset,YOffset):
            self.Width = width
            self.Height = height
            self.XPos = x
            self.YPos = y
            self.XOffset = XOffset
            self.YOffset = YOffset

            self.Surface = pygame.Surface((self.Width,self.Height)) #Creates surface for the button
            self.Rect = pygame.Rect(self.XPos,self.YPos,self.Width,self.Height) #Creates rectangle for the button
            self.Text = text
            self.Colour = 'white'
        
        def display_button(self):
            screen.blit(self.Surface,self.Rect) #Displays the button's rectangle and surface to the screen
            screen.blit(self.Text,(self.XPos +self.XOffset,self.YPos + self.YOffset)) #draws the button's text onto the screen, adjusted by the offset
        
        def update_button(self,MousePos):
            self.Surface.fill('white') #By default the button is white
            if self.Rect.collidepoint(MousePos): #If the button and mouse collide
                self.Surface.fill('yellow') #The button is yellow
                if pygame.mouse.get_pressed(num_buttons=3)[0]: #If the mouse's left click is pressed
                    if time.perf_counter() > get_LastButtonPress() + 0.6000000000:
                        update_LastButtonPress()
                        return True #Return true meaning the button was pressed
                    
                        
            
            return False #Return False meaning the button was not pressed



    running = True
    while running: #Repeated loop for the main menu
        screen.fill((30,200,0)) 
        title = title_font.render('Settings', False, (255,255,255)) #Displays the word settings on the top of the screen
        screen.blit(title,(450,20))
        
        
        LapsText = medium_font.render('Total laps: ' + str(get_totalLaps()),False,(255,255,255))
        screen.blit(LapsText,(480,120))

        if get_DisplayCheckpoints():
            DisplayCheckpointText = medium_font.render('CheckPoints are being displayed',False,(255,255,255))
            screen.blit(DisplayCheckpointText,(250,280))
        else:
            DisplayCheckpointText = medium_font.render('CheckPoints are not being displayed',False,(255,255,255))
            screen.blit(DisplayCheckpointText,(250,280))

        if get_GameMode():
            GameModeText = medium_font.render('1 player is selected',False,(255,255,255))
            screen.blit(GameModeText,(440,450))
        else:
            DisplayCheckpointText = medium_font.render('2 players are selected',False,(255,255,255))
            screen.blit(DisplayCheckpointText,(440,450))

        LapIncreaseButtonText = body_font.render('Increase number of laps', False, (0,0,0)) #Creates black text to be displayed on the button
        LapIncreaseButton = Button(200,50,330,200,LapIncreaseButtonText,0,15)
        
        LapDecreaseButtonText = body_font.render('Decrease number of laps', False, (0,0,0)) #Creates black text to be displayed on the button
        LapDecreaseButton = Button(200,50,730,200,LapDecreaseButtonText,0,15)

        ToggleCheckpointDisplayButtonText = body_font.render('Toggle checkpoint display', False, (0,0,0)) #Creates black text to be displayed on the button
        ToggleCheckpointDisplayButton = Button(230,50,530,350,ToggleCheckpointDisplayButtonText,0,15)

        ToggleGameModeButtonText = body_font.render('Toggle 1/2 players', False, (0,0,0)) #Creates black text to be displayed on the button
        ToggleGameModeButton = Button(200,50,540,550,ToggleGameModeButtonText,0,15)

        MenuButtonText = body_font.render('Back to main menu', False, (0,0,0)) #Creates black text to be displayed on the button
        MenuButton = Button(200,50,540,700,MenuButtonText,0,15)
        
        MousePos = pygame.mouse.get_pos() #Gets the mouse's position
        if LapIncreaseButton.update_button(MousePos): #If the lap increase button was pressed
            if get_totalLaps() <10:
                set_totalLaps(get_totalLaps() + 1) 
        if LapDecreaseButton.update_button(MousePos): #If the lap decrease button was pressed
            if get_totalLaps() >1:
                set_totalLaps(get_totalLaps() - 1) 
        if ToggleCheckpointDisplayButton.update_button(MousePos): 
            switch_DisplayCheckpoints()

        if ToggleGameModeButton.update_button(MousePos): 
            switch_GameMode()

        if MenuButton.update_button(MousePos): #If the menu button was pressed
            return 'M' #Returns M to go to the main menu
        
        for event in pygame.event.get(): #If the X button is pressed, the game closes
            if event.type == pygame.QUIT:
                running = False
                
        LapIncreaseButton.display_button()
        LapDecreaseButton.display_button()
        ToggleCheckpointDisplayButton.display_button()
        ToggleGameModeButton.display_button()
        MenuButton.display_button()
        pygame.display.update()
    return 'Q'

def results():
    class Button():#Class for the on screen buttons which can be pressed
        def __init__(self,width,height,x,y,text,XOffset,YOffset):
            self.Width = width
            self.Height = height
            self.XPos = x
            self.YPos = y
            self.XOffset = XOffset
            self.YOffset = YOffset

            self.Surface = pygame.Surface((self.Width,self.Height)) #Creates surface for the button
            self.Rect = pygame.Rect(self.XPos,self.YPos,self.Width,self.Height) #Creates rectangle for the button
            self.Text = text
            self.Colour = 'white'
        
        def display_button(self):
            screen.blit(self.Surface,self.Rect) #Displays the button's rectangle and surface to the screen
            screen.blit(self.Text,(self.XPos +self.XOffset,self.YPos + self.YOffset)) #draws the button's text onto the screen, adjusted by the offset
        
        def update_button(self,MousePos):
            self.Surface.fill('white') #By default the button is white
            if self.Rect.collidepoint(MousePos): #If the button and mouse collide
                self.Surface.fill('yellow') #The button is yellow
                if pygame.mouse.get_pressed(num_buttons=3)[0]: #If the mouse's left click is pressed
                    if time.perf_counter() > get_LastButtonPress() + 0.6000000000:
                        update_LastButtonPress()
                        return True #Return true meaning the button was pressed
                    
                        
            
            return False #Return False meaning the button was not pressed




    running = True
    while running:
        screen.fill((10,200,0))
        title = title_font.render('Race Finish!', False, (255,255,255)) #Displays the words 'Race finish' at the top of the screen
        screen.blit(title,(450,50))

        PlayerWon = medium_font.render('Player ' + str(get_results()[1]) + ' won!', False, (255,255,255)) #Displays which player won the game
        screen.blit(PlayerWon,(450,250))

        TimeLaps = medium_font.render('It took ' + str(get_results()[0]) + ' seconds to beat ' + str(get_totalLaps()) + ' laps', False, (255,255,255)) #Displays the time taken and how many laps were raced
        screen.blit(TimeLaps,(300,350))


            
        RaceButtonText = body_font.render('New race', False, (0,0,0)) #Creates black text to be displayed on the button
        RaceButton = Button(200,50,530,450,RaceButtonText,52,15)
            
        MenuButtonText = body_font.render('Main menu', False, (0,0,0)) #Creates black text to be displayed on the button
        MenuButton = Button(200,50,530,650,MenuButtonText,62,15)
            
        MousePos = pygame.mouse.get_pos() #Gets the mouse's position
        if RaceButton.update_button(MousePos): #If button 1 was pressed
            return 'R' #Returns R to begin the race
        if MenuButton.update_button(MousePos): #If button 2 was pressed
            return 'M' #Returns M to go to the menu
            
        for event in pygame.event.get(): #If the X button is pressed, the game closes
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                    
        RaceButton.display_button()
        MenuButton.display_button()
        pygame.display.update()
    return 'Q'
            


def game_loop():
    """ Class definitions"""

    CarImage = pygame.image.load('Racecar.png') #Sets the Surface object CarImage equal to Car temp.png
    CarImage = pygame.Surface.convert_alpha(CarImage) #Converts that image so that it can contain pixel alphas
    

    class Car(pygame.sprite.Sprite):

        def __init__(self,XPos,YPos,Rotation,CarImage,PlayerNo):
            pygame.sprite.Sprite.__init__(self)
            self.XPos = XPos    
            self.YPos = YPos
            self.Rotation = Rotation
            self.XSpeed = 0 #Sets speeds to 0 as the car is initially not moving
            self.YSpeed = 0
            self.ResultantSpeed = 0
            self.CarImage = pygame.Surface.convert_alpha(CarImage) #Makes it so pixels can be transparent
            self.DisplayCarImage = self.CarImage
            self.rect = self.DisplayCarImage.get_rect()
            self.rect.topleft = (self.XPos,self.YPos)
            self.mask = pygame.mask.from_surface(self.DisplayCarImage)
            self.LapCount = 0
            self.LastCheckpoint = 0
            self.PlayerNo = PlayerNo #Number of the player, 1 for player 1, 2 for player 2 etc
            self.IsGoingUp = False #Boolean to store if the car is currently moving up
            self.IsGoingDown = False #Boolean to store if the car is currently moving down
            self.IsTurningLeft = False #Boolean to store if the car is currently turning left
            self.IsTurningRight = False #Boolean to store if the car is currently turning right
            self.Friction = 0.0095 #Value of friction being applied on this specific car




    #Getters and setters
        def get_XPos(self): #Getter for the X position of the car
            return self.XPos
        
        def get_YPos(self): #Getter for the Y position of the car
            return self.YPos
        
        def get_XSpeed(self): #Getter for the X speed of the car
            return self.XSpeed
        
        def get_YSpeed(self): #Getter for the Y speed of the car
            return self.YSpeed
        
        def get_ResultantSpeed(self): #Getter for the resultant speed of the car
            return self.ResultantSpeed
        
        def get_Rotation(self): #Getter for the rotation of the car
            return self.Rotation
        
        def get_rect(self): #Getter for the rect of the car
            return self.rect
        
        def get_mask(self): #Getter for the mask of the car
            return self.mask
        
        def get_image(self): #Getter for the image of the car
            return self.CarImage
        
        def get_checks(self):
            return self.LastCheckpoint
        
        def get_laps(self):
            return self.LapCount
        
        def get_PlayerNo(self):
            return self.PlayerNo
        
        def get_IsGoingUp(self): #Getter for if the car is going up
            return self.IsGoingUp

        def get_IsGoingDown(self): #Getter for if the car is going down
            return self.IsGoingDown

        def get_IsTurningLeft(self): #Getter for if the car is turning left
            return self.IsTurningLeft

        def get_IsTurningRight(self): #Getter for if the car is turning right
            return self.IsTurningRight
        
        def get_Friction(self): #Getter for the friction of the car
            return self.Friction
        
        def set_Friction(self,NewValue): #Setter for the friction of the car
            self.Friction = NewValue


        def set_image(self, image):
            self.DisplayCarImage = image


        def set_IsGoingUp(self,NewValue): #Setter for if the car is going up
            self.IsGoingUp = NewValue

        def set_IsGoingDown(self,NewValue): #Setter for if the car is going down
            self.IsGoingDown = NewValue

        def set_IsTurningLeft(self,NewValue): #Setter for if the car is turning left
            self.IsTurningLeft = NewValue

        def set_IsTurningRight(self,NewValue): #Setter for if the car is turning right
            self.IsTurningRight = NewValue

        

        def set_speed(self,ResultantSpeed): #This method takes in a new resultant speed as a parameter and updates the ResultantSpeed attribute and then calulates the correct X and Y speeds based off the rotation
            self.ResultantSpeed = ResultantSpeed
            if self.Rotation < 90:
                self.XSpeed = np.cos(np.radians(90-self.Rotation)) * ResultantSpeed
                self.YSpeed = np.sin(np.radians(90-self.Rotation)) * ResultantSpeed

            elif self.Rotation < 180:
                self.XSpeed = np.cos(np.radians(self.Rotation-90)) * ResultantSpeed
                self.YSpeed = -1 * np.sin(np.radians(self.Rotation-90)) * ResultantSpeed

            elif self.Rotation < 270:
                self.XSpeed = -1 * np.cos(np.radians(270-self.Rotation)) * ResultantSpeed
                self.YSpeed = -1 * np.sin(np.radians(270-self.Rotation)) * ResultantSpeed

            else:
                self.XSpeed = -1 * np.cos(np.radians(self.Rotation-270)) * ResultantSpeed
                self.YSpeed = np.sin(np.radians(self.Rotation-270)) * ResultantSpeed

            

        def move_car(self):
            self.XPos += self.XSpeed #update X and Y values
            self.YPos -= self.YSpeed
            

            #Adding boundaries to the screen
            if self.XPos > screen.get_width() - CarImage.get_width(): 
                self.XPos = screen.get_width() - CarImage.get_width()
            if self.YPos > screen.get_height() - CarImage.get_height():
                self.YPos = screen.get_height() - CarImage.get_height() 

            if self.XPos<0:
                self.XPos = 0
            if self.YPos<0:
                self.YPos = 0

            self.rect.topleft = (self.XPos,self.YPos)
            

        def rotate_car(self,angle, theCarImage):
            self.Rotation += angle
            if self.Rotation >360:
                self.Rotation -= 360
            if self.Rotation <0:
                self.Rotation += 360
            theCarImage = pygame.transform.rotate(theCarImage,(self.Rotation) * -1)
            self.mask = pygame.mask.from_surface(theCarImage)
            return theCarImage
            

        def display_car(self):
            screen.blit(self.DisplayCarImage,(self.XPos,self.YPos))

        
        def next_checkpoint(self):  #method to move onto the next checkpoint being required to be reached
            self.LastCheckpoint += 1
        

        def finished_lap(self, TotalLaps): #Method which increases the number of laps which have been completed.  
            print("Lap complete")
            self.LapCount += 1
            self.LastCheckpoint = 0
            if self.LapCount >= TotalLaps:
                print("Final lap done")
                return 'O' #returns O meaning the game is over and the results screen should now be displayed
            return 'C' #returns C meaning the game should continue
        
        def wrong_checkpoint(self):
            time.sleep(0)

        
            
        


    class Track(pygame.sprite.Sprite):
        def __init__(self,image,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.TrackImage = pygame.Surface.convert_alpha(pygame.image.load(image))
            self.XPos = x
            self.YPos = y
            self.rect = self.TrackImage.get_rect()
            self.rect.topleft = (self.XPos,self.YPos)
            self.mask = pygame.mask.from_surface(self.TrackImage)
            

        def get_rect(self): #Getter for the rect of the track
            return self.rect

        def get_mask(self): #Getter for the mask of the track
            return self.mask
        
        def get_image(self): #Getter for the image of the track
            return self.TrackImage

        def get_XPos(self): #Getter for the mask of the track
            return self.XPos
        
        def get_YPos(self): #Getter for the image of the track
            return self.YPos  

        def display_track(self): #Method to display the track to the screen
            screen.blit(self.TrackImage,(self.XPos,self.YPos)) 
            
    class FinishLine:
        def __init__(self,image,x,y):
            self.FinishLineImage = pygame.Surface.convert_alpha(pygame.image.load(image))
            self.XPos = x
            self.YPos = y
            self.rect = self.FinishLineImage.get_rect()
            self.rect.topleft = (self.XPos,self.YPos)
            self.mask = pygame.mask.from_surface(self.FinishLineImage)

        def get_rect(self): #Getter for the rect of the finish line
            return self.rect

        def get_mask(self): #Getter for the mask of the finish line
            return self.mask
        
        def get_image(self): #Getter for the image of the finish line
            return self.FinishLineImage

        def get_XPos(self): #Getter for the mask of the finish line
            return self.XPos
        
        def get_YPos(self): #Getter for the image of the finish line
            return self.YPos   
        
        def display_FinishLine(self): #Method to display the finish line to the screen
            screen.blit(self.FinishLineImage,(self.XPos,self.YPos))
        
    class CheckPoint:
        def __init__(self,x,y,rotation,width,CheckNo):
            self.CheckpointImage = pygame.Surface.convert_alpha(pygame.image.load("Checkpoint.png"))
            self.CheckpointImage = pygame.transform.scale(self.CheckpointImage,(width,1))
            self.CheckpointImage = pygame.transform.rotate(self.CheckpointImage,rotation)
            self.XPos = x
            self.YPos = y
            self.rect = self.CheckpointImage.get_rect()
            self.rect.topleft = (self.XPos,self.YPos)
            self.mask = pygame.mask.from_surface(self.CheckpointImage)
            self.CheckNo = CheckNo


        def get_rect(self): #Getter for the rect of the checkpoint
            return self.rect

        def get_mask(self): #Getter for the mask of the checkpoint
            return self.mask
        
        def get_image(self): #Getter for the image of the checkpoint
            return self.CheckpointImage

        def get_XPos(self): #Getter for the mask of the checkpoint
            return self.XPos
        
        def get_YPos(self): #Getter for the image of the checkpoint
            return self.YPos   
        
        def display_checkpoint(self): #Method to display the checkpointto the screen
            screen.blit(self.CheckpointImage,(self.XPos,self.YPos))


        





    """ End class definitions"""
                
    """Subroutines start"""

    
        
    def checkpoint_reached(TheCar,CheckNo,TotalChecks):
        if CheckNo == TheCar.get_checks() + 1: #If the checkpoint is correct
            if CheckNo == TotalChecks + 1: #If this is the finish line
                result = TheCar.finished_lap(TotalLaps) #Run the finished lap subroutine
                if result == 'O': #If the game is over
                    print("checkpoint reached final round")
                    return 'O'
                else:
                    return 'C'
            else:
                TheCar.next_checkpoint() #If not the finish line then run next_checkpoint
                return 'C'
        else:
            TheCar.wrong_checkpoint() #If not the correct checkpoint then run wrong_checkpoint
            return 'C'


    '''
    def checkpoint_reached(TheCar,CheckNo,TotalChecks):
        if CheckNo == TheCar.get_checks() + 1: #If the checkpoint is correct
            if CheckNo == TotalChecks + 1: #If this is the finish line
                TheCar.finished_lap(TotalLaps)
            else:
                TheCar.next_checkpoint() #If not the finish line then run next_checkpoint 
        else:
            TheCar.wrong_checkpoint() #If not the correct checkpoint then run wrong_checkpoint
    '''
    
    





    """ Subroutines end"""

    #Instantiating the car and racetrack objects
    Car1 = Car(240,540,0,CarImage,1)
    if not get_GameMode():
        Car2 = Car(180,500,0,CarImage,2)

    Track1 = Track("TEMP racetrack.png", 100,100)
    Finishline1 = FinishLine("finishline.png", 159,400)
    #Instantiating all of the checkpoints
    Check1 = CheckPoint(171,287,-45,170,1)
    Check2 = CheckPoint(320,272,90,125,2)
    Check3 = CheckPoint(430,275,90,125,3)
    Check4 = CheckPoint(540,275,90,125,4)
    Check5 = CheckPoint(595,250,-45,180,5)
    Check6 = CheckPoint(625,150,-45,160,6)
    Check7 = CheckPoint(800,136,90,110,7)
    Check8 = CheckPoint(950,136,90,110,8)
    Check9 = CheckPoint(1022,145,45,163,9)
    Check10 = CheckPoint(1022,340,0,120,10)
    Check11 = CheckPoint(1022,470,0,120,11)
    Check12 = CheckPoint(1022,590,-45,163,12)
    Check13 = CheckPoint(920,590,90,133,13)
    Check14 = CheckPoint(780,590,90,133,14)
    Check15 = CheckPoint(640,590,90,133,15)
    Check16 = CheckPoint(500,590,90,133,16)
    Check17 = CheckPoint(360,590,90,133,17)
    Check18 = CheckPoint(170,590,45,170,18)
    Check19 = CheckPoint(165,530,0,120,19)


    TotalChecks = 19

    CheckArray = [Check1,Check2,Check3,Check4,Check5,Check6,Check7,Check8,Check9,Check10,Check11,Check12,Check13,Check14,Check15,Check16,Check17,Check18,Check19]


    #Creating Sprite groups
    Car1Group = pygame.sprite.Group()
    Car1Group.add(Car1)

    if not get_GameMode():
        Car2Group = pygame.sprite.Group()
        Car2Group.add(Car2)






    #Definitions of global variables used in the game

    running = True
    Acceleration = 0.055
    RotationAmount = 0.45
    StartTime = time.perf_counter()
    FrameRate = 0.0165000000
    '''Variables only used to test the mean and standard deviation of time between frames
    count = 0
    total = 0
    sigmaXSquared = 0
    '''
    NormalFriction = 0.0095
    OffTrackFriction = 0.04
    TimerStart = time.perf_counter()



    '''Game loop'''
    while running: #Infinite loop to prevent the display window from closing until the user decides to
        
        NewTime = time.perf_counter() #newTime is set equal to the current time using the system's clock
        
        #Here is a loop which makes the game wait until the time defined in FrameRate has passed since the last iteration of the game loop
        
        while True: 
            if NewTime > StartTime + FrameRate:
                break
            NewTime = time.perf_counter()
        
            
        
    
        '''Code to test the mean and standard deviation of the time between frames

        count += 1
        total += NewTime - StartTime  
        sigmaXSquared += (NewTime - StartTime) **2
        '''

        StartTime = NewTime
        
        #print(StartTime)
        
        def car_processing(TheCar,CarGroup):
            global running
            if not TheCar.get_IsGoingUp() or not TheCar.get_IsGoingDown(): #If both IsGoingUp and IsGoingDown are true, then the speed remains the same
                if TheCar.get_IsGoingUp():
                    TheCar.set_speed((TheCar.get_ResultantSpeed() + Acceleration + 0.00003 * TheCar.get_ResultantSpeed()))
                elif TheCar.get_IsGoingDown():
                    TheCar.set_speed((TheCar.get_ResultantSpeed() - Acceleration - 0.00003 * TheCar.get_ResultantSpeed()))

            if not TheCar.get_IsTurningLeft() or not TheCar.get_IsTurningRight():#If both IsTurningLeft and IsTurningRight are true, then the angle remains the same
                if TheCar.get_IsTurningLeft():
                    TheCar.set_image(TheCar.rotate_car(-RotationAmount *TheCar.get_ResultantSpeed(), TheCar.get_image())) 
                elif TheCar.get_IsTurningRight():
                    TheCar.set_image(TheCar.rotate_car(RotationAmount *TheCar.get_ResultantSpeed(), TheCar.get_image())) 
                


            
            for event in pygame.event.get(): #event handling
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN: # This means any key has been PRESSED
                    if event.key == pygame.K_a: #This means it was the a key
                        Car1.set_IsTurningLeft(True)

                    if event.key == pygame.K_d: #This means it was the d key
                        Car1.set_IsTurningRight(True)

                    if event.key == pygame.K_w: #This means it was the w key
                        Car1.set_IsGoingUp(True) 

                    if event.key == pygame.K_s: #This means it was the s key
                        Car1.set_IsGoingDown(True)
                
                    if event.key == pygame.K_LEFT: #This means it was the a key
                        Car2.set_IsTurningLeft(True)

                    if event.key == pygame.K_RIGHT: #This means it was the d key
                        Car2.set_IsTurningRight(True)

                    if event.key == pygame.K_UP: #This means it was the w key
                        Car2.set_IsGoingUp(True) 

                    if event.key == pygame.K_DOWN: #This means it was the s key
                        Car2.set_IsGoingDown(True)


                    

                if event.type == pygame.KEYUP: # This means any key has been LET GO OF
                    if event.key == pygame.K_a: #This means it was the a key
                        Car1.set_IsTurningLeft(False)

                    if event.key == pygame.K_d: #This means it was the d key
                        Car1.set_IsTurningRight(False)
                    if event.key == pygame.K_w: #This means it was the w key
                        Car1.set_IsGoingUp(False)
                    if event.key == pygame.K_s: #This means it was the s key
                        Car1.set_IsGoingDown(False)
                    if event.key == pygame.K_LEFT: #This means it was the left key
                        Car2.set_IsTurningLeft(False)
                    if event.key == pygame.K_RIGHT: #This means it was the right key
                        Car2.set_IsTurningRight(False)
                    if event.key == pygame.K_UP: #This means it was the up key
                        Car2.set_IsGoingUp(False)
                    if event.key == pygame.K_DOWN: #This means it was the down key
                        Car2.set_IsGoingDown(False)



                #end event handling

            #Adding frictional forces to the car's speed
            if TheCar.get_ResultantSpeed() != 0:
                TheCar.set_speed(TheCar.get_ResultantSpeed() - TheCar.get_Friction() *TheCar.get_ResultantSpeed())
            


            screen.fill((10,200,0))
            TheCar.move_car()


            #Rectangle collision detection between the track and the car
            if pygame.sprite.spritecollide(Track1, CarGroup, False):
                #Mask collision detection between the track and the car
                if pygame.sprite.spritecollide(Track1, CarGroup,False, pygame.sprite.collide_mask):
                    TheCar.set_Friction(NormalFriction)
                else:
                    TheCar.set_Friction(OffTrackFriction)     

            else:
                TheCar.set_Friction(OffTrackFriction)     

            #Rectangle collision detection between the finish line and the car
            if pygame.sprite.spritecollide(Finishline1, CarGroup, False):
                #Mask collision detection between the finish line and the car
                if pygame.sprite.spritecollide(Finishline1, CarGroup,False, pygame.sprite.collide_mask):
                    result = checkpoint_reached(TheCar,TotalChecks + 1,TotalChecks)
                    if result == 'O':
                        set_results(round(NewTime-TimerStart,3),TheCar.get_PlayerNo())
                        return 'O'

            for i in range(TotalChecks): #Checks if any of the checkpoints have collided with the car
                if pygame.sprite.collide_rect(TheCar,CheckArray[i]):
                    result = checkpoint_reached(TheCar,i + 1,TotalChecks)
                    if result == 'O':
                        set_results(round(NewTime-TimerStart,3),TheCar.get_PlayerNo())
                        return 'O'
            
            
            
            

        
        if car_processing(Car1,Car1Group) == 'O':
            return 'O'
        
        if not get_GameMode():
            if car_processing(Car2,Car2Group) == 'O':
                return 'O'
        
        #Displaying objects onto screen
        Track1.display_track()
        Car1.display_car()
        if not get_GameMode():
            Car2.display_car()


        Finishline1.display_FinishLine()




        
        LapsText1 = medium_font.render('Lap ' + str(Car1.get_laps()) + "/" + str(get_totalLaps()),False,(255,255,255)) #Displays the completed laps out of the total laps on screen
        screen.blit(LapsText1,(3,0)) #Displays the text in the top left of the screen  
        if not get_GameMode():
            LapsText2 = medium_font.render('Lap ' + str(Car2.get_laps()) + "/" + str(get_totalLaps()),False,(255,255,255)) #Displays the completed laps out of the total laps on screen
            screen.blit(LapsText2,(260,0)) #Displays the text in the top left of the screen
        
        
        if DisplayCheckpoints:
            for i in range(TotalChecks): #Displays every checkpoint on the screen so that the user can understand their positions
                CheckArray[i].display_checkpoint()

        

        TimerDisplay = round(time.perf_counter() - TimerStart,3) #Finds the difference between the current time and the time that the game started and rounds it to 1 millisecond
        TimerText = medium_font.render('Timer: ' + str(TimerDisplay),False,(255,255,255)) #Displays the text of the timer on the screen
        screen.blit(TimerText,(960,0)) #Displays the timer in the top right of the screen

        
        
        
        pygame.display.update()
        
    '''End game loop'''
    return 'Q'

'''Code to test the mean and standard deviation of the time between frames

print("\n\nMean = ", total/count)
print("Standard deviation = ",np.sqrt(sigmaXSquared/count - (total/count)**2))
'''
NextProcess = menu()
running = True

while running:
    #print(next_process)

    if NextProcess == 'R':
        #print("Game loop")
        NextProcess = game_loop()

    elif NextProcess == 'S':
        #print("Settings")
        NextProcess = settings()

    elif NextProcess == 'O':
        #print("Results")
        NextProcess = results()

    elif NextProcess == 'M':
        #print("Menu")
        NextProcess = menu()

    elif NextProcess == 'Q':
        running = False

pygame.quit()


#image