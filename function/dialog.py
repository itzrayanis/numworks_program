import kandinsky
from ion import *
import time

ttc=0.15

def info(text):
    kandinsky.fill_rect(0, 180, 320, 40, (150, 150, 150))     
    kandinsky.draw_string(text, 10, 190, (255, 255, 255), (150, 150, 150))
    kandinsky.draw_string("Ok", 270, 190, (255, 255, 255), (150, 150, 150))
    while True:
        if keydown(KEY_OK):
            return
        time.sleep(0.05)

def dialog(text="Are you sure?"):
    kandinsky.fill_rect(0, 180, 320, 40, (150, 150, 150))     
    kandinsky.draw_string(text, 10, 190, (255, 255, 255), (150, 150, 150))
    kandinsky.draw_string("Oui", 240, 190, (255, 255, 255), (150, 150, 150))
    kandinsky.draw_string("Non", 280, 190, (255, 255, 255), (150, 150, 150))
    while True:
        if keydown(KEY_LEFT):
            time.sleep(ttc)
            return 1
        if keydown(KEY_RIGHT):
            time.sleep(ttc)
            return 0
        time.sleep(0.05)

def menu(options):
    selection = 0
    menu_y = [60, 100, 140] 
    while True:
        kandinsky.fill_rect(0, 0, 320, 222, (255,255,255))
        opt_num = 0
        for i,opt in enumerate(options):
            opt_num += 1
            color = (255,255,0) if i == selection else (0,0,0)
            bg = (100,100,100) if i == selection else (200,200,200)
            kandinsky.fill_rect(10, menu_y[i]-4, 120, 32, bg)
            kandinsky.draw_string(opt, 15, menu_y[i], color, bg)
        while True:
            if keydown(KEY_DOWN):
                selection = (selection + 1) % opt_num
                time.sleep(ttc)
                break
            if keydown(KEY_UP):
                selection = (selection - 1) % opt_num
                time.sleep(ttc)
                break
            if keydown(KEY_OK):
                time.sleep(ttc)
                return selection
            if keydown(KEY_BACKSPACE) or keydown(KEY_TOOLBOX):
                time.sleep(ttc)
                return None
            time.sleep(0.05)