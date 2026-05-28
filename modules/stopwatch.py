import time
from core.fullscreen import FullScreenApp

class Stopwatch(FullScreenApp):
    def __init__(self, theme_name="matrix_green"):
        super().__init__(theme_name)
        self.start_time = None
        self.elapsed = 0.0
        self.running = False
        self.laps = []

    def update(self):
        if self.running:
            self.elapsed = time.perf_counter() - self.start_time + self.paused_elapsed if self.start_time else 0.0
        else:
            self.elapsed = self.paused_elapsed

    def draw(self):
        h, w = self.renderer.height, self.renderer.width
        box_w = min(60, w-4)
        box_h = 16
        x = (w - box_w)//2
        y = (h - box_h)//2
        self.renderer.draw_box(x, y, box_w, box_h, title=" STOPWATCH ")

        # Format waktu
        ms = int(self.elapsed * 1000) % 1000
        secs = int(self.elapsed) % 60
        mins = (int(self.elapsed) // 60) % 60
        hours = int(self.elapsed) // 3600
        time_str = f"{hours:02}:{mins:02}:{secs:02}.{ms:03}"
        self.renderer.centered_text(y+3, time_str)

        status = "▶ RUNNING" if self.running else "⏸ PAUSED"
        self.renderer.centered_text(y+5, status)

        # Laps (3 terakhir)
        if self.laps:
            laps_str = "Laps:\n" + "\n".join(f"  Lap {i}: {lap}" for i, lap in enumerate(self.laps[-3:], 1))
            # Gambar teks multiline
            lines = laps_str.split('\n')
            for i, line in enumerate(lines):
                self.renderer.centered_text(y+7+i, line)
        else:
            self.renderer.centered_text(y+7, "No laps recorded")

        footer = "[ Q ] Back | [ Space ] Start/Pause | [ L ] Lap | [ R ] Reset"
        self.renderer.centered_text(h-2, footer)

    def handle_key(self, key):
        if key and key.lower() == 'q':
            self.running = False
            self.running = False # Stop thread
            self.running = False # ?? Just exit
            self.running = False
            # better: set self.running = False then break loop
        elif key and key == ' ':
            if not self.running:
                self.start_time = time.perf_counter()
                self.running = True
            else:
                self.paused_elapsed = self.elapsed
                self.running = False
        elif key and key.lower() == 'l' and self.running:
            # Format lap
            lap_time = self.elapsed
            ms = int(lap_time * 1000) % 1000
            secs = int(lap_time) % 60
            mins = (int(lap_time) // 60) % 60
            hours = int(lap_time) // 3600
            self.laps.append(f"{hours:02}:{mins:02}:{secs:02}.{ms:03}")
        elif key and key.lower() == 'r':
            self.running = False
            self.start_time = None
            self.elapsed = 0.0
            self.paused_elapsed = 0.0
            self.laps.clear()
