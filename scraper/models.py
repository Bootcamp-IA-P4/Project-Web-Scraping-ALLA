from django.db import models

# Create your models here.
from django.db import models

class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_url = models.URLField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, blank=True, null=True)
    work_mode = models.CharField(max_length=255, blank=True, null=True)
    contract_type = models.CharField(max_length=255, blank=True, null=True)
    workday = models.CharField(max_length=255, blank=True, null=True)
    search_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job_offers'

    def __str__(self):
        return f"{self.title} at {self.company}"
