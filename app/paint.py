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
    [
        (255,255,255), # White
        (0,0,0), # Black
        (128,128,128), # Gray
        (192,192,192), # Silver
        (255,0,0), # Red
        (128,0,0), # Maroon
        (255,128,128), # Light Red
        (128,64,64), # Brownish Red
        (255,255,0), # Yellow
        (128,128,0), # Olive
        (255,255,128), # Light Yellow
        (128,128,64), # Olive Gray
        (0,255,0), # Green
        (0,128,0), # Dark Green
        (128,255,128), # Light Green
        (64,128,64), # Forest Green
        (0,255,255), # Cyan
        (0,128,128), # Teal
        (128,255,255), # Light Cyan
        (64,128,128), # Blue Teal
        (0,0,255), # Blue
        (0,0,128), # Navy
        (128,128,255), # Light Blue
        (64,64,128), # Slate Blue
        (255,0,255), # Magenta
        (128,0,128), # Purple
        (255,128,255), # Light Magenta
        (128,64,128), # Plum
        (255,128,0), # Orange
        (128,64,0), # Brown
        (255,192,128), # Peach
        (128,96,64), # Tan
        (255,215,0), # Gold
        (218,165,32), # Goldenrod
        (240,230,140), # Khaki
        (139,69,19), # Saddle Brown
    ],
    [
        (255,240,245), # Lavender Blush
        (230,230,250), # Lavender
        (176,224,230), # Powder Blue
        (135,206,250), # Light Sky Blue
        (173,216,230), # Light Blue
        (176,196,222), # Light Steel Blue
        (127,255,212), # Aquamarine
        (152,251,152), # Pale Green
        (60,179,113), # Medium Sea Green
        (95,158,160), # Cadet Blue
        (244,164,96), # Sandy Brown
        (222,184,135), # Burly Wood
        (210,180,140), # Tan
        (188,143,143), # Rosy Brown
        (255,228,225), # Misty Rose
        (250,235,215), # Antique White
        (255,239,213), # Papaya Whip
        (255,228,181), # Moccasin
        (255,222,173), # Navajo White
        (245,222,179), # Wheat
        (255,250,205), # Lemon Chiffon
        (250,250,210), # Light Goldenrod Yellow
        (255,239,213), # Papaya Whip
        (255,245,238), # Seashell
        (220,220,220), # Gainsboro
        (211,211,211), # Light Gray
        (192,192,192), # Silver
        (169,169,169), # Dark Gray
        (112,128,144), # Slate Gray
        (119,136,153), # Light Slate Gray
        (47,79,79), # Dark Slate Gray
        (105,105,105), # Dim Gray
        (0,139,139), # Dark Cyan
        (0,100,0), # Dark Green
        (85,107,47), # Dark Olive Green
        (189,183,107), # Dark Khaki
    ],
    [
        (255,192,203), # Pink
        (255,105,180), # Hot Pink
        (255,20,147),  # Deep Pink
        (199,21,133),  # Medium Violet Red
        (219,112,147), # Pale Violet Red
        (255,160,122), # Light Salmon
        (250,128,114), # Salmon
        (233,150,122), # Dark Salmon
        (255,69,0), # Red Orange
        (255,140,0), # Dark Orange
        (255,215,0), # Gold
        (218,112,214), # Orchid
        (221,160,221), # Plum
        (238,130,238), # Violet
        (216,191,216), # Thistle
        (186,85,211), # Medium Orchid
        (147,112,219), # Medium Purple
        (123,104,238), # Medium Slate Blue
        (106,90,205), # Slate Blue
        (72,61,139), # Dark Slate Blue
        (65,105,225), # Royal Blue
        (30,144,255), # Dodger Blue
        (100,149,237), # Cornflower Blue
        (70,130,180), # Steel Blue
        (176,224,230), # Powder Blue
        (0,191,255), # Deep Sky Blue
        (135,206,235), # Sky Blue
        (135,206,250), # Light Sky Blue
        (0,206,209), # Dark Turquoise
        (72,209,204), # Medium Turquoise
        (32,178,170), # Light Sea Green
        (60,179,113), # Medium Sea Green
        (46,139,87), # Sea Green
        (152,251,152), # Pale Green
        (143,188,143), # Dark Sea Green
        (102,205,170), # Medium Aquamarine
    ]
]

# Def

def clear_screen():
    kandinsky.fill_rect(0,0,320,222,font_color)

