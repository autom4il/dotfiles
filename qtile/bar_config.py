# Qtile bar config
from libqtile import bar
from libqtile.config import Screen
from widgets_config import init_widgets

# Bar settings 
primary_screen_bar = {
    "size": 30,
    "background": "#02848e",
}

secondary_screen_bar = {
    "size": 30,
    "background": "#000000",
}

# Set wallpaper
wallpaper = {
    "wallpaper": "~/Pictures/arch-wallpaper.png",
    "wallpaper_mode": "fill",
}

def init_screens():
    screens = [
        Screen(
            top=bar.Bar(
                # This are the primary screen widgets defined in
                # widgets_config.py file
                init_widgets()[0],
                **primary_screen_bar
            ),
            **wallpaper
        ),
        Screen(
            top=bar.Bar(
                # This are the secondary widgets displayed in
                # the second screen and defined at widgets_config.py file
                init_widgets()[1],
                **secondary_screen_bar
            ),
            **wallpaper
        ),
    ]

    return screens

