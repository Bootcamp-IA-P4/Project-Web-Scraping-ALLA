from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()

service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

time.sleep(2)  


# abrimos la página de InfoJobs
driver.get("https://www.infojobs.net/")
# esperamos 4 segundos
time.sleep(4)  


try:
    # esperamos hasta que la barra de búsqueda esté presente en la página
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "palabra"))
    )
    time.sleep(6)  

    # escribimos "Full Stack" en la barra de búsqueda
    search_box.send_keys("Full Stack")

    # esperamos 4 segundos
    time.sleep(4)  

    
    # esperamos a que el botón de búsqueda esté presente y hacer clic
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "searchOffers"))
    )
    # esperamos 3 segundos
    time.sleep(3)  

    search_button.click()

    print("Búsqueda realizada con éxito.")

except Exception as e:
    print(f"Error al localizar el campo de búsqueda o el botón: {e}")
