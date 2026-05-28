import sys
import time
from blessed import Terminal
from core.renderer import Renderer
from core.themes import get_theme
from core.controls import handle_sigint
from modules.clock import DigitalClock
from modules.alarm import AlarmSystem
from modules.stopwatch import Stopwatch
from modules.timer import CountdownTimer

def startup_animation(term):
    """Boot sequence"""
    renderer = Renderer(term, "matrix_green")
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        for step in [
            "[ OK ] Initializing Renderer",
            "[ OK ] Loading Themes",
            "[ OK ] Starting Animation Engine",
            "[ OK ] Fullscreen Mode Enabled"
        ]:
            renderer.clear()
            renderer.centered_text(term.height//2 - 2, "TERMINAL TOOLS SUITE")
            renderer.centered_text(term.height//2, step)
            time.sleep(0.4)
        time.sleep(0.5)

def main_menu():
    term = Terminal()
    signal.signal(signal.SIGINT, lambda sig, frame: handle_sigint(term))
    theme_name = "matrix_green"
    renderer = Renderer(term, theme_name)
    items = [
        "Digital Clock",
        "Alarm",
        "Stopwatch",
        "Timer",
        "Settings",
        "Themes",
        "Credits",
        "Exit"
    ]
    current = 0

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            renderer.clear()
            h, w = term.height, term.width
            box_w = min(50, w-4)
            box_h = len(items) + 4
            x = (w - box_w)//2
            y = (h - box_h)//2
            renderer.draw_box(x, y, box_w, box_h, title=" MAIN MENU ")

            for i, item in enumerate(items):
                if i == current:
                    prefix = "▶ "
                    color = renderer.theme["accent"]
                else:
                    prefix = "  "
                    color = renderer.theme["fg"]
                line = f"{prefix}{item}"
                renderer.centered_text(y+2+i, f"{getattr(term, color)}{line}{term.normal}")

            footer = "[ ↑↓ ] Navigate | [ Enter ] Select | [ Q ] Quit"
            renderer.centered_text(h-2, footer)

            key = term.inkey()
            if key.name == 'KEY_UP':
                current = (current - 1) % len(items)
            elif key.name == 'KEY_DOWN':
                current = (current + 1) % len(items)
            elif key.name == 'KEY_ENTER':
                choice = items[current]
                if choice == "Exit":
                    break
                elif choice == "Digital Clock":
                    DigitalClock(theme_name).run()
                elif choice == "Alarm":
                    AlarmSystem(theme_name).run()
                elif choice == "Stopwatch":
                    Stopwatch(theme_name).run()
                elif choice == "Timer":
                    CountdownTimer(theme_name).run()
                elif choice == "Themes":
                    # Sederhana: ganti tema
                    themes = ["matrix_green","cyberpunk_neon","minimal_white","retro_amber",
                              "rgb_dynamic","vaporwave","hacker_red","deep_blue"]
                    idx = themes.index(theme_name) if theme_name in themes else 0
                    theme_name = themes[(idx+1) % len(themes)]
                    renderer = Renderer(term, theme_name)
                elif choice == "Settings":
                    pass  # Opsi lanjutan
                elif choice == "Credits":
                    pass  # Bisa ditambahkan
            elif key.lower() == 'q':
                break

    print(term.clear + term.normal)
    sys.exit()

if __name__ == "__main__":
    # Startup animation
    startup_animation(Terminal())
    main_menu()
