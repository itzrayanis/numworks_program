from ion import *
import kandinsky
import time

# Screen constants (fixed, never in paint_config)
SCREEN_W  = 320
SCREEN_H  = 222
TOOLBAR_H = 18
CANVAS_H  = SCREEN_H - TOOLBAR_H   # 204 usable px

# Config: paint_config.py if present, otherwise default values
try:
    import paint_config
    TAILLE_MIN    = paint_config.TAILLE_MIN
    TAILLE_MAX    = paint_config.TAILLE_MAX
    MAX_PTS       = paint_config.MAX_PTS
    TTC           = paint_config.TTC
    color_choices = paint_config.color_choices
    state         = paint_config.state
    points        = list(paint_config.points)
    if "line_start" not in state: state["line_start"] = None
    if "running"    not in state: state["running"]    = True
except:
    TAILLE_MIN = 4
    TAILLE_MAX = 40
    MAX_PTS    = 500
    TTC        = 0.18

    color_choices = [
        [
            (255, 255, 255),
            (0,   0,   0  ),
            (128, 128, 128),
            (255, 0,   0  ),
            (128, 0,   0  ),
            (255, 255, 0  ),
            (0,   255, 0  ),
            (0,   255, 255),
            (0,   0,   255),
            (255, 0,   255),
            (128, 0,   128),
            (255, 128, 0  ),
            (128, 64,  0  ),
            (255, 215, 0  ),
        ]
    ]

    state = {
        "bg_color"   : (255, 255, 255),
        "draw_color" : (0,   0,   0  ),
        "w"          : 20,
        "h"          : 20,
        "cursor_x"   : 160,
        "cursor_y"   : 100,
        "mode"       : "draw",
        "running"    : True,
        "line_start" : None,
    }

    points = []

# State shortcuts
def S(k):      return state[k]
def SET(k, v): state[k] = v

# Visual constants for modes
MODE_LABELS = {
    "draw"   : "DRAW",
    "erase"  : "ERASE",
    "line"   : "LINE",
    "fill"   : "FILL",
    "pipette": "PICK",
}
MODE_COLORS = {
    "draw"   : (0,   150, 255),
    "erase"  : (220, 80,  80 ),
    "line"   : (80,  200, 80 ),
    "fill"   : (255, 165, 0  ),
    "pipette": (180, 0,   255),
}
MODES_LIST = ["draw", "erase", "line", "fill", "pipette"]

# Rendering functions
def draw_canvas():
    kandinsky.fill_rect(0, 0, SCREEN_W, CANVAS_H, S("bg_color"))
    for p in points:
        kandinsky.fill_rect(p[0], p[1], p[2], p[3], p[4])

def draw_toolbar():
    tb_y  = CANVAS_H
    mode  = S("mode")
    col   = MODE_COLORS[mode]
    label = MODE_LABELS[mode]
    pts   = len(points)

    kandinsky.fill_rect(0, tb_y, SCREEN_W, TOOLBAR_H, (40, 40, 40))

    # Active color square
    kandinsky.fill_rect(3,  tb_y + 3,  12, 12, S("draw_color"))
    kandinsky.fill_rect(3,  tb_y + 3,  12,  1, (180, 180, 180))
    kandinsky.fill_rect(3,  tb_y + 3,   1, 12, (180, 180, 180))
    kandinsky.fill_rect(14, tb_y + 3,   1, 12, (180, 180, 180))
    kandinsky.fill_rect(3,  tb_y + 14, 12,  1, (180, 180, 180))

    # Brush size
    kandinsky.draw_string("S:%d" % S("w"), 19, tb_y + 4, (220, 220, 220), (40, 40, 40))

    # Mode (LINE* if waiting for 2nd point)
    if mode == "line" and S("line_start") is not None:
        kandinsky.draw_string("LINE*", 88, tb_y + 4, (255, 220, 0), (40, 40, 40))
    else:
        kandinsky.draw_string(label, 88, tb_y + 4, col, (40, 40, 40))

    # Points counter
    cnt_col = (255, 80, 80) if pts >= MAX_PTS * 0.9 else (160, 160, 160)
    kandinsky.draw_string("%d/%d" % (pts, MAX_PTS), 195, tb_y + 4, cnt_col, (40, 40, 40))

