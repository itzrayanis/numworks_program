from ion import *
import kandinsky 
import time

# Init var and list

selected_color = (0,0,0)
font_color = (255,255,255)

ttc = 0.2

start = 1
shift = False

points = [
]
cursor_x=0
cursor_y=0
w=20
h=20

color_choices = [
    (255,255,255), # White
    (0,0,0),       # Black
    (255,0,0),     # Red
    (0,0,255),     # Blue
    (0,255,0),     # Green
    (255,255,0),   # Yellow
    (255,128,0),   # Orange
    (128,0,255),   # Purple
    (255,0,128),   # Pink
    (139,69,19)    # Brown
]

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

def menu():
    options = ["Scale", "Color", "Background"]
    selection = 0
    menu_y = [60, 100, 140] 
    while True:
        kandinsky.fill_rect(0, 0, 320, 222, font_color)
        draw()
        for i,opt in enumerate(options):
            color = (255,255,0) if i == selection else (0,0,0)
            bg = (100,100,100) if i == selection else (200,200,200)
            kandinsky.fill_rect(10, menu_y[i]-4, 120, 32, bg)
            kandinsky.draw_string(opt, 15, menu_y[i], color, bg)
        while True:
            if keydown(KEY_DOWN):
                selection = (selection + 1) % 3
                time.sleep(ttc)
                break
            if keydown(KEY_UP):
                selection = (selection - 1) % 3
                time.sleep(ttc)
                break
            if keydown(KEY_OK):
                time.sleep(ttc)
                return selection
            if keydown(KEY_BACKSPACE) or keydown(KEY_TOOLBOX):
                time.sleep(ttc)
                return None
            time.sleep(0.05)

def scale_menu():
    global w, h
    curseur_y = 150
    taille_min, taille_max = 10, 30
    taille = w
    done = False
    while not done:
        # Efface l'écran
        kandinsky.fill_rect(0, 0, 320, 222, font_color)
        draw()

        kandinsky.draw_string("Scale :", 105, 10, (0,0,0), font_color)

        kandinsky.fill_rect(80, 35, 20, 20, font_color)
        kandinsky.draw_string("<", 85, 35, (0,0,0), font_color)

        kandinsky.fill_rect(120, 35, 80, 20, font_color)
        kandinsky.draw_string(str(taille), 155, 35, (0,0,0), font_color)

        kandinsky.fill_rect(220, 35, 20, 20, font_color)
        kandinsky.draw_string(">", 225, 35, (0,0,0), font_color)

        curseur_couleur = (150,150,150)
        kandinsky.fill_rect(135, curseur_y, taille, taille, curseur_couleur)

        while True:
            if keydown(KEY_LEFT):
                if taille > taille_min:
                    taille -= 2
                time.sleep(ttc)
                break
            if keydown(KEY_RIGHT):
                if taille < taille_max:
                    taille += 2
                time.sleep(ttc)
                break
            if keydown(KEY_OK):
                w = taille
                h = taille
                time.sleep(ttc)
                done = True
                break
            if keydown(KEY_BACKSPACE):
                time.sleep(ttc)
                done = True
                break
            time.sleep(0.05)

def color_menu(is_bg=False):
    global selected_color, font_color
    nb = len(color_choices)
    idx = 0
    done = False
    while not done:
        kandinsky.fill_rect(0, 0, 320, 222, font_color if not is_bg else color_choices[idx])
        draw()

        titre = "Background" if is_bg else "Color"
        kandinsky.draw_string(titre, 120, 10, (0,0,0), (255,255,255) if idx != 1 else (200, 200, 200))

        for i,couleur in enumerate(color_choices):
            x = 30 + i*26
            y = 40
            kandinsky.fill_rect(x, y, 20, 20, couleur)

            if idx == i:
                kandinsky.fill_rect(x-2, y-5, 24, 4, (255,0,0))
        if not is_bg:
            kandinsky.fill_rect(135, 150, 50, 50, color_choices[idx])

        while True:
            if keydown(KEY_LEFT):
                idx = (idx-1) % nb
                if is_bg:
                    font_color = color_choices[idx]
                    clear_screen()
                time.sleep(0.15)
                break
            if keydown(KEY_RIGHT):
                idx = (idx+1) % nb
                if is_bg:
                    font_color = color_choices[idx]
                    clear_screen()
                time.sleep(0.15)
                break
            if keydown(KEY_OK):
                if is_bg:
                    font_color = color_choices[idx]
                    clear_screen()
                else:
                    selected_color = color_choices[idx]
                time.sleep(0.15)
                done = True
                break
            if keydown(KEY_BACKSPACE):
                time.sleep(0.15)
                done = True
                break
            time.sleep(0.05)


cursor()
time.sleep(0.1)

while start == 1:
    # Draw
    if keydown(KEY_OK):
        points.append({"x":cursor_x,"y":cursor_y,"w":w,"h":h,"color":selected_color})
        draw()
        cursor()
        time.sleep(ttc)
    if keydown(KEY_BACKSPACE):
        found = None
        for p in points:
            if p.get("x") == cursor_x and p.get("y") == cursor_y and p.get("w") == w and p.get("h") == h:
                found = p
                break
        if found:
            points.remove(found)
            draw()
            cursor()
            time.sleep(ttc)

    # Cursor
    if keydown(KEY_RIGHT):
        if cursor_x+w <= 319:
            cursor_x+=w
            cursor()
            time.sleep(ttc)
    if keydown(KEY_LEFT):
        if cursor_x-w >= -1:
            cursor_x-=w
            cursor()
            time.sleep(ttc)
    if keydown(KEY_UP):
        if cursor_y-h >= -1:
            cursor_y-=h
            cursor()
            time.sleep(ttc)
    if keydown(KEY_DOWN):
        if cursor_y+h <= 210:
            cursor_y+=h
            cursor()
            time.sleep(ttc)

    # Option

    if keydown(KEY_SHIFT):
        shift = not shift
        time.sleep(ttc)

    if keydown(KEY_TOOLBOX):
        time.sleep(ttc)
        opt = menu()
        if opt == 0:
            scale_menu()
        elif opt == 1:
            color_menu(is_bg=False)
        elif opt == 2:
            color_menu(is_bg=True)

        cursor()
        time.sleep(ttc)

    if keydown(KEY_BACKSPACE):
        if shift == True:
            confirm = dialog(text="Do you want quit?")
            time.sleep(ttc)
            if confirm == 1:
                clear_screen()
                kandinsky.draw_string("See you late \nClick on RETURN \nfor exit", 10, 160, (0, 0, 0))
                start = 0
            if confirm == 0:
                clear_screen()    
                cursor()
            time.sleep(0.15)
