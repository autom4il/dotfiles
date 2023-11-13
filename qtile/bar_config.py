# Qtile bar config
from libqtile import bar
from libqtile.config import Screen
from widgets_config import init_widgets

# Bar settings 
customize_bar = {
    "size": 30,
    "background": "#028690",
}


# Set wallpaper
customize_wallpaper = {
    "wallpaper": "~/Pictures/arch-wallpaper.png",
    "wallpaper_mode": "fill",
}

def init_screens():
    screens = [
        Screen(
            top=bar.Bar(
                init_widgets(),
                **customize_bar
            ),
            **customize_wallpaper
        ),
    ]
    return screens
