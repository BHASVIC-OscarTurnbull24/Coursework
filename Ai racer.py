import pygame
import numpy as np
import time
#track 1080 X 695  779 X501, finish width 125 PX 60, car 30x60

pygame.init() #Initialises pygame so its functionality can be used
pygame.font.init()
title_font = pygame.font.SysFont('Aptos', 120)
body_font = pygame.font.SysFont('Aptos', 40)
screen = pygame.display.set_mode((1243, 800)) #Creates a display window with 800 horizontal pixels and 600 vertical pixels


#Customising pygame window
pygame.display.set_caption("Ai racer")
icon = pygame.image.load('Racecar.png')
pygame.display.set_icon(icon)


def menu():
    running = True
    while running:
        screen.fill((10,200,0))
        title = title_font.render('Ai racer', False, (255,255,255))
        screen.blit(title,(480,50))
        title = body_font.render('Press S for settings, press R to start racing', False, (255,255,255))
        screen.blit(title,(60,250))

        for event in pygame.event.get(): #event handling
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #This means it was the s key
                        running = False
                        return 'R'
                if event.key == pygame.K_s: #This means it was the s key
                        running = False
                        return 'S'
                

        pygame.display.update()


def settings():
    screen.fill((10,200,0))
    pygame.display.update()

def results():
    screen.fill((10,200,0))
    pygame.display.update()


