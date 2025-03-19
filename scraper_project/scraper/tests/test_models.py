from django.test import TestCase
from datetime import datetime
from scraper.models import JobOffer 

class ModelsTestCase(TestCase):
    # creamos un setup de prueba para pasar los test
    def setUp(self):
        self.job_offer = JobOffer.objects.create(
            title="Junior full Stack Developer",
            company="Factoria F5",
            company_url="https://factoriaf5.org/",
            location="Madrid",
            salary="2000",
            work_mode="Híbrido",
            contract_type="Indefinido",
            workday="Jornada completa",
            search_date=datetime.now(),
            search_term="Full stack",
        )

    def test_job_offer_fields(self):
        """Testing that the attribute values are correct"""
        job_offer = JobOffer.objects.get(title="Junior full Stack Developer")
        self.assertEqual(job_offer.company_url, "https://factoriaf5.org/")
        self.assertEqual(job_offer.search_term, "Full stack")
        self.assertEqual(job_offer.location, "Madrid")
        self.assertEqual(job_offer.salary, "2000")
        self.assertEqual(job_offer.work_mode, "Híbrido")
        self.assertEqual(job_offer.contract_type, "Indefinido")
        self.assertEqual(job_offer.workday, "Jornada completa")
        self.assertEqual(job_offer.search_date.date(), datetime.now().date())

    def test_job_offer_str(self):
        """Testing the __str__ method of the JobOffer model"""
        self.assertEqual(str(self.job_offer), "Junior full Stack Developer at Factoria F5")  # Corregido el uso de __str__

    def test_null_fields(self):
        """Testing that nullable fields actually can be null"""
        # creamos una oferta de trabajo sin proporcionar valores para los campos opcionales
        job_offer = JobOffer.objects.create(
            title="Junior Developer",
            company="Factoria",
            company_url="https://factoriaf5.org/",
            location="Madrid",
        )
        # comprobamos que los campos opcionales son nulos en la base de datos
        self.assertIsNone(job_offer.salary)
        self.assertIsNone(job_offer.work_mode)
        self.assertIsNone(job_offer.contract_type)
        self.assertIsNone(job_offer.workday)