import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-gpu")  # Desactivar GPU
options.add_argument("--no-sandbox")  # Desactivar sandbox
options.add_argument("--disable-extensions")

# cambiamos el user-agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

# iniciamos Chrome con undetected_chromedriver
driver = uc.Chrome(options=options)

driver.get("https://www.infojobs.net/")
time.sleep(4)

try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
    )
    submit_button.click()
    print("Agree and close clicked.")
except Exception as e:
    print(f"Error: {e} - Agree button not found or already clicked.")

try:
    # esperamos hasta que la barra de búsqueda esté presente
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "palabra"))
    )
    search_box.send_keys("Full Stack")
    print("...Searching...")

    # esperamos a que el botón de búsqueda esté presente y hacer clic
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "searchOffers"))
    )
    search_button.click()
    time.sleep(4)

    print("Búsqueda realizada con éxito.")
    time.sleep(4)

except Exception as e:
    print(f"Error al localizar el campo de búsqueda o el botón: {e}")

print("El navegador sigue abierto, puedes cerrarlo manualmente.")
