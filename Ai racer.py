import pygame
import numpy as np

pygame.init() #Initialises pygame so its functionality can be used
screen = pygame.display.set_mode((1130, 700)) #Creates a display window with 800 horizontal pixels and 600 vertical pixels
CarImage = pygame.image.load('Car temp.png') #Sets the Surface object CarImage equal to Car temp.png
CarImage = pygame.Surface.convert_alpha(CarImage) #Converts that image so that it can contain pixel alphas
DisplayCarImage = CarImage
""" Class definitions"""

class Car:

    def __init__(self,XPos,YPos,Rotation):
        self.XPos = XPos
        self.YPos = YPos
        self.Rotation = Rotation
        self.XSpeed = 0
        self.YSpeed = 0
        self.ResultantSpeed = 0
        pass

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
        

    def rotate_car(self,angle, theCarImage):
        self.Rotation += angle
        if self.Rotation >360:
            self.Rotation -= 360
        if self.Rotation <0:
            self.Rotation += 360
        theCarImage = pygame.transform.rotate(theCarImage,(self.Rotation) * -1)
        return theCarImage
        

    def display_car(self):
        screen.blit(DisplayCarImage,(self.XPos,self.YPos))
    




""" End class definitions"""

Car1 = Car(500,350,0)


#Definitions of global variables used in the game
running = True
IsGoingUp = False
IsGoingDown = False
IsTurningLeft = False
IsTurningRight = False
Friction = 0.0015
Acceleration = 0.0005
RotationAmount = 0.3
while running: #Infinite loop to prevent the display window from closing until the user decides to
    
    if not IsGoingUp or not IsGoingDown: #If both IsGoingUp and IsGoingDown are true, then the speed remains the same
        if IsGoingUp:
            Car1.set_speed(Car1.get_ResultantSpeed() + Acceleration)
        elif IsGoingDown:
            Car1.set_speed(Car1.get_ResultantSpeed() - Acceleration)

    if not IsTurningLeft or not IsTurningRight:#If both IsTurningLeft and IsTurningRight are true, then the angle remains the same
        if IsTurningLeft:
            DisplayCarImage = Car1.rotate_car(-RotationAmount *Car1.get_ResultantSpeed(), CarImage) 
        elif IsTurningRight:
            DisplayCarImage = Car1.rotate_car(RotationAmount *Car1.get_ResultantSpeed(), CarImage)
        



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
    if Car1.get_ResultantSpeed() > 0:
        Car1.set_speed(Car1.get_ResultantSpeed() - Friction * Car1.get_ResultantSpeed())
    elif Car1.get_ResultantSpeed() < 0:
        Car1.set_speed(Car1.get_ResultantSpeed() + Friction)



    screen.fill((0,0,0))
    Car1.move_car()
    Car1.display_car()
    pygame.display.update()



            
pygame.quit()


 