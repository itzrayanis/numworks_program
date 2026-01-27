from ion import *
import kandinsky 
import time

# Init var and list
points = [
    {"x":0,"y":0,"w":10,"h":10,"color":(255,255,255)}
]
cursor_x=0
cursor_y=0
w=20
h=20

selected_color = (0,0,0)
font_color = (255,255,255)

shift = False

# Def

def clear_screen():
    kandinsky.fill_rect(0,0,320,222,font_color)

def draw():
    for p in points:
        kandinsky.fill_rect(p.get("x"),p.get("y"),p.get("w"),p.get("h"),p.get("color"))

def cursor():
    clear_screen()
    draw()
    kandinsky.fill_rect(cursor_x,cursor_y,w,1,(150,150,150))
    kandinsky.fill_rect(cursor_x,cursor_y,1,h,(150,150,150))
    kandinsky.fill_rect(cursor_x,cursor_y+h,w,1,(150,150,150))
    kandinsky.fill_rect(cursor_x+w,cursor_y,1,h,(150,150,150))

# Info box def

def dialog(text="Êtes-vous sûr ?"):
    print(f"Dialog:{text}")
    box_w, box_h = 320, 20

    kandinsky.fill_rect(0, 180, 320, 40, (150, 150, 150))     
    kandinsky.draw_string(text, 10, 190, (255, 255, 255), (150, 150, 150))

    # Options
    kandinsky.draw_string("Oui", 240, 190, (255, 255, 255), (150, 150, 150))
    kandinsky.draw_string("Non", 280, 190, (255, 255, 255), (150, 150, 150))

    # Boucle d’attente
    while True:
        if keydown(KEY_LEFT):
            print("LEFT")
            return 1
        if keydown(KEY_RIGHT):
            print("RIGHT")
            return 0
        time.sleep(0.05)

# Main 
cursor()
time.sleep(0.1)
while True:
    # Draw
    if keydown(KEY_OK):
        points.append({"x":cursor_x,"y":cursor_y,"w":w,"h":h,"color":selected_color})
        draw()
    if keydown(KEY_BACKSPACE):
        points.append({"x":cursor_x,"y":cursor_y,"w":w,"h":h,"color":font_color})
        draw()

    # Cursor
    if keydown(KEY_RIGHT):
        cursor_x+=w
        cursor()
        time.sleep(0.2)
    if keydown(KEY_LEFT):
        cursor_x-=w
        cursor()
        time.sleep(0.2)
    if keydown(KEY_UP):
        cursor_y-=h
        cursor()
        time.sleep(0.2)
    if keydown(KEY_DOWN):
        cursor_y+=h
        cursor()
        time.sleep(0.2)

    # Option

    if keydown(KEY_SHIFT):
        if shift == False:
            shift = True
        else:
            shift = False

    if keydown(KEY_BACKSPACE):
        if shift == True:
            time.sleep(0.2)
            confirm = dialog(text="Voulez-vous quitter ?")
            if(confirm == 1):
                clear_screen()
                kandinsky.draw_string("A bientot \nAppuyer sur RETURN \npour quitter", 10, 160, (0, 0, 0))
                exit()

                
