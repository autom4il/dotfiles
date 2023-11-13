# Qtile widgets
from libqtile import widget

def init_widgets():
    widgets = [
        widget.GroupBox(
            font="hack", 
            fontsize = 18, 
            active = "#ffffff", 
            inactive = "#02848e", 
            background = "#000000",
            margin_y = 3, 
            margin_x = 5, 
            padding_y = 5, 
            padding_x = 12,
            highlight_method = "line", 
            highlight_color = "#000000", 
            this_current_screen_border = "#f86b09",
        ),
       widget.TextBox(
            font = "JetBrainsMono Nerd Font Mono",
            text = "",
            padding = 0,
            fontsize = 33,
            background = "#028690",
            foreground = "#000000",
        ),
        widget.CurrentLayoutIcon(
            font = "JetBrainsMono Nerd Font Mono",
            scale = 0.6,
            background = "#028690",
        ),
        widget.Sep(
            linewidth = 0, 
            padding = 1,
        ),
        widget.CurrentLayout(
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = "15",
            padding = 5,
        ),
        widget.TextBox(
            text = "",
            fontsize = 33,
            padding = 0,
            foreground = "#028690",
            background = "#3b4b7a",
        ),
        widget.WindowName(
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 15,
            background = "#3b4b7a",
        ),
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 37,
            foreground = "#028690",
            background = "#3b4b7a",
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
        widget.Volume(
            fmt= "Vol:{}",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
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
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 37,
            foreground = "#000000",
            background = "#028690",
        ),
        widget.Systray(
            icon_size = 20,
            background = "#000000",
        ),
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 37,
            foreground = "#000000",
            background = "#000000",
        ),
        widget.Clock(
            format = "%I:%M %p ",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 15,
            background = "#000000",
            foreground = "#ffffff",
        ),
        widget.Clock(
            format = "%a %Y-%m-%d",
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 16,
            background = "#000000",
            foreground = "#ffffff",
        ),
    ]
    return widgets
