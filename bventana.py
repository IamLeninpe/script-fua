import time
import pygetwindow as gw
import keyboard
from tkinter import messagebox

def windowsE(target_tab):
    chrome_windows = [win for win in gw.getWindowsWithTitle("Google Chrome")]

    if not chrome_windows:
        messagebox.showerror("Error", "No se encontró una ventana de Chrome.")
        return False

    chrome_window = chrome_windows[0]
    chrome_window.activate()
    time.sleep(1)

    for _ in range(20):
        if target_tab in chrome_window.title:
            print("Pestaña encontrada y activada.")
            return True
        else:
            keyboard.press_and_release("ctrl+tab")
            time.sleep(0.5)
    
    messagebox.showerror("Error", "No se encontró la pestaña especificada.")
    return False