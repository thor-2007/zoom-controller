import tkinter as tk
import keyboard
import pyautogui
import time
import threading



def move_mouse_center():
    width, height = pyautogui.size()
    pyautogui.moveTo(width // 2, height // 2)

def zoom_in(steps=1):
    move_mouse_center()
    for _ in range(steps):
        keyboard.press('windows')
        keyboard.press('+')
        time.sleep(0.05)
        keyboard.release('+')
        keyboard.release('windows')
        time.sleep(0.1)

def zoom_out(steps=1):
    move_mouse_center()
    for _ in range(steps):
        keyboard.press('windows')
        keyboard.press('-')
        time.sleep(0.05)
        keyboard.release('-')
        keyboard.release('windows')
        time.sleep(0.1)

class ZoomApp:
    def __init__(self, root):
        self.root = root
        root.title("Zoom Control Thor A. Ånderå")
        root.geometry("400x500")

        self.zoom_steps = tk.IntVar(value=1)
        self.zoomed_in = False
        self.running = False

        tk.Label(root, text="Zoom Kontroll", font=("Arial", 17)).pack(pady=20)

        tk.Label(root, text="Choose zoom-level:", font=("Arial", 12)).pack(pady=10)

        tk.Radiobutton(root, text="1 level (200%)", variable=self.zoom_steps, value=1, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="2 level (300%)", variable=self.zoom_steps, value=2, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="3 level (400%)", variable=self.zoom_steps, value=3, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="4 level (500%)", variable=self.zoom_steps, value=4, font=("Arial", 12)).pack()

        # Valideringsfunksjon som tillater bokstav ELLER tall, maks ett tegn
        def validate_key_input(P):
            if len(P) == 0:
                return True  # tillat tomt for sletting
            if len(P) > 1:
                return False  # maks ett tegn
            return P.isalnum()  # bokstav eller tall

        vcmd = (root.register(validate_key_input), '%P')

        frame_key = tk.Frame(root)
        frame_key.pack(pady=10)
        tk.Label(frame_key, text="Choose hotkey:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.key_entry = tk.Entry(frame_key, width=3, font=("Arial", 12), validate='key', validatecommand=vcmd)
        self.key_entry.pack(side=tk.LEFT)
        self.key_entry.insert(0, 'z')  # standard

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.start_btn = tk.Button(button_frame, text="Start", command=self.start_zoom, font=("Arial", 14))
        self.stop_btn = tk.Button(button_frame, text="Stop", command=self.stop_zoom, font=("Arial", 14), state='disabled')

        self.start_btn.grid(row=0, column=0, padx=10)
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def start_zoom(self):
        if self.running:
            return
        self.zoom_key = self.key_entry.get().strip().lower()
        if len(self.zoom_key) != 1 or not self.zoom_key.isalnum():
            self.status_label.config(text="Please enter one valid letter or number for zoom key.")
            return

        self.running = True
        self.status_label.config(text=f"Program running... Hold '{self.zoom_key}' for zooming inn")
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')

        self.thread = threading.Thread(target=self.zoom_loop, daemon=True)
        self.thread.start()

    def stop_zoom(self):
        self.running = False
        self.zoomed_in = False
        self.status_label.config(text="Program stopped.")
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')

    def zoom_loop(self):
        while self.running:
            if keyboard.is_pressed(self.zoom_key):
                if not self.zoomed_in:
                    zoom_in(self.zoom_steps.get())
                    self.zoomed_in = True
            else:
                if self.zoomed_in:
                    zoom_out(self.zoom_steps.get())
                    self.zoomed_in = False
            time.sleep(0.1)

root = tk.Tk()


app = ZoomApp(root)
root.mainloop()
