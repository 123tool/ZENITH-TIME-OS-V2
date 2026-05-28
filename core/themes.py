THEMES = {
    "matrix_green": {"fg": "green", "bg": "black", "accent": "bright_green", "border": "green"},
    "cyberpunk_neon": {"fg": "cyan", "bg": "black", "accent": "bright_magenta", "border": "bright_cyan"},
    "minimal_white": {"fg": "white", "bg": "black", "accent": "bright_white", "border": "white"},
    "retro_amber": {"fg": "yellow", "bg": "black", "accent": "bright_yellow", "border": "yellow"},
    "rgb_dynamic": {"fg": "white", "bg": "black", "accent": "rainbow", "border": "rainbow"},
    "vaporwave": {"fg": "bright_magenta", "bg": "black", "accent": "cyan", "border": "bright_magenta"},
    "hacker_red": {"fg": "red", "bg": "black", "accent": "bright_red", "border": "red"},
    "deep_blue": {"fg": "blue", "bg": "black", "accent": "bright_blue", "border": "blue"},
}

def get_theme(name):
    return THEMES.get(name, THEMES["matrix_green"])
