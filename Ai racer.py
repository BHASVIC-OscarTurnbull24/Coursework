import pygame
import numpy as np

pygame.init() #Initialises pygame so its functionality can be used
CarImage = pygame.image.load('Car temp.png')

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
            self.XSpeed = np.cos(90-self.Rotation) * ResultantSpeed
            self.YSpeed = np.sin(90-self.Rotation) * ResultantSpeed

        elif self.Rotation < 180:
            self.XSpeed = np.cos(self.Rotation-90) * ResultantSpeed
            self.YSpeed = np.sin(self.Rotation-90) * ResultantSpeed

        elif self.Rotation < 270:
            self.XSpeed = np.cos(270-self.Rotation) * ResultantSpeed
            self.YSpeed = np.sin(270-self.Rotation) * ResultantSpeed

        else:
            self.XSpeed = np.cos(self.Rotation-270) * ResultantSpeed
            self.YSpeed = np.sin(self.Rotation-270) * ResultantSpeed
        

    def move_car(self):
        self.XPos += self.XSpeed
        self.YPos += self.YSpeed

    def rotate_car(self,angle, theCarImage):
        self.Rotation += angle
        if self.Rotation >360:
            self.Rotation -= 360
        theCarImage = pygame.transform.rotate(theCarImage,angle * -1)
        return theCarImage
        

    def display_car(self):
        screen.blit(CarImage,(self.XPos,self.YPos))
    




""" End class definitions"""
screen = pygame.display.set_mode((800, 600)) #Creates a display window with 800 horizontal pixels and 600 vertical pixels
Car1 = Car(100,100,0)


running = True
while running: #Infinite loop to prevent the display window from closing until the user decides to

    for event in pygame.event.get(): #event handling
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # This means any key has been pressed
            if event.key == pygame.K_a: #This means it was the a key
                CarImage = Car1.rotate_car(-2, CarImage)

            if event.key == pygame.K_d: #This means it was the d key
                CarImage = Car1.rotate_car(2, CarImage)

            if event.key == pygame.K_w: #This means it was the w key
                Car1.set_speed(Car1.get_ResultantSpeed() + 2)

            if event.key == pygame.K_s: #This means it was the s key
                Car1.set_speed(Car1.get_ResultantSpeed() - 2)


        #end event handling
    if Car1.get_ResultantSpeed() > 0:
        Car1.set_speed(Car1.get_ResultantSpeed() - 1)
    elif Car1.get_ResultantSpeed() < 0:
        Car1.set_speed(Car1.get_ResultantSpeed() + 1)


    screen.fill((0,0,0))
    Car1.move_car()
    Car1.display_car()
    pygame.display.update()



            
pygame.quit()


 