# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:07:03 2021

@author: Kevhead891
"""


from pyautogui import *
import pyautogui
import time
import keyboard


###might use it later so that it clicks slightly off everytime
#import random 
#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place

class E7ShopRefresher(object):
    window_size  = 0 
    visual_inspection_cnt = 0
    covenant_cnt = 0 
    refresh_cnt = 0 
    mystic_cnt = 0
    RB_pos = 0
    Coven_pos = 0 
    Mystic_pos = 0      

    def __init__(self, name):
        self.name = name 
    
    def init_refresher(self):
        #Aprox place X: 1263 Y:  590
        #=========================================================
        #%%Fail-Safes
        ##After each pyautogui instruction waits for 0.3 seconds
        pyautogui.PAUSE = 0.3
        ##If you drag your mouse to the upper left will abort program
        pyautogui.FAILSAFE = True
        #%%Set-up
        ##Get screen res
        self.window_size=pyautogui.size()
        ##Move to center of the screen instantly
        pyautogui.moveTo(self.window_size[0]/2, self.window_size[1]/2, duration=0)
        #number of visual inspections done on screen
        self.visual_inspection_cnt=0
        #number of coven bought
        self.covenant_cnt=0
        #number of mystic bought
        self.mystic_cnt=0
        #number of refresh done
        self.refresh_cnt=0    
    
    def scan_shop (self):
        #Search for the refresh button
        self.RB_pos=pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90)
    #The confidence is added due to little variations in the background
    #Search for the price and quantity image of covenant summon
        self.Coven_pos=pyautogui.locateOnScreen('cov.PNG',confidence=0.90)
    #Search for the price and quantity image of mystic summon
        self.Mystic_pos=pyautogui.locateOnScreen('mystic.PNG',confidence=0.90)
        if (self.Coven_pos) != None:
            print("Buy Covenant Summons.")
            self.visual_inspection_cnt=0
            # Coven_pos_buy =pyautogui.locateOnScreen('new_coven.PNG',confidence=0.93)
            Coven_point=pyautogui.center(self.Coven_pos)
            #print("La pos en x seria...",Coven_point[0],"\nLa pos en y seria...", Coven_point[1])
            #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
            pyautogui.click(x= round(1.9 * Coven_point[0]), y= round(Coven_point[1] + 30), clicks=2, interval=0.05, button='left')
            time.sleep(0.5)#wait for confirm button
            Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG', confidence=0.90)
            Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
            pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
            self.covenant_cnt+=1
    #checks for mystic
        elif (self.Mystic_pos) != None:
            print("Buy Mystic Summons.")
            self.visual_inspection_cnt=0
            # Mystic_pos_buy = pyautogui.locateOnScreen('new_mystic.PNG',confidence=0.93)
            Mystic_point=pyautogui.center(self.Mystic_pos)
            #print("x=",Mystic_point[0],"y=",Mystic_point[1])
            #print("La pos en x seria...",Mystic_point[0],"\nLa pos en y seria...", Mystic_point[1])
            #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
            pyautogui.click(x= round(1.9 * Mystic_point[0]), y= round(Mystic_point[1] + 30), clicks=2, interval=0.05, button='left')
            time.sleep(0.5)#wait for confirm button
            Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG', confidence=0.90)
            Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
            pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
            self.mystic_cnt+=1

    def drag_search(self, drag_length):

        pyautogui.moveTo(self.window_size[0]/2, self.window_size[1]/2, duration=0)
        #Drag upward 500 pixels in 0.2 seconds
        pyautogui.dragTo(self.window_size[0]/2, self.window_size[1]/2-drag_length, duration=0.2)
        time.sleep(0.1)
        self.visual_inspection_cnt = self.visual_inspection_cnt + 1

    def refresh_shop (self):
        time.sleep(0.5)
        RB_point=pyautogui.center(self.RB_pos)
        pyautogui.click(x=RB_point[0], y=RB_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(1)#wait for confirm to appear
        Confirm_pos=pyautogui.locateOnScreen('confirm button.PNG' , confidence=0.90 )
        Confirm_point=pyautogui.center(Confirm_pos)
        pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')
        self.visual_inspection_cnt=0
        time.sleep(0.5)
        self.refresh_cnt+=1
        print("Covenant Summons bought=",self.covenant_cnt)
        print("Mystic Summons bought=",self.mystic_cnt)
        print("Refresh Done=",self.refresh_cnt)


#===== Main Code ===============================


# Initialize =========
E7_Refresher_object = E7ShopRefresher('inst_1')
E7_Refresher_object.init_refresher()
#=====================

# loop bookmark search========== 
while keyboard.is_pressed('q') == False:
    time.sleep(0.2)
    E7_Refresher_object.scan_shop()
    E7_Refresher_object.drag_search(500)  # drag 500 units up 
    E7_Refresher_object.scan_shop()
    E7_Refresher_object.refresh_shop()

#==============================