def clear():
    points.clear()
    clear_screen()

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
        draw()
        kandinsky.fill_rect(0, 0, 320, 222, font_color)
        kandinsky.fill_rect(0, 0, 150, 222, (200,200,200))
        kandinsky.draw_string("Options", 15, 15, (0,0,0),(200,200,200))
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
        clear_screen()
        draw()

        kandinsky.fill_rect(0,0,320,60,(200,200,200))
        kandinsky.draw_string("Scale :", 105, 10, (0,0,0),(200,200,200))

        kandinsky.fill_rect(80, 35, 20, 20, (200,200,200))
        kandinsky.draw_string("<", 85, 35, (0,0,0), (200,200,200))

        kandinsky.fill_rect(120, 35, 80, 20, (200,200,200))
        kandinsky.draw_string(str(taille), 155, 35, (0,0,0), (200,200,200))

        kandinsky.fill_rect(220, 35, 20, 20, (200,200,200))
        kandinsky.draw_string(">", 225, 35, (0,0,0), (200,200,200))

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

    n_palettes = len(color_choices)
    palette_idx = 0  
    idx = 0

    while palette_idx < n_palettes and len(color_choices[palette_idx]) == 0:
        palette_idx += 1
    if palette_idx == n_palettes:  
        return

    colors = color_choices[palette_idx]
    nb = len(colors)
    if nb == 0:
        return

    done = False
    color_width = 26
    visible_count = (320 - 30) // color_width
    first_visible = 0  

    while not done:
        colors = color_choices[palette_idx]
        nb = len(colors)
        if idx >= nb:
            idx = nb-1 if nb > 0 else 0
        if nb == 0:
            kandinsky.fill_rect(0, 0, 320, 222, (200,200,200))
            kandinsky.draw_string("Empty palette", 100, 100, (255,0,0), (200,200,200))
            kandinsky.draw_string("Change with UP/DOWN", 60, 120, (0,0,0), (200,200,200))
            time.sleep(0.15)
        else:
            bg_color = font_color if not is_bg else colors[idx]
            kandinsky.fill_rect(0, 0, 320, 222, bg_color)
            draw()
            kandinsky.fill_rect(0,0,320,80,(200,200,200))  
            titre = "Background" if is_bg else "Color"
            kandinsky.draw_string(titre, 120, 10, (0,0,0), (200,200,200))
    
            kandinsky.draw_string("%d/%d" % (palette_idx+1, n_palettes), 280, 10, (0,0,0), (200,200,200)) 

            if idx < first_visible:
                first_visible = idx
            elif idx > first_visible + visible_count - 1:
                first_visible = idx - visible_count + 1
            if nb > visible_count:
                first_visible = min(first_visible, nb-visible_count)
                first_visible = max(0, first_visible)
            else:
                first_visible = 0

            for dispIndex in range(visible_count):
                colorIndex = first_visible + dispIndex
                if colorIndex >= nb:
                    break
                couleur = colors[colorIndex]
                x = 30 + dispIndex*color_width
                y = 40
                kandinsky.fill_rect(x, y, 20, 20, couleur)
                if idx == colorIndex:
                    kandinsky.fill_rect(x-2, y-5, 24, 4, (255,0,0))

            if nb > visible_count:
                if first_visible > 0:
                    kandinsky.draw_string("<", 8, 40, (100,100,100), (200,200,200))
                if first_visible + visible_count < nb:
                    kandinsky.draw_string(">", 320-18, 40, (100,100,100), (200,200,200))

            if not is_bg:
                if nb > 0:
                    kandinsky.fill_rect(135, 150, 50, 50, colors[idx])

        arrow_up_color = (60,60,200) if palette_idx > 0 else (180,180,180)
        arrow_down_color = (60,60,200) if palette_idx < n_palettes-1 else (180,180,180)
        kandinsky.draw_string("^", 8, 10, arrow_up_color, (200,200,200))
        kandinsky.draw_string("v", 8, 25, arrow_down_color, (200,200,200))

        while True:
            if nb>0 and keydown(KEY_LEFT):
                idx = (idx-1) % nb
                if is_bg:
                    font_color = colors[idx]
                    clear_screen()
                time.sleep(0.15)
                break
            if nb>0 and keydown(KEY_RIGHT):
                idx = (idx+1) % nb
                if is_bg:
                    font_color = colors[idx]
                    clear_screen()
                time.sleep(0.15)
                break
            if n_palettes>1 and keydown(KEY_UP):
                prev_palette = palette_idx
                while True:
                    palette_idx = (palette_idx-1) % n_palettes
                    if len(color_choices[palette_idx]) > 0 or palette_idx == prev_palette:
                        break
                # try to keep idx on the same color index if possible
                nb = len(color_choices[palette_idx])
                if nb > 0:
                    idx = min(idx, nb-1)
                else:
                    idx = 0
                time.sleep(0.15)
                break
            if n_palettes>1 and keydown(KEY_DOWN):
                prev_palette = palette_idx
                while True:
                    palette_idx = (palette_idx+1) % n_palettes
                    if len(color_choices[palette_idx]) > 0 or palette_idx == prev_palette:
                        break
                nb = len(color_choices[palette_idx])
                if nb > 0:
                    idx = min(idx, nb-1)
                else:
                    idx = 0
                time.sleep(0.15)
                break
            if nb>0 and keydown(KEY_OK):
                if is_bg:
                    font_color = colors[idx]
                    clear_screen()
                else:
                    selected_color = colors[idx]
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
        if shift == False:
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
        elif shift == True:
            confirm = dialog(text="Do you clear ?")
            time.sleep(ttc)
            if confirm == 1:
                clear()
                cursor_x=0
                cursor_y=0
                cursor()
            if confirm == 0:
                clear_screen()    
                cursor()
            time.sleep(0.15)

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

    if keydown(KEY_HOME):
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
