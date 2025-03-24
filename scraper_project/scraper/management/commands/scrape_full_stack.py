from django.core.management.base import BaseCommand
from django.test import RequestFactory
from scraper.views import job_search

class Command(BaseCommand):
    help = 'Perform automatic job search for Full Stack Junior every 2 minutes'

    def handle(self, *args, **kwargs):
        # Creamos un objeto Request para simular la solicitud POST
        factory = RequestFactory()
        
        # simulamos el POST con la palabra "Full Stack Junior"
        request = factory.post('/job_search/', data={'search_term': 'Full Stack Junior'})

        job_search(request)
        
        self.stdout.write(self.style.SUCCESS('Successfully ran the job search for Full Stack!'))
