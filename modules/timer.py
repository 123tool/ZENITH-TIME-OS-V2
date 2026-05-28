import time
from core.fullscreen import FullScreenApp

class CountdownTimer(FullScreenApp):
    def __init__(self, theme_name="matrix_green"):
        super().__init__(theme_name)
        self.duration = 60  # detik default
        self.remaining = self.duration
        self.running = False
        self.start_time = None

    def update(self):
        if self.running:
            elapsed = time.perf_counter() - self.start_time
            self.remaining = max(0, self.duration - elapsed)
            if self.remaining <= 0:
                self.running = False
                self.remaining = 0
                # Alert
                from core.sounds import beep
                beep()

    def draw(self):
        h, w = self.renderer.height, self.renderer.width
        box_w = min(60, w-4)
        box_h = 14
        x = (w - box_w)//2
        y = (h - box_h)//2
        self.renderer.draw_box(x, y, box_w, box_h, title=" COUNTDOWN TIMER ")

        # Progress bar
        perc = 1 - (self.remaining / self.duration) if self.duration > 0 else 1
        bar_len = 40
        filled = int(bar_len * perc)
        bar = "█" * filled + "░" * (bar_len - filled)
        bar_color = self.renderer.theme["accent"]
        bar_text = f"{bar_color}{bar}{self.renderer.term.normal}"
        self.renderer.centered_text(y+3, f"[{bar_text}] {int(perc*100)}%")

        mins, secs = divmod(int(self.remaining), 60)
        time_str = f"{mins:02}:{secs:02}"
        self.renderer.centered_text(y+5, time_str)

        status = "▶ RUNNING" if self.running else "⏸ READY"
        self.renderer.centered_text(y+7, status)

        # Input for new duration
        self.renderer.centered_text(y+9, "Press [ S ] to set duration (seconds)")
        footer = "[ Q ] Back | [ Space ] Start | [ R ] Reset | [ S ] Set"
        self.renderer.centered_text(h-2, footer)

    def handle_key(self, key):
        if key and key.lower() == 'q':
            self.running = False
        elif key and key == ' ':
            if not self.running:
                self.start_time = time.perf_counter()
                self.running = True
            else:
                self.running = False
        elif key and key.lower() == 'r':
            self.running = False
            self.remaining = self.duration
        elif key and key.lower() == 's':
            # Simpel: minta input di terminal? Tidak bisa di fullscreen, kita set default atau siklus
            self.duration = (self.duration + 30) % 300 + 30  # 30,60,90,...,270
            self.remaining = self.duration
