from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox, Tk, Entry, StringVar
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import ttk
import time

def buscar_y_escribir_datos(fecha, hora, renipres, fua, dni, cod_presta, responsable):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    service = Service("C:/Users/RSY/Desktop/fua-script/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        if "http://192.168.86.210:10088/opensis/arfsisweb/index.jsp#/registrar" not in driver.current_url:
            messagebox.showerror("Error", "La pestaña abierta no tiene la URL esperada.")
            return

        wait = WebDriverWait(driver, 10)

        fecha_input = wait.until(EC.presence_of_element_located((By.ID, "ate_fecatencion")))
        fecha_input.clear()
        fecha_input.send_keys(fecha)
        fecha_input.send_keys(Keys.TAB)

        hora_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[inputid='hora']")))
        hora_input.clear()
        hora_input.send_keys(hora)
        hora_input.send_keys(Keys.TAB)

        renipres_input = wait.until(EC.presence_of_element_located((By.ID, "ate_ideess")))
        renipres_input.clear()
        renipres_input.send_keys(renipres)
        renipres_input.send_keys(Keys.TAB)

        fua_input = wait.until(EC.presence_of_element_located((By.ID, "ate_numregate")))
        fua_input.clear()
        fua_input.send_keys(fua)
        fua_input.send_keys(Keys.TAB)

        dni_input = wait.until(EC.presence_of_element_located((By.ID, "ate_numregafiins")))
        dni_input.clear()
        dni_input.send_keys(dni)
        dni_input.send_keys(Keys.TAB)

        etnia_input = wait.until(EC.presence_of_element_located((By.ID, "ate_idetnia")))
        etnia_input.clear()
        etnia_input.send_keys("58")
        etnia_input.send_keys(Keys.TAB)

        cod_presta_input = wait.until(EC.presence_of_element_located((By.ID, "ate_idservicio")))
        cod_presta_input.clear()
        cod_presta_input.send_keys(cod_presta)

        modalidad_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".p-dropdown-label.p-inputtext.tabindex.p-placeholder")))
        actions = ActionChains(driver)
        actions.move_to_element(modalidad_input).click()
        actions.send_keys(Keys.ENTER).pause(1)
        actions.send_keys(Keys.ARROW_DOWN).pause(1)
        actions.send_keys(Keys.ARROW_DOWN).pause(1) 
        actions.send_keys(Keys.ENTER).perform()

        tipo_doc_responsable = wait.until(EC.presence_of_element_located((By.ID, "tipoDocumentoResponsable")))
        actions = ActionChains(driver)
        actions.move_to_element(tipo_doc_responsable).click()
        actions.send_keys(Keys.ENTER).pause(1)
        actions.send_keys(Keys.ENTER).perform()

        personal_salud_input = wait.until(EC.presence_of_element_located((By.ID, "ate_dnipersonalsalud")))
        personal_salud_input.clear()
        personal_salud_input.send_keys(responsable)
        dni_input.send_keys(Keys.TAB)

        if cod_presta == "022":
            actions.key_down(Keys.CONTROL).send_keys("2").key_up(Keys.CONTROL).perform()
            button_preventivo = wait.until(EC.presence_of_element_located((By.ID, "plusPreventivo")))
            button_preventivo.click()
            preventivo_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.p-inputtext.p-component.p-inputtext-sm.p-invalid.p-inputtext-sm.tabindex.preventivo")))
            preventivo_input.send_keys("407")  
            actions.send_keys(Keys.TAB).perform()

            valor_element = wait.until(EC.presence_of_element_located((By.ID, "valor407-1")))
            actions.move_to_element(valor_element).click().perform()
            actions.send_keys(Keys.ENTER).perform()

        actions.key_down(Keys.CONTROL).send_keys("3").key_up(Keys.CONTROL).perform()

        button_diagnostico = wait.until(EC.presence_of_element_located((By.ID, "buttonDiagnostico")))
        button_diagnostico.click()

        empty_area = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body"))) 
        actions.move_to_element(empty_area).click().perform()

        diagnostico_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.p-inputtext.p-component.p-inputtext-sm.p-invalid.tabindex.diagnostico")))
        diagnostico_input.click()

        diagnostico_value = "Z742"
        if cod_presta == "022":
            diagnostico_value = "Z133"
        diagnostico_input.send_keys(diagnostico_value)
        dni_input.send_keys(Keys.TAB)

        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys("6").key_up(Keys.CONTROL).perform()

        button_diagnostico = wait.until(EC.presence_of_element_located((By.ID, "plusProcedimiento")))
        button_diagnostico.click()

        procedimiento_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.p-inputtext.p-component.p-invalid.p-inputtext-sm.tabindex.procedimiento")))
        procedimiento_input.click()

        procedimiento_value = "99509"
        if cod_presta == "022":
            procedimiento_value = "99402.09"
        procedimiento_input.send_keys(procedimiento_value)
        procedimiento_input.send_keys(Keys.TAB)

        ActionChains(driver).send_keys("1").perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(0.7)

        ActionChains(driver).send_keys("1").perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(0.7)

        ActionChains(driver).send_keys("1").perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

    finally:
        driver.quit()

