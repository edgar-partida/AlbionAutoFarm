from util.Screen import Screen
import mss
import cv2
import numpy
from time import time, sleep


screen = Screen(mss,cv2,numpy,sleep,time)
def main():
    full_screen_image = screen.get_full_screen_capture()
    screen.show_dependant_image(full_screen_image)
    print("Welcome!!")
    print("Game screen coordingates are : ")
    print(screen.game_screen_coordinates)
    screen.show_image(screen.take_game_screenshot())




main()