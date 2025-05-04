from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('teams_auto_joiner.log'),
        logging.StreamHandler()
    ]
)

def configurar_chrome():
    """Configura las opciones de Chrome para Selenium"""
    chrome_options = Options()
    chrome_options.binary_location = '/usr/local/bin/chrome-for-testing'  # Especificar la ubicación de Chrome for Testing
    # chrome_options.add_argument('--headless')  # Descomenta para modo headless
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    prefs = {
        "profile.default_content_setting_values.media_stream_mic": 1,     # Permitir micrófono
        "profile.default_content_setting_values.media_stream_camera": 1    # Permitir cámara
    }
    chrome_options.add_experimental_option("prefs", prefs)
    return chrome_options

# Inicia el navegador con las opciones configuradas
driver = webdriver.Chrome(options=configurar_chrome())
id = '374936558346'
p = 'Z23f7ts2'
# Abre la web que desees
driver.maximize_window() 
driver.get(f"https://teams.microsoft.com/meet/{id}?launchAgent=marketing_join&laentry=hero&p={p}")
#https://teams.microsoft.com/meet/374936558346?launchAgent=marketing_join&laentry=hero&p=Z23f7ts2

driver.implicitly_wait(5)

# Encuentra el botón (por ejemplo, por ID)

name_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".fui-Input__input"))
)          
logging.info("Introduciendo alias")
name_input.send_keys("proyector")


button_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="prejoin-join-button"]')))
button_input.click()

logging.info("Ingreso en la reunion correcto")

input("Presiona Enter para salir...")