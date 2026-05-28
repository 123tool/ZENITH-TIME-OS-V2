import time
import math
from .renderer import Renderer

class AnimationEngine:
    def __init__(self, renderer):
        self.renderer = renderer

    def glow_pulse(self, intensity=1.0):
        # Mengembalikan faktor glow berdasarkan sinus
        return 0.5 + 0.5 * math.sin(time.time() * 3 * intensity)

    def crt_flicker(self):
        return 0.9 + 0.1 * (math.sin(time.time() * 50) > 0.9)

    def draw_scanlines(self, renderer):
        # Overlay scanline dengan karakter transparan atau warna bg
        pass  # bisa ditambahkan
