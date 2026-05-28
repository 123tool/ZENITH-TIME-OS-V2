from blessed import Terminal
import time
import math
from .themes import get_theme

class Renderer:
    def __init__(self, term, theme_name="matrix_green"):
        self.term = term
        self.theme = get_theme(theme_name)
        self.width = term.width
        self.height = term.height

    def clear(self):
        print(self.term.home + self.term.clear)

    def draw_box(self, x, y, w, h, title="", border_color=None):
        if border_color is None:
            border_color = self.theme["border"]
        color = getattr(self.term, border_color)
        # Gambar sudut dan garis
        top = f"{color}╔{'═'*(w-2)}╗{self.term.normal}"
        bottom = f"{color}╚{'═'*(w-2)}╝{self.term.normal}"
        mid = f"{color}║{self.term.normal}{' '*(w-2)}{color}║{self.term.normal}"
        with self.term.location(x, y):
            print(top)
        for i in range(1, h-1):
            with self.term.location(x, y+i):
                print(mid)
        with self.term.location(x, y+h-1):
            print(bottom)
        if title:
            title_colored = f"{getattr(self.term, self.theme['accent'])}{title}{self.term.normal}"
            self.centered_text(y, title_colored)

    def centered_text(self, row, text):
        x = max(0, (self.width - len(text)) // 2)
        with self.term.location(x, row):
            print(text)

    def rainbow_text(self, row, text, offset=0):
        colors = [self.term.red, self.term.yellow, self.term.green, self.term.cyan, self.term.blue, self.term.magenta]
        x = max(0, (self.width - len(text)) // 2)
        with self.term.location(x, row):
            for i, ch in enumerate(text):
                if ch != ' ':
                    color = colors[(i + offset) % len(colors)]
                    print(color + ch, end='')
                else:
                    print(' ', end='')
            print(self.term.normal)
