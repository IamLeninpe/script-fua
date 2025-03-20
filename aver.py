import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
from bventana import windowsE

def buscar_pestana_y_escribir_fecha_y_hora():
    if not windowsE("ARFSIS-WEB"):
        return
    time.sleep(0.5)
    pyautogui.typewrite(entry_fecha.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(entry_hora.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(entry_renipress.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(entry_lote.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(entry_fua.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    for _ in range(6):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.typewrite(entry_dni.get())
    pyautogui.press('tab')
    time.sleep(1.7)
    pyautogui.press('tab')
    time.sleep(1.7)
    pyautogui.press('tab')
    time.sleep(1.7)
    pyautogui.typewrite(entry_etnia.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(entry_cod_presta.get())
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')  # Presiona la tecla Enter (Intro) nuevamente
    time.sleep(1.7)
    pyautogui.press('tab')
    time.sleep(1.7)
    pyautogui.typewrite(entry_dni_prof.get())  # Escribe el DNI del profesional

    messagebox.showinfo("Éxito", "Datos escritos en el formulario.")

def formatear_entrada(event, formato, separador, max_len, siguiente_campo=None):
    texto = event.widget.get()
    if len(texto) > max_len:
        event.widget.delete(max_len, tk.END)
    if len(texto) in formato and texto[-1] != separador:
        event.widget.insert(tk.END, separador)
    if len(texto) == max_len and siguiente_campo:
        siguiente_campo.focus()

root = tk.Tk()
root.title("Automatización de Datos del Formulario")

# Campo Fecha
tk.Label(root, text="Ingrese la fecha (DD/MM):").pack(pady=5)
entry_fecha = tk.Entry(root)
entry_fecha.pack(pady=5)
entry_fecha.focus()
entry_fecha.bind("<KeyRelease>", lambda e: formatear_entrada(e, {2}, "/", 5, entry_hora))

# Campo Hora
tk.Label(root, text="Ingrese la hora (HH:MM):").pack(pady=5)
entry_hora = tk.Entry(root)
entry_hora.pack(pady=5)
entry_hora.bind("<KeyRelease>", lambda e: formatear_entrada(e, {2}, ":", 5, entry_renipress))

# Campo RENIPRESS
tk.Label(root, text="Ingrese el RENIPRESS:").pack(pady=5)
entry_renipress = tk.Entry(root)
entry_renipress.pack(pady=5)
entry_renipress.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8, entry_lote))

# Campo Lote
tk.Label(root, text="Lote").pack(pady=5)
entry_lote = tk.Entry(root)
entry_lote.pack(pady=5)
entry_lote.insert(0, "25")  # Valor por defecto
entry_lote.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8, entry_fua))

# Campo FUA
tk.Label(root, text="Ingrese FUA").pack(pady=5)
entry_fua = tk.Entry(root)
entry_fua.pack(pady=5)
entry_fua.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8, entry_dni))

# Campo DNI
tk.Label(root, text="Ingrese el DNI:").pack(pady=5)
entry_dni = tk.Entry(root)
entry_dni.pack(pady=5)
entry_dni.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8, entry_etnia))

# Campo Etnia
tk.Label(root, text="Etnia").pack(pady=5)
entry_etnia = tk.Entry(root)
entry_etnia.pack(pady=5)
entry_etnia.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8, entry_cod_presta))

# Campo Cod Presta
tk.Label(root, text="Cod Prestación").pack(pady=5)
entry_cod_presta = tk.Entry(root)
entry_cod_presta.pack(pady=5)
entry_cod_presta.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8, entry_dni_prof))

# Campo DNI_PROF
tk.Label(root, text="Ingrese el DNI del Profesional:").pack(pady=5)
entry_dni_prof = tk.Entry(root)
entry_dni_prof.pack(pady=5)
entry_dni_prof.bind("<KeyRelease>", lambda e: formatear_entrada(e, set(), "", 8))

# Botón Ejecutar
tk.Button(root, text="Ejecutar", command=buscar_pestana_y_escribir_fecha_y_hora).pack(pady=20)

root.mainloop()