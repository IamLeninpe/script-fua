from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import time

# Ruta del ChromeDriver
chrome_driver_path = "chromedriver.exe"

# Función para adjuntar a una sesión existente
def attach_to_session(executor_url, session_id):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
    original_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            return {'success': 0, 'value': None, 'sessionId': session_id}
        return original_execute(self, command, params)

    RemoteWebDriver.execute = new_command_execute

    # Configurar opciones vacías para el navegador
    options = Options()
    driver = RemoteWebDriver(command_executor=executor_url, options=options)
    driver.session_id = session_id
    RemoteWebDriver.execute = original_execute
    return driver

# URL del WebDriver y sesión existente (debes reemplazar estos valores)
executor_url = "http://localhost:9515"  # Cambia esto según tu configuración
session_id = "tu-session-id"  # Reemplaza con el ID de sesión existente

# Adjuntar a la sesión existente
driver = attach_to_session(executor_url, session_id)

# Realizar acciones en la pestaña abierta
driver.get("http://192.168.86.202:10088/opensis/arfsisweb/index.jsp#/registrar")

# Esperar 5 segundos para que la página cargue completamente
time.sleep(10)

# Cerrar el navegador
driver.quit()