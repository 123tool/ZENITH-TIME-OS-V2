import time
import threading
from datetime import datetime, timedelta
from core.fullscreen import FullScreenApp
from core.sounds import beep

class AlarmSystem(FullScreenApp):
    def __init__(self, theme_name="matrix_green"):
        super().__init__(theme_name)
        self.alarms = []
        self.current_input = ""
        self.setting = False
        self.triggered = False

    def update(self):
        now = datetime.now().strftime("%H:%M")
        if now in self.alarms and not self.triggered:
            self.triggered = True
            threading.Thread(target=self.alert_loop, daemon=True).start()

    def alert_loop(self):
        while self.triggered:
            beep()
            time.sleep(0.5)

    def draw(self):
        h, w = self.renderer.height, self.renderer.width
        box_w = min(70, w-4)
        box_h = 14
        x = (w - box_w)//2
        y = (h - box_h)//2
        self.renderer.draw_box(x, y, box_w, box_h, title=" ALARM ")

        info = "Set alarm (HH:MM): " + self.current_input
        self.renderer.centered_text(y+2, info)

        alarms_list = f"Active alarms: {', '.join(self.alarms) if self.alarms else 'none'}"
        self.renderer.centered_text(y+4, alarms_list)

        status = "STATUS: Normal"
        if self.triggered:
            status = "STATUS: ALARM! [Enter] to stop"
            # Flashing effect
            if int(time.time() * 2) % 2 == 0:
                self.renderer.draw_box(x, y, box_w, box_h, title=" ALARM! ", border_color="red")
        self.renderer.centered_text(y+6, status)

        footer = "[ Q ] Back | [ A ] Add | [ D ] Delete all"
        self.renderer.centered_text(h-2, footer)

    def handle_key(self, key):
        if key and key.lower() == 'q':
            self.running = False
            self.triggered = False
        elif key and key == 'a' and not self.setting:
            self.setting = True
            self.current_input = ""
        elif self.setting:
            if key and key.isdigit() or key in (':', ':'):
                if len(self.current_input) < 5:
                    self.current_input += key
            elif key and key.name == 'KEY_ENTER':
                if len(self.current_input) == 5:
                    self.alarms.append(self.current_input)
                self.setting = False
                self.current_input = ""
            elif key and key.name == 'KEY_DELETE':
                self.current_input = self.current_input[:-1]
        elif key and key == 'd':
            self.alarms.clear()
        elif key and key.name == 'KEY_ENTER' and self.triggered:
            self.triggered = False