def draw_cursor():
    cx  = S("cursor_x")
    cy  = S("cursor_y")
    cw  = S("w")
    ch  = S("h")
    col = MODE_COLORS[S("mode")]

    kandinsky.fill_rect(cx,      cy,      cw, 1,  col)
    kandinsky.fill_rect(cx,      cy,      1,  ch, col)
    kandinsky.fill_rect(cx,      cy + ch, cw, 1,  col)
    kandinsky.fill_rect(cx + cw, cy,      1,  ch, col)

    # Yellow cross on LINE start point
    ls = S("line_start")
    if ls is not None:
        lx, ly = ls
        kandinsky.fill_rect(lx,         ly + ch//2, cw, 1, (255, 220, 0))
        kandinsky.fill_rect(lx + cw//2, ly,          1, ch, (255, 220, 0))

def refresh():
    draw_canvas()
    draw_cursor()
    draw_toolbar()

# Dialogs
def info(text):
    kandinsky.fill_rect(0, CANVAS_H - 22, SCREEN_W, 22, (60, 60, 60))
    kandinsky.draw_string(text, 6, CANVAS_H - 18, (255, 255, 255), (60, 60, 60))
    kandinsky.draw_string("[OK]", 268, CANVAS_H - 18, (255, 220, 0), (60, 60, 60))
    while True:
        if keydown(KEY_OK):
            time.sleep(TTC)
            return
        time.sleep(0.05)

def confirm_dialog(text="Sure?"):
    kandinsky.fill_rect(0, CANVAS_H - 22, SCREEN_W, 22, (60, 60, 60))
    kandinsky.draw_string(text, 6, CANVAS_H - 18, (255, 255, 255), (60, 60, 60))
    kandinsky.draw_string("YES", 228, CANVAS_H - 18, (80,  220, 80), (60, 60, 60))
    kandinsky.draw_string("NO",  276, CANVAS_H - 18, (220, 80,  80), (60, 60, 60))
    while True:
        if keydown(KEY_LEFT):  time.sleep(TTC); return True
        if keydown(KEY_RIGHT): time.sleep(TTC); return False
        time.sleep(0.05)

# Canvas actions
def point_at_cursor():
    cx, cy, cw, ch = S("cursor_x"), S("cursor_y"), S("w"), S("h")
    for p in points:
        if p[0] == cx and p[1] == cy and p[2] == cw and p[3] == ch:
            return p
    return None

def action_draw():
    if len(points) >= MAX_PTS:
        info("Max %d pts!" % MAX_PTS)
        return
    if point_at_cursor() is None:
        points.append((S("cursor_x"), S("cursor_y"), S("w"), S("h"), S("draw_color")))

def action_erase():
    p = point_at_cursor()
    if p: points.remove(p)

def action_pipette():
    p = point_at_cursor()
    if p:
        SET("draw_color", p[4])
        info("Color picked!")

def action_clear():
    if confirm_dialog("Clear canvas?"):
        points.clear()

def action_line():
    cx, cy = S("cursor_x"), S("cursor_y")
    start  = S("line_start")

    if start is None:
        SET("line_start", (cx, cy))
        if point_at_cursor() is None and len(points) < MAX_PTS:
            points.append((cx, cy, S("w"), S("h"), S("draw_color")))
    else:
        x0, y0 = start
        x1, y1 = cx, cy
        cw, ch = S("w"), S("h")
        col    = S("draw_color")

        steps_x = (x1 - x0) // cw
        steps_y = (y1 - y0) // ch
        n       = max(abs(steps_x), abs(steps_y))

        if n == 0:
            SET("line_start", None)
            return

        # Build candidate points first
        candidates = []
        for i in range(n + 1):
            px = x0 + round(steps_x * i / n) * cw
            py = y0 + round(steps_y * i / n) * ch
            if 0 <= px <= SCREEN_W - cw and 0 <= py <= CANVAS_H - ch - 1:
                exists = any(p[0]==px and p[1]==py and p[2]==cw and p[3]==ch for p in points)
                if not exists:
                    candidates.append((px, py, cw, ch, col))

        remaining = MAX_PTS - len(points)
        if len(candidates) > remaining:
            info("Not enough points left! (%d needed, %d left)" % (len(candidates), remaining))
            SET("line_start", None)
            return

        for pt in candidates:
            if len(points) < MAX_PTS:
                points.append(pt)

        SET("line_start", None)

def action_fill():
    cx, cy = S("cursor_x"), S("cursor_y")
    cw, ch = S("w"), S("h")
    col    = S("draw_color")

    occupied = {}
    for p in points:
        if p[2] == cw and p[3] == ch:
            occupied[(p[0], p[1])] = p[4]

    target_color = occupied.get((cx, cy), None)
    if target_color == col:
        return

    queue   = [(cx, cy)]
    visited = {(cx, cy)}
    to_add  = []

    while queue:
        x, y = queue.pop(0)
        if occupied.get((x, y), None) != target_color:
            continue
        to_add.append((x, y))
        for nx, ny in [(x+cw, y), (x-cw, y), (x, y+ch), (x, y-ch)]:
            if (nx, ny) not in visited:
                if 0 <= nx <= SCREEN_W - cw and 0 <= ny <= CANVAS_H - ch - 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        if len(to_add) >= MAX_PTS:
            break

    # Count truly new points (existing ones in fill_set are replaced, not added)
    fill_set       = set(to_add)
    existing_count = sum(1 for p in points if (p[0], p[1]) in fill_set and p[2] == cw and p[3] == ch)
    new_pts_needed = len(to_add) - existing_count
    remaining      = MAX_PTS - len(points)

    if new_pts_needed > remaining:
        info("Not enough points left! (%d needed, %d left)" % (new_pts_needed, remaining))
        return

    points[:] = [p for p in points if (p[0], p[1]) not in fill_set or p[2] != cw or p[3] != ch]
    for x, y in to_add:
        if len(points) < MAX_PTS:
            points.append((x, y, cw, ch, col))

def cycle_mode(direction):
    idx = MODES_LIST.index(S("mode"))
    SET("mode", MODES_LIST[(idx + direction) % len(MODES_LIST)])
    SET("line_start", None)

# Cursor movement
def move_cursor(dx, dy):
    cx = max(0, min(S("cursor_x") + dx * S("w"), SCREEN_W - S("w")))
    cy = max(0, min(S("cursor_y") + dy * S("h"), CANVAS_H - S("h") - 1))
    SET("cursor_x", cx)
    SET("cursor_y", cy)

# Menus
def menu_main():
    options = ["Scale", "Color", "Background", "Mode", "Clear"]
    sel     = 0
    n       = len(options)
    menu_y  = [40 + i * 30 for i in range(n)]

    while True:
        kandinsky.fill_rect(0, 0, SCREEN_W, SCREEN_H, (30, 30, 30))
        kandinsky.fill_rect(0, 0, 165, SCREEN_H, (50, 50, 50))
        kandinsky.draw_string("OPTIONS", 18, 14, (255, 220, 0), (50, 50, 50))

        for i, opt in enumerate(options):
            active = (i == sel)
            if active:
                if i == 4: bg = (180, 50, 50)
                else:      bg = (0, 120, 220)
            else:
                bg = (50, 50, 50)
            kandinsky.fill_rect(8, menu_y[i] - 4, 148, 26, bg)
            kandinsky.draw_string(opt, 16, menu_y[i], (255, 255, 255), bg)

        while True:
            if keydown(KEY_DOWN): sel = (sel+1) % n; time.sleep(TTC); break
            if keydown(KEY_UP):   sel = (sel-1) % n; time.sleep(TTC); break
            if keydown(KEY_OK):   time.sleep(TTC); return sel
            if keydown(KEY_BACKSPACE) or keydown(KEY_TOOLBOX):
                time.sleep(TTC); return None
            time.sleep(0.05)

def menu_scale():
    taille = S("w")
    done   = False
    while not done:
        kandinsky.fill_rect(0, 0, SCREEN_W, SCREEN_H, (30, 30, 30))
        kandinsky.draw_string("SCALE", 118, 14, (255, 220, 0), (30, 30, 30))
        kandinsky.fill_rect(60,  80, 26, 26, (60, 60, 60))
        kandinsky.draw_string("<", 67, 84, (255, 255, 255), (60, 60, 60))
        kandinsky.fill_rect(100, 80, 80, 26, (60, 60, 60))
        kandinsky.draw_string(str(taille), 132, 84, (255, 220, 0), (60, 60, 60))
        kandinsky.fill_rect(194, 80, 26, 26, (60, 60, 60))
        kandinsky.draw_string(">", 200, 84, (255, 255, 255), (60, 60, 60))
        px = (SCREEN_W - taille) // 2
        kandinsky.fill_rect(px, 130, taille, taille, S("draw_color"))
        kandinsky.draw_string("OK=confirm  BACK=cancel", 30, 195, (120, 120, 120), (30, 30, 30))
        while True:
            if keydown(KEY_LEFT):
                if taille > TAILLE_MIN: taille -= 1
                time.sleep(TTC); break
            if keydown(KEY_RIGHT):
                if taille < TAILLE_MAX: taille += 1
                time.sleep(TTC); break
            if keydown(KEY_OK):
                SET("w", taille); SET("h", taille)
                time.sleep(TTC); done = True; break
            if keydown(KEY_BACKSPACE):
                time.sleep(TTC); done = True; break
            time.sleep(0.05)

def menu_mode():
    modes  = ["draw", "erase", "line", "fill", "pipette"]
    labels = ["Draw    - draw",
              "Erase   - erase",
              "Line    - line",
              "Fill    - fill",
              "Pipette - color"]
    sel    = modes.index(S("mode")) if S("mode") in modes else 0
    n      = len(modes)
    menu_y = [36 + i * 30 for i in range(n)]

    while True:
        kandinsky.fill_rect(0, 0, SCREEN_W, SCREEN_H, (30, 30, 30))
        kandinsky.fill_rect(0, 0, SCREEN_W, 28, (50, 50, 50))
        kandinsky.draw_string("MODE", 100, 8, (255, 220, 0), (50, 50, 50))
        kandinsky.draw_string("4=prev  6=next", 170, 8, (130, 130, 130), (50, 50, 50))

        for i, lbl in enumerate(labels):
            active = (i == sel)
            col    = MODE_COLORS[modes[i]]
            bg     = col if active else (45, 45, 45)
            fg     = (0, 0, 0) if active else (190, 190, 190)
            kandinsky.fill_rect(10, menu_y[i] - 2, SCREEN_W - 20, 24, bg)
            kandinsky.draw_string(lbl, 16, menu_y[i], fg, bg)

        while True:
            if keydown(KEY_DOWN): sel = (sel+1) % n; time.sleep(TTC); break
            if keydown(KEY_UP):   sel = (sel-1) % n; time.sleep(TTC); break
            if keydown(KEY_OK):
                SET("mode", modes[sel]); SET("line_start", None)
                time.sleep(TTC); return
            if keydown(KEY_BACKSPACE):
                time.sleep(TTC); return
            time.sleep(0.05)

def menu_color(is_bg=False):
    n_pal     = len(color_choices)
    pal       = 0
    idx       = 0
    cw        = 26
    vis       = (SCREEN_W - 30) // cw
    first_vis = 0
    done      = False

    while pal < n_pal and len(color_choices[pal]) == 0:
        pal += 1
    if pal == n_pal:
        return

    while not done:
        colors = color_choices[pal]
        nb     = len(colors)
        idx    = min(idx, nb - 1) if nb > 0 else 0

        kandinsky.fill_rect(0, 0, SCREEN_W, SCREEN_H, S("bg_color"))
        draw_canvas()
        kandinsky.fill_rect(0, 0, SCREEN_W, 78, (50, 50, 50))
        title = "BACKGROUND" if is_bg else "COLOR"
        kandinsky.draw_string(title, 100, 8, (255, 220, 0), (50, 50, 50))
        kandinsky.draw_string("%d/%d" % (pal+1, n_pal), 272, 8, (160, 160, 160), (50, 50, 50))

        if nb > 0:
            if idx < first_vis: first_vis = idx
            elif idx > first_vis + vis - 1: first_vis = idx - vis + 1
            first_vis = max(0, min(first_vis, max(0, nb - vis)))

            for d in range(vis):
                ci = first_vis + d
                if ci >= nb: break
                x = 30 + d * cw
                kandinsky.fill_rect(x, 42, 20, 20, colors[ci])
                if ci == idx:
                    kandinsky.fill_rect(x - 1, 40, 22, 2, (255, 80, 80))
                    kandinsky.fill_rect(x - 1, 62, 22, 2, (255, 80, 80))

            if not is_bg:
                kandinsky.draw_string("Preview:", 108, 110, (180, 180, 180), S("bg_color"))
                kandinsky.fill_rect(128, 126, 64, 64, colors[idx])

        au = (100, 100, 255) if pal > 0         else (70, 70, 70)
        ad = (100, 100, 255) if pal < n_pal - 1 else (70, 70, 70)
        kandinsky.draw_string("^", 6,  8, au, (50, 50, 50))
        kandinsky.draw_string("v", 6, 22, ad, (50, 50, 50))

        while True:
            if nb > 0 and keydown(KEY_LEFT):
                idx = (idx - 1) % nb
                if is_bg: SET("bg_color", colors[idx])
                time.sleep(0.15); break
            if nb > 0 and keydown(KEY_RIGHT):
                idx = (idx + 1) % nb
                if is_bg: SET("bg_color", colors[idx])
                time.sleep(0.15); break
            if n_pal > 1 and keydown(KEY_UP):
                prev = pal
                while True:
                    pal = (pal - 1) % n_pal
                    if len(color_choices[pal]) > 0 or pal == prev: break
                nb = len(color_choices[pal])
                idx = min(idx, nb-1) if nb > 0 else 0
                time.sleep(0.15); break
            if n_pal > 1 and keydown(KEY_DOWN):
                prev = pal
                while True:
                    pal = (pal + 1) % n_pal
                    if len(color_choices[pal]) > 0 or pal == prev: break
                nb = len(color_choices[pal])
                idx = min(idx, nb-1) if nb > 0 else 0
                time.sleep(0.15); break
            if nb > 0 and keydown(KEY_OK):
                if is_bg: SET("bg_color", colors[idx])
                else:     SET("draw_color", colors[idx])
                time.sleep(0.15); done = True; break
            if keydown(KEY_BACKSPACE):
                time.sleep(0.15); done = True; break
            time.sleep(0.05)

# Main loop
refresh()
time.sleep(0.1)

while S("running"):

    mode = S("mode")

    # OK: action according to mode
    if keydown(KEY_OK):
        if   mode == "draw"   : action_draw()
        elif mode == "erase"  : action_erase()
        elif mode == "pipette": action_pipette()
        elif mode == "line"   : action_line()
        elif mode == "fill"   : action_fill()
        refresh()
        time.sleep(TTC)

    # BACKSPACE: erase / cancel line
    if keydown(KEY_BACKSPACE):
        if mode == "line" and S("line_start") is not None:
            SET("line_start", None)
        else:
            action_erase()
        refresh()
        time.sleep(TTC)

    # Movement
    if keydown(KEY_RIGHT): move_cursor( 1,  0); refresh(); time.sleep(TTC)
    if keydown(KEY_LEFT):  move_cursor(-1,  0); refresh(); time.sleep(TTC)
    if keydown(KEY_UP):    move_cursor( 0, -1); refresh(); time.sleep(TTC)
    if keydown(KEY_DOWN):  move_cursor( 0,  1); refresh(); time.sleep(TTC)

    # SHIFT: toggle draw <-> erase
    if keydown(KEY_SHIFT):
        SET("mode", "erase" if mode == "draw" else "draw")
        SET("line_start", None)
        refresh()
        time.sleep(TTC)

    # 4 / 6: cycle mode
    if keydown(KEY_FOUR): cycle_mode(-1); refresh(); time.sleep(TTC)
    if keydown(KEY_SIX):  cycle_mode( 1); refresh(); time.sleep(TTC)

    # TOOLBOX: main menu
    if keydown(KEY_TOOLBOX):
        time.sleep(TTC)
        opt = menu_main()
        if   opt == 0: menu_scale()
        elif opt == 1: menu_color(is_bg=False)
        elif opt == 2: menu_color(is_bg=True)
        elif opt == 3: menu_mode()
        elif opt == 4: action_clear()
        refresh()
        time.sleep(TTC)

    # HOME: quit
    if keydown(KEY_HOME):
        time.sleep(TTC)
        if confirm_dialog("Quit?"):
            SET("running", False)
            kandinsky.fill_rect(0, 0, SCREEN_W, SCREEN_H, (30, 30, 30))
            kandinsky.draw_string("Bye! Press BACK", 60, 100, (255, 220, 0), (30, 30, 30))
        else:
            refresh()
        time.sleep(0.2)

    time.sleep(0.02)