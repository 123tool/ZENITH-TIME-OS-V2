import time
from datetime import datetime
from core.fullscreen import FullScreenApp
from core.animation import AnimationEngine

class DigitalClock(FullScreenApp):
    def __init__(self, theme_name="matrix_green", mode="24"):
        super().__init__(theme_name)
        self.mode = mode
        self.anim = AnimationEngine(self.renderer)
        self.last_time = ""

    def update(self):
        now = datetime.now()
        if self.mode == "12":
            hour = now.strftime("%I")
            ampm = now.strftime("%p")
            self.time_str = f"{hour}:{now.strftime('%M:%S')} {ampm}"
        else:
            self.time_str = now.strftime("%H:%M:%S")
        self.date_str = now.strftime("%A, %d %B %Y")
        # Animasi blink untuk separator
        if now.second % 2 == 0:
            self.separator = ":"
        else:
            self.separator = " "

    def draw(self):
        h, w = self.renderer.height, self.renderer.width
        # Kotak tengah
        box_w = min(60, w-4)
        box_h = 10
        x = (w - box_w)//2
        y = (h - box_h)//2
        theme = self.renderer.theme
        accent = theme["accent"]
        self.renderer.draw_box(x, y, box_w, box_h, title=" DIGITAL CLOCK ", border_color=accent)

        # Tampilkan waktu dengan efek glow
        glow = self.anim.glow_pulse()
        # Teks waktu di tengah
        time_row = y + 3
        self.renderer.centered_text(time_row, self.time_str)
        # Date
        date_row = y + 5
        self.renderer.centered_text(date_row, self.date_str)
        # Info mode
        info = f"Mode: {self.mode}H | Theme: {self.renderer.theme}"
        self.renderer.centered_text(y+7, info)
        # Petunjuk bawah
        footer = "[ Q ] Back to Menu"
        self.renderer.centered_text(h-2, footer)

    def handle_key(self, key):
        if key and key.lower() == 'q':
            self.running = False
        elif key and key.lower() == 'm':
            self.mode = "12" if self.mode == "24" else "24"