def game_loop():
    """ Class definitions"""

    CarImage = pygame.image.load('Racecar.png') #Sets the Surface object CarImage equal to Car temp.png
    CarImage = pygame.Surface.convert_alpha(CarImage) #Converts that image so that it can contain pixel alphas
    

    class Car(pygame.sprite.Sprite):

        def __init__(self,XPos,YPos,Rotation,CarImage):
            pygame.sprite.Sprite.__init__(self)
            self.XPos = XPos
            self.YPos = YPos
            self.Rotation = Rotation
            self.XSpeed = 0
            self.YSpeed = 0
            self.ResultantSpeed = 0
            self.CarImage = pygame.Surface.convert_alpha(CarImage)
            self.DisplayCarImage = self.CarImage
            self.rect = self.DisplayCarImage.get_rect()
            self.rect.topleft = (self.XPos,self.YPos)
            self.mask = pygame.mask.from_surface(self.DisplayCarImage)
            self.LapCount = 0
            self.LastCheckpoint = 0




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


        def set_image(self, image):
            self.DisplayCarImage = image

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
                end_game(self)
        
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
            self.image = pygame.Surface.convert_alpha(pygame.image.load("Checkpoint.png"))
            self.image = pygame.transform.scale(self.image,(width,1))
            self.image = pygame.transform.rotate(self.image,rotation)
            self.XPos = x
            self.YPos = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.XPos,self.YPos)
            self.mask = pygame.mask.from_surface(self.image)
            self.CheckNo = CheckNo


        def get_rect(self): #Getter for the rect of the checkpoint
            return self.rect

        def get_mask(self): #Getter for the mask of the checkpoint
            return self.mask
        
        def get_image(self): #Getter for the image of the checkpoint
            return self.image

        def get_XPos(self): #Getter for the mask of the checkpoint
            return self.XPos
        
        def get_YPos(self): #Getter for the image of the checkpoint
            return self.YPos   
        
        def display_checkpoint(self): #Method to display the checkpointto the screen
            screen.blit(self.image,(self.XPos,self.YPos))


        





    """ End class definitions"""
                
    """Global subroutines start"""

    def abs(number):
        if number <0:
            return number * -1
        else:
            return number
        
    def checkpoint_reached(TheCar,CheckNo,TotalChecks):
        if CheckNo == TheCar.get_checks() + 1:
            if CheckNo == TotalChecks + 1:
                TheCar.finished_lap(TotalLaps)
            else:
                TheCar.next_checkpoint()
        else:
            TheCar.wrong_checkpoint()

    def end_game(theCar):
        print("w")





    """ Global subroutines end"""

    #Instantiating the car and racetrack objects
    Car1 = Car(210,500,0,CarImage)
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
    CarGroup = pygame.sprite.Group()
    CarGroup.add(Car1)




    #Definitions of global variables used in the game

    running = True
    IsGoingUp = False
    IsGoingDown = False
    IsTurningLeft = False
    IsTurningRight = False
    Friction = 0.0095
    Acceleration = 0.055
    RotationAmount = 0.45
    StartTime = time.perf_counter()
    FrameRate = 0.0165000000
    TotalLaps = 3 #This will become a player input later
    '''Variables only used to test the mean and standard deviation of time between frames
    count = 0
    total = 0
    sigmaXSquared = 0
    '''
    NormalFriction = 0.0095
    OffTrackFriction = 0.04

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
        

        if not IsGoingUp or not IsGoingDown: #If both IsGoingUp and IsGoingDown are true, then the speed remains the same
            if IsGoingUp:
                Car1.set_speed((Car1.get_ResultantSpeed() + Acceleration + 0.00003 * Car1.get_ResultantSpeed()))
            elif IsGoingDown:
                Car1.set_speed((Car1.get_ResultantSpeed() - Acceleration - 0.00003 * Car1.get_ResultantSpeed()))

        if not IsTurningLeft or not IsTurningRight:#If both IsTurningLeft and IsTurningRight are true, then the angle remains the same
            if IsTurningLeft:
                Car1.set_image(Car1.rotate_car(-RotationAmount *Car1.get_ResultantSpeed(), Car1.get_image())) 
            elif IsTurningRight:
                Car1.set_image(Car1.rotate_car(RotationAmount *Car1.get_ResultantSpeed(), Car1.get_image())) 
            



        for event in pygame.event.get(): #event handling
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN: # This means any key has been PRESSED
                if event.key == pygame.K_a: #This means it was the a key
                    IsTurningLeft = True

                if event.key == pygame.K_d: #This means it was the d key
                    IsTurningRight = True

                if event.key == pygame.K_w: #This means it was the w key
                    IsGoingUp = True

                if event.key == pygame.K_s: #This means it was the s key
                    IsGoingDown = True

                

            if event.type == pygame.KEYUP: # This means any key has been LET GO OF
                if event.key == pygame.K_a: #This means it was the a key
                    IsTurningLeft = False

                if event.key == pygame.K_d: #This means it was the d key
                    IsTurningRight = False

                if event.key == pygame.K_w: #This means it was the w key
                    IsGoingUp = False

                if event.key == pygame.K_s: #This means it was the s key
                    IsGoingDown = False


            #end event handling

        #Adding frictional forces to the car's speed
        if Car1.get_ResultantSpeed() != 0:
            Car1.set_speed(Car1.get_ResultantSpeed() - Friction *Car1.get_ResultantSpeed())
        


        screen.fill((10,200,0))
        Car1.move_car()


        #Rectangle collision detection between the track and the car
        if pygame.sprite.spritecollide(Track1, CarGroup, False):
            #Mask collision detection between the track and the car
            if pygame.sprite.spritecollide(Track1, CarGroup,False, pygame.sprite.collide_mask):
                Friction = NormalFriction 
            else:
                Friction = OffTrackFriction     

        else:
            Friction = OffTrackFriction

        #Rectangle collision detection between the finish line and the car
        if pygame.sprite.spritecollide(Finishline1, CarGroup, False):
            #Mask collision detection between the finish line and the car
            if pygame.sprite.spritecollide(Finishline1, CarGroup,False, pygame.sprite.collide_mask):
                checkpoint_reached(Car1,TotalChecks + 1,TotalChecks)

        for i in range(TotalChecks): #Checks if any of the checkpoints have collided with the car
            if pygame.sprite.collide_rect(Car1,CheckArray[i]):
                checkpoint_reached(Car1,i + 1,TotalChecks)
            

        
        
        
        Track1.display_track()
        Car1.display_car()
        Finishline1.display_FinishLine()
        #for i in range(TotalChecks): #displays every checkpoint on the screen (for testing)
        #    CheckArray[i].display_checkpoint()
        
        
        
        pygame.display.update()
        
    '''End game loop'''

'''Code to test the mean and standard deviation of the time between frames

print("\n\nMean = ", total/count)
print("Standard deviation = ",np.sqrt(sigmaXSquared/count - (total/count)**2))
'''


next_process = menu()
if next_process == 'R':
    game_loop()
elif next_process == 'S':
    settings()
pygame.quit()



