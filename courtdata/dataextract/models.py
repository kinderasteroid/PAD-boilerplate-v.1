from django.db import models

# Create your models here.
class CaseData(models.Model):
    caseNumber = models.CharField(max_length=255)
    caseParticipant = models.CharField(max_length=255)
    caseCategory = models.CharField(max_length=255)