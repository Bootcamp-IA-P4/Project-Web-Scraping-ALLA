from django.test import TestCase
from django.urls import reverse
from scraper.models import JobOffer

class JobSearchViewTestCase(TestCase):
    def setUp(self):
        """Creating some job offers for testing"""
        JobOffer.objects.create(
            title="Full stack developer",
            company="Company A",
            company_url="http://companya.com",
            location="Madrid",
            salary="3000",
            work_mode="Remoto",
            contract_type="Indefinido",
            workday="Jornada completa",
            search_term="developer"
        )
        JobOffer.objects.create(
            title="Java script developer",
            company="Company B",
            company_url="http://companyb.com",
            location="Barcelona",
            salary="2500",
            work_mode="Presencial",
            contract_type="Temporal",
            workday="Jornada completa",
            search_term="Java"
        )

    def test_job_list_with_search_term(self):
        """Testing the job_list with a search term"""
        response = self.client.get(reverse('job_list') + '?search_term=developer')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Full stack developer")

    def test_reset_search_data_post(self):
        """Testing the reset button to delete all job offers from database"""
        response = self.client.post(reverse('reset_search_data'))
        self.assertRedirects(response, reverse('job_list'))
        self.assertEqual(JobOffer.objects.count(), 0)
    
    def test_job_search_get(self):
        """Testing the searching_html form is working properly"""
        response = self.client.get(reverse('job_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/search.html')

    def test_error_page_get(self):
        """Testing error.html is displaying correctly"""
        response = self.client.get(reverse('error_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/error.html')