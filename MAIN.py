import threading
import tkinter as tk
from pynput import keyboard, mouse

count = 0

def update_label():
    label.config(text=str(count))

def on_press(key):
    global count
    count += 1
    label.after(0, update_label)

def on_click(x, y, button, pressed):
    global count
    if pressed:
        count += 1
        label.after(0, update_label)

# GUI Setup
root = tk.Tk()
root.title("Global Counter")
root.geometry("300x200")
label = tk.Label(root, text="0", font=("Arial", 48))
label.pack(expand=True)

# Run pynput listeners on a separate thread
def start_listeners():
    kb_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_click=on_click)
    kb_listener.start()
    mouse_listener.start()
    kb_listener.join()
    mouse_listener.join()

listener_thread = threading.Thread(target=start_listeners, daemon=True)
listener_thread.start()

root.mainloop()
