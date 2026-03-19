from ion import *
import kandinsky
import time

SCREEN_W  = 320
SCREEN_H  = 222
TOOLBAR_H = 18
CANVAS_H  = SCREEN_H - TOOLBAR_H  

TAILLE_MIN = 4
TAILLE_MAX = 40
MAX_PTS    = 1000
TTC        = 0.2

CELL_SIZE  = 12 
COL_ALIVE  = (0, 0, 0)
COL_DEAD   = (255, 255, 255)
CURSOR_COL = (255, 220, 0)

state = {
    "running"   : False,
    "cursor_x"  : 8,
    "cursor_y"  : 8,
    "mode"      : "draw", 
}

cells = [] 

def S(k): return state[k]
def SET(k, v): state[k] = v

def draw_canvas():
    kandinsky.fill_rect(0, 0, SCREEN_W, CANVAS_H, COL_DEAD)
    for x, y in cells:
        kandinsky.fill_rect(x, y, CELL_SIZE, CELL_SIZE, COL_ALIVE)

def draw_cursor():
    if S("mode") == "run":
        return
    cx, cy = S("cursor_x"), S("cursor_y")
    kandinsky.fill_rect(cx, cy, CELL_SIZE, 2, CURSOR_COL)
    kandinsky.fill_rect(cx, cy, 2, CELL_SIZE, CURSOR_COL)
    kandinsky.fill_rect(cx+CELL_SIZE-2, cy, 2, CELL_SIZE, CURSOR_COL)
    kandinsky.fill_rect(cx, cy+CELL_SIZE-2, CELL_SIZE, 2, CURSOR_COL)

def draw_toolbar():
    tb_y = CANVAS_H
    mode_label = {"draw":"DESSIN", "erase":"EFFACE", "run":"RUN"}[S("mode")]
    kandinsky.fill_rect(0, tb_y, SCREEN_W, TOOLBAR_H, (40, 40, 40))
    kandinsky.draw_string("Mode:%s   Cells:%d   OK:step  9:step  Toolbox:Menu" % (
        mode_label, len(cells)), 6, tb_y+2, (255,255,0), (40,40,40))

def refresh():
    draw_canvas()
    draw_cursor()
    draw_toolbar()

def info(text):
    kandinsky.fill_rect(0, CANVAS_H - 22, SCREEN_W, 22, (60, 60, 60))
    kandinsky.draw_string(text, 6, CANVAS_H - 18, (255,255,255), (60,60,60))
    kandinsky.draw_string("[OK]", 268, CANVAS_H - 18, (255,220,0), (60,60,60))
    while True:
        if keydown(KEY_OK):
            time.sleep(TTC)
            return

def cell_at_cursor():
    cx, cy = S("cursor_x"), S("cursor_y")
    for c in cells:
        if c[0] == cx and c[1] == cy:
            return c
    return None

def add_cell_at_cursor():
    if len(cells) >= MAX_PTS:
        info("Too many cells !")
        return
    if cell_at_cursor() is None:
        cells.append((S("cursor_x"), S("cursor_y")))

def remove_cell_at_cursor():
    c = cell_at_cursor()
    if c:
        cells.remove(c)

def toggle_mode():
    m = S("mode")
    SET("mode", "erase" if m == "draw" else "draw")

def move_cursor(dx, dy):
    x = max(0, min(S("cursor_x") + dx * CELL_SIZE, SCREEN_W - CELL_SIZE))
    y = max(0, min(S("cursor_y") + dy * CELL_SIZE, CANVAS_H - CELL_SIZE))
    SET("cursor_x", x)
    SET("cursor_y", y)

def clear_cells():
    cells.clear()

def neighbors(cell):
    x, y = cell
    nbs = []
    for dx in (-CELL_SIZE, 0, CELL_SIZE):
        for dy in (-CELL_SIZE, 0, CELL_SIZE):
            if dx == 0 and dy == 0: continue
            nx, ny = x+dx, y+dy
            if 0 <= nx < SCREEN_W and 0 <= ny < CANVAS_H:
                nbs.append((nx, ny))
    return nbs

def conway_step():
    count = {}
    for c in cells:
        for n in neighbors(c):
            count[n] = count.get(n, 0) + 1
    new_cells = []
    checked = set()
    for pos, cnt in count.items():
        if cnt == 3 or (cnt == 2 and pos in cells):
            if pos not in checked and 0 <= pos[0] < SCREEN_W and 0 <= pos[1] < CANVAS_H:
                new_cells.append(pos)
                checked.add(pos)
    cells.clear()
    for c in new_cells:
        if len(cells) < MAX_PTS:
            cells.append(c)

def menu():
    options = ["Play/Stop", "Clean", "Quit"]
    sel = 0
    n = len(options)
    menu_y = [50 + i * 36 for i in range(n)]
    while True:
        kandinsky.fill_rect(0, 0, SCREEN_W, SCREEN_H, (30,30,30))
        kandinsky.fill_rect(0,0,165,SCREEN_H, (50,50,50))
        kandinsky.draw_string("OPTIONS", 18, 14, (255,220,0), (50,50,50))
        for i, opt in enumerate(options):
            active = (i==sel)
            bg = (0,120,220) if active else (50,50,50)
            kandinsky.fill_rect(8, menu_y[i] - 4, 148, 26, bg)
            kandinsky.draw_string(opt, 16, menu_y[i], (255,255,255), bg)
        while True:
            if keydown(KEY_DOWN): sel = (sel+1)%n; time.sleep(TTC); break
            if keydown(KEY_UP): sel = (sel-1)%n; time.sleep(TTC); break
            if keydown(KEY_OK):
                time.sleep(TTC); return sel
            if keydown(KEY_BACKSPACE) or keydown(KEY_TOOLBOX):
                time.sleep(TTC); return None
            time.sleep(0.05)

refresh()
time.sleep(0.1)

while True:
    refresh()
    if S("mode") == "run" or S("running") is True:
        conway_step()
        time.sleep(0.14)
        if keydown(KEY_TOOLBOX):
            SET("mode","draw")
            S("running") and SET("running", False)
            menu()
            continue
    else:
        if keydown(KEY_RIGHT): move_cursor(1,0); refresh(); time.sleep(TTC)
        if keydown(KEY_LEFT): move_cursor(-1,0); refresh(); time.sleep(TTC)
        if keydown(KEY_UP): move_cursor(0,-1); refresh(); time.sleep(TTC)
        if keydown(KEY_DOWN): move_cursor(0,1); refresh(); time.sleep(TTC)

        if keydown(KEY_OK):
            if S("mode")=="draw": add_cell_at_cursor()
            elif S("mode")=="erase": remove_cell_at_cursor()
            refresh()
            time.sleep(TTC)

        if keydown(KEY_NINE):
            conway_step()
            refresh()
            time.sleep(TTC)

        if keydown(KEY_SHIFT):
            toggle_mode()
            refresh()
            time.sleep(TTC)

        if keydown(KEY_TOOLBOX):
            time.sleep(TTC)
            op = menu()
            if op == 0:
                m = S("mode")
                if m == "run":
                    SET("mode","draw")
                    SET("running",False)
                else:
                    SET("mode","run")
                    SET("running",True)
            elif op == 1:
                if len(cells) > 0:
                    clear_cells()
                    info("Effacé!")
            elif op == 2:
                info("Au revoir!")
                break
            refresh()
            time.sleep(TTC)

    time.sleep(0.02)
