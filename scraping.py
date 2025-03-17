import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

driver = uc.Chrome(options=options)
driver.get("https://www.infojobs.net/")
time.sleep(4)

# aceptamos cookies
try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
    )
    submit_button.click()
    print("Agree cookies and close...")
except Exception as e:
    print(f"Error: {e} - Agree button not found or already clicked.")

# empezamos búsqueda
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "palabra"))
    )
    search_box.send_keys("Full Stack")
    print("...Searching...")

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "searchOffers"))
    )
    search_button.click()
    time.sleep(4)

    # SCROLL dinámico hasta que todas las ofertas estén cargadas
    previous_count = 0
    while True:
        offers = driver.find_elements(By.CSS_SELECTOR, "div.sui-AtomCard")
        total_offers = len(offers)

        # si no hay nuevas ofertas, salimos del bucle
        if total_offers == previous_count:
            break
        previous_count = total_offers

        # Scroll hasta la última oferta visible
        driver.execute_script("arguments[0].scrollIntoView();", offers[-1])
        time.sleep(2)  # esperamos que carguen más ofertas

    print(f"Total ofertas encontradas: {len(offers)}")

    # extraemos información de cada oferta
    for index, offer in enumerate(offers):
        try:
            title = offer.find_element(By.CSS_SELECTOR, "h2.ij-OfferCardContent-description-title a").text
            company = offer.find_element(By.CSS_SELECTOR, "h3.ij-OfferCardContent-description-subtitle a").text
            location = offer.find_element(By.CSS_SELECTOR, "li.ij-OfferCardContent-description-list-item").text
            
            try:
                salary = offer.find_element(By.CSS_SELECTOR, ".ij-OfferCardContent-description-salary-info").text
            except:
                salary = "No disponible"

            print(f"Oferta {index + 1}:")
            print(f"  Título: {title}")
            print(f"  Empresa: {company}")
            print(f"  Ubicación: {location}")
            print(f"  Salario: {salary}")
            print("-" * 40)
        
        except Exception as e:
            print(f"Error al extraer datos de la oferta {index + 1}: {e}")

    print("Búsqueda realizada con éxito.")

except Exception as e:
    print(f"Error al localizar el campo de búsqueda o el botón: {e}")

print("El navegador sigue abierto, puedes cerrarlo manualmente.")
time.sleep(3600)
