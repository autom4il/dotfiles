# Qtile layouts config

from libqtile import layout

# Layout settings
monadtall = {
    "border_focus": "#2596be",
    "border_normal": "#FFFFFF",
    "margin": 8,
    "border_width": 2,
    }

floating = {
    "border_focus": "#fcc862",
    "border_normal": "#ffffff",
    "border_width": 2,
    }

maxstack = {
    "border_focus": "#2596be",
    "border_normal": "#FFFFFF",
    "margin": 8,
    "border_width": 2,
    }


def init_layouts():
    layouts = [
        layout.MonadTall(**monadtall),
        layout.Floating(**floating),
        layout.Max(**maxstack)
    ]
    return layouts
