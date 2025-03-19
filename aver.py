import time
import pygetwindow as gw
import pyautogui
import keyboard

target_tab = "ARFSIS-WEB"
fecha = "07/03/2025"  

chrome_windows = [win for win in gw.getWindowsWithTitle("Google Chrome")]

if not chrome_windows:
    print("No se encontró una ventana de Chrome.")
else:
    chrome_window = chrome_windows[0]
    chrome_window.activate()
    time.sleep(1)  

    for _ in range(20):
        if target_tab in chrome_window.title:
            print("Pestaña encontrada y activada.")
            break
        else:
            keyboard.press_and_release("ctrl+tab")  
            time.sleep(0.5)  
    else:
        print("No se encontró la pestaña especificada.")

    time.sleep(0.5)
    pyautogui.typewrite(fecha)
    print(f"Fecha '{fecha}' escrita en el formulario.")