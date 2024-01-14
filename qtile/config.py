# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from colors import widget_c, monadtall_c, floating_c, maxstack_c

dgroups_key_binder = simple_key_binder("mod4")

mod = "mod4"
terminal = guess_terminal()

browser = "firefox"
physlock = "physlock -p 'Locked!'"

follow_mouse_focus = False

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
        Group("1", layout = "monadtall", label = "", screen_affinity = 0),
        Group("2", layout = "monadtall", label = "", screen_affinity = 0),
        Group("3", layout = "max", label = "", screen_affinity = 0),
        Group("4", layout = "monadtall", label = "", screen_affinity = 0),
        Group("5", layout = "monadtall", label = "", screen_affinity = 1),
        Group("6", layout = "monadtall", label = "", screen_affinity = 1),
        Group("7", layout = "monadtall", label = "", screen_affinity = 1),
    ]

def init_layouts():
    layouts = [
        layout.MonadTall(
            border_focus = monadtall_c[0],
            border_normal = monadtall_c[1],
            margin = 8,
            border_width = 2,
        ),
        layout.Floating(
            border_focus = floating_c[0],
            border_normal = floating_c[1],
            border_width = 2,
        ),
        layout.Max(
            border_focus = maxstack_c[0],
            border_normal = maxstack_c[1],
            margin = 8,
            border_width = 2,
        ),
    ]
    return layouts

def init_widgets_list():
    groups = ['1', '2', '3', '4', '5', '6', '7']
    primary_widgets_list = [
       widget.GroupBox(
            font="hack", 
            fontsize = 18, 
            active = widget_c[0], 
            inactive = widget_c[1], 
            background = widget_c[2],
            highlight_color = widget_c[3],
            this_current_screen_border = widget_c[4],
            margin_y = 3, 
            margin_x = 5, 
            padding_y = 5, 
            padding_x = 12,
            highlight_method = "line", 
            visible_groups = groups[0:4],
       ),
       widget.TextBox(
            font = "JetBrainsMono Nerd Font Mono",
            text = "",
            padding = 0,
            fontsize = 33,
            foreground = widget_c[5],
            background = widget_c[6],
        ),
        widget.CurrentLayoutIcon(
            font = "JetBrainsMono Nerd Font Mono",
            scale = 0.6,
            background = widget_c[7],
        ),
        widget.CurrentLayout(
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = "15",
            padding = 5,
            background = widget_c[7],
        ),
        widget.TextBox(
            text = "",
            fontsize = 33,
            padding = 0,
            foreground = widget_c[8],
            background = widget_c[9],
        ),
        widget.Spacer(
            bar.STRETCH,
        ),
        widget.TextBox(
            text = "",
            fontsize = 33,
            padding = 0,
            foreground = widget_c[10],
            background = widget_c[11],
        ),
        widget.Systray(
            icon_size = 130,
            padding = 20,
            background = widget_c[12]
            
        ),
        widget.TextBox(
            text = "",
            fontsize = 33,
            padding = 0,
            foreground = widget_c[13],
            background = widget_c[14],
        ),
        widget.CPU(
            format = " {freq_current}GHz {load_percent}% ",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
        ),
        widget.Memory(
            format = "  {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} ",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
        ),
        widget.Wlan(
            format = "{essid} {percent:2.0%}",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
            disconnected_message = "Wifi Disabled"
        ),
        widget.Spacer(
            length = 10,
        ),
        widget.Battery(
            charge_char = '',
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
            update_interval = 1,
        ),
        widget.Clock(
            format = "%I:%M %p ",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 15,
            foreground = widget_c[15],
            background = widget_c[16],
        ),
        widget.Clock(
            format = "%a %Y-%m-%d",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
            foreground = widget_c[15],
            backgroung = widget_c[16],
        ),
    ]

    secondary_widgets_list = [
          widget.GroupBox(
            font="hack",
            fontsize = 18,
            active = widget_c[0],
            inactive = widget_c[1],
            background = widget_c[2],
            highlight_color = widget_c[3],
            this_current_screen_border = widget_c[4],
            margin_y = 3,
            margin_x = 5,
            padding_y = 5,
            padding_x = 12,
            highlight_method = "line",
            visible_groups = groups[4:7],
        ),
        widget.TextBox(
            font = "JetBrainsMono Nerd Font Mono",
            text = "",
            padding = 0,
            fontsize = 33,
            foreground = widget_c[5],
            background = widget_c[6],
        ),
        widget.CurrentLayoutIcon(
            font = "JetBrainsMono Nerd Font Mono",
            scale = 0.6,
            background = widget_c[7],
        ),
        widget.CurrentLayout(
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = "15",
            padding = 5,
            background = widget_c[7],
        ),
        widget.TextBox(
            text = "",
            fontsize = 33,
            padding = 0,
            foreground = widget_c[8],
            background = widget_c[9],
        ),
    ]
    widgets = primary_widgets_list, secondary_widgets_list
    return widgets

def init_screens():
    return [
        Screen(
               top = bar.Bar(widgets=widgets_list[0], size=30),
               wallpaper = "~/Pictures/arch_wallpaper.png",
               wallpaper_mode = "fill"
        ),
        Screen(
               top = bar.Bar(widgets=widgets_list[1], size=30),
               wallpaper = "~/Pictures/arch_wallpaper.png",
               wallpaper_mode = "fill"
        ),
    ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    layouts = init_layouts()

mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
            start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
            start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
    ]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])
