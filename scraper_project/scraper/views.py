from django.shortcuts import render, redirect
from django.urls import reverse
import time
from .models import JobOffer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from django.http import HttpResponse
import logging
from scraper.logging_config import get_logger

logger = get_logger(__name__)

def job_search(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        if search_term:
            options = Options()
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-extensions")

            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            options.add_argument(f"user-agent={user_agent}")

            driver = uc.Chrome(options=options)
            driver.get("https://www.infojobs.net/")
            logger.info("Opened web to scrape")
            time.sleep(4)

            try:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
                )
                submit_button.click()
                logger.info("Cookies accepted.")
            except Exception as e:
                print(f"Error: {e} - Agree button not found or already clicked.")
                logger.error(f"Error: {e} - Agree button not found or already clicked.")

            try:
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "palabra"))
                )
                search_box.send_keys(search_term)

                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "searchOffers"))
                )
                search_button.click()
                time.sleep(4)

                previous_count = 0
                while True:
                    offers = driver.find_elements(By.CSS_SELECTOR, "div.sui-AtomCard")
                    total_offers = len(offers)

                    if total_offers == previous_count:
                        break
                    previous_count = total_offers

                    driver.execute_script("arguments[0].scrollIntoView();", offers[-1])
                    time.sleep(2)

                for offer in offers:
                    try:
                        title = offer.find_element(By.CSS_SELECTOR, "h2.ij-OfferCardContent-description-title a").text
                        company_element = offer.find_element(By.CSS_SELECTOR, "h3.ij-OfferCardContent-description-subtitle a")
                        company = company_element.text
                        company_url = company_element.get_attribute("href")
                        location = offer.find_element(By.CSS_SELECTOR, "li.ij-OfferCardContent-description-list-item").text
                        
                        try:
                            salary = offer.find_element(By.CSS_SELECTOR, ".ij-OfferCardContent-description-salary-info").text
                        except:
                            salary = "No disponible"

                        work_mode = offer.find_elements(By.CSS_SELECTOR, ".ij-OfferCardContent-description-list-item")[1].text
                        contract_type = offer.find_element(By.CSS_SELECTOR, ".ij-OfferCardContent-description-list-item--hideOnMobile").text
                        workday = offer.find_elements(By.CSS_SELECTOR, ".ij-OfferCardContent-description-list-item--hideOnMobile")[1].text

                        # guardamos la oferta en la base de datos con el search_term
                        JobOffer.objects.create(
                            title=title,
                            company=company,
                            company_url=company_url,
                            location=location,
                            salary=salary,
                            work_mode=work_mode,
                            contract_type=contract_type,
                            workday=workday,
                            search_term=search_term  # guardamos el término de búsqueda
                        )
                    except Exception as e:
                        print(f"Error scraping offer: {e}")
                        logger.error(f"Error scraping offer: {e}")

                driver.quit()
                logger.info("Scraping finished")
                return redirect(reverse('job_list') + f'?search_term={search_term}')
            except Exception as e:
                driver.quit()
                logger.error(f"Error: {e}")
                return render(request, 'scraper/error.html', {'error': f"Error: {e}"})

    
    return render(request, 'scraper/search.html')


def job_list(request):
    search_term = request.GET.get('search_term')
    
    if search_term:
        # filtramos las ofertas por término de búsqueda y la fecha actual
        offers = JobOffer.objects.filter(search_term=search_term).order_by('-search_date')
    else:
        # si no hay término de búsqueda, mostrar todas las ofertas
        offers = JobOffer.objects.all().order_by('-search_date')

    return render(request, 'scraper/job_list.html', {'offers': offers, 'search_term': search_term})


def reset_search_data(request):
    if request.method == 'POST':
        JobOffer.objects.all().delete()
        logger.warning("All data deleted")

        return redirect(reverse('job_list'))
    return HttpResponse(status=405)

def error_page(request):
    return render(request, 'scraper/error.html')