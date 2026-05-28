from blessed import Terminal
import signal
from .renderer import Renderer
from .controls import handle_sigint

class FullScreenApp:
    def __init__(self, theme_name="matrix_green"):
        self.term = Terminal()
        self.renderer = Renderer(self.term, theme_name)
        signal.signal(signal.SIGINT, lambda sig, frame: handle_sigint(self.term))
        self.running = True

    def run(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            self.main_loop()

    def main_loop(self):
        while self.running:
            self.renderer.clear()
            # Override di subclass
            self.update()
            self.draw()
            key = self.term.inkey(timeout=0.05)
            self.handle_key(key)
            if key and key.lower() == 'q':
                self.running = False

    def update(self): pass
    def draw(self): pass
    def handle_key(self, key): pass
