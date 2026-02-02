selected_color = (0,0,0) # Default color
font_color = (255,255,255) # Default font color

ttc = 0.2 # Time to click

start = 1
shift = False

points = [
] # List of points (You can add your own default points)
cursor_x=170 # Default cursor x position
cursor_y=110 # Default cursor position
cursor_taille_min, cursor_taille_max = 10, 30 # Default cursor size range
w=20 # Default width
h=20 # Default height

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
