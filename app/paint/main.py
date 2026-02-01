from ion import *
import kandinsky 
import time
import paint_config

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