def formatear_entrada(event, posiciones, separador, max_length, siguiente_campo=None):
    widget = event.widget
    texto = widget.get()
    if len(texto) > max_length:
        widget.delete(max_length, "end")
        return
    for pos in posiciones:
        if len(texto) == pos and texto[-1] != separador:
            widget.insert(pos, separador)
    if len(texto) == max_length and siguiente_campo:
        siguiente_campo.focus()

def iniciar_programa():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    renipres = entry_renipres.get()
    fua = entry_fua.get()
    dni = entry_dni.get()
    cod_presta = cod_presta_var.get()
    responsable = entry_responsable.get()
    if not fecha or not hora or not renipres or not fua or not dni or not cod_presta or not responsable:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    buscar_y_escribir_datos(fecha, hora, renipres, fua, dni, cod_presta, responsable)

root = Tk()
root.title("Ingreso de Datos")

window_width = 350
window_height = 350

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10), padding=5)
style.configure("TEntry", font=("Arial", 10), padding=5)
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TRadiobutton", font=("Arial", 10), padding=5)

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Ingrese la fecha (DD/MM):").grid(row=0, column=0, sticky="w", pady=5)
entry_fecha = ttk.Entry(main_frame)
entry_fecha.grid(row=0, column=1, sticky="ew", pady=5)
entry_fecha.focus()
entry_fecha.bind("<KeyRelease>", lambda e: formatear_entrada(e, {2}, "/", 5))

ttk.Label(main_frame, text="Ingrese la hora (HH:MM):").grid(row=1, column=0, sticky="w", pady=5)
entry_hora = ttk.Entry(main_frame)
entry_hora.grid(row=1, column=1, sticky="ew", pady=5)
entry_hora.bind("<KeyRelease>", lambda e: formatear_entrada(e, {2}, ":", 5))

ttk.Label(main_frame, text="Ingrese el RENIPRES:").grid(row=2, column=0, sticky="w", pady=5)
entry_renipres = ttk.Entry(main_frame)
entry_renipres.grid(row=2, column=1, sticky="ew", pady=5)

ttk.Label(main_frame, text="Ingrese el FUA:").grid(row=3, column=0, sticky="w", pady=5)
entry_fua = ttk.Entry(main_frame)
entry_fua.grid(row=3, column=1, sticky="ew", pady=5)

ttk.Label(main_frame, text="Ingrese el DNI:").grid(row=4, column=0, sticky="w", pady=5)
entry_dni = ttk.Entry(main_frame)
entry_dni.grid(row=4, column=1, sticky="ew", pady=5)

ttk.Label(main_frame, text="Seleccione el COD PRESTA:").grid(row=5, column=0, sticky="w", pady=5)
cod_presta_var = StringVar(value="016")

frame_cod_presta = ttk.Frame(main_frame)
frame_cod_presta.grid(row=5, column=1, sticky="ew", pady=5)

ttk.Radiobutton(frame_cod_presta, text="022", variable=cod_presta_var, value="022").pack(side="left", padx=10)
ttk.Radiobutton(frame_cod_presta, text="075", variable=cod_presta_var, value="075").pack(side="left", padx=10)

ttk.Label(main_frame, text="Responsable:").grid(row=6, column=0, sticky="w", pady=5)
entry_responsable = ttk.Entry(main_frame)
entry_responsable.grid(row=6, column=1, sticky="ew", pady=5)

btn_ejecutar = ttk.Button(main_frame, text="Ejecutar", command=iniciar_programa)
btn_ejecutar.grid(row=7, column=0, columnspan=2, pady=10)

main_frame.columnconfigure(1, weight=1)

root.mainloop()