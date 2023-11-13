# Qtile main config
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
from libqtile.utils import guess_terminal

# Import other libraries
from bar_config import init_screens
from layouts_config import init_layouts
import os
import subprocess

mod = "mod4"
dgroups_key_binder = simple_key_binder("mod4")
terminal = guess_terminal()

browser = "firefox"
physlock = "physlock -p 'Locked!'"

# Windows behaviour
follow_mouse_focus = True

keys = [
    # Applications
    Key([mod], "Return", lazy.spawn(terminal), desc = "Launch Alacritty"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc = "Launch Rofi"),
    Key([mod], "b", lazy.spawn(browser), desc = "Launch Firefox"),

    # Lock session
    Key([mod, "shift"], "l", lazy.spawn(physlock), desc = "Launch Physlock"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Change between layouts
    Key([mod], "Tab", lazy.next_layout(), desc = "Next layout"),
    
    # Change between windows if using Max layout
    Key([mod], "Right", lazy.layout.next(), desc = "Next window"),
    Key([mod], "Left", lazy.layout.previous(), desc = "Previous windows"),
    ]

# Groups
groups = [
    # MonadTall layout
    Group("1", layout = "monadtall", label = ""),
    Group("2", layout = "monadtall", label = ""),
    Group("3", layout = "max", label = ""),
    Group("4", layout = "monadtall", label = ""),
    Group("5", layout = "monadtall", label = ""),
    ]

# Mouse
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
    ]

# Code specific to running the configuration config.py as the main script or
# imported as "config"

if __name__ in ["config", "__main__"]:
    # Initialize Screens
    screens = init_screens()

    # Initialize layouts
    layouts = init_layouts()

    # Floating window layout
    floating_layout = layouts[1]

#@hook.subscribe.startup_once
#def autostart():
#    home = os.path.expanduser("~")
#    subprocess.Popen([home + "/.config/qtile/autostart.sh"])
