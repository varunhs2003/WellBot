
from django.db import models



class Symptom(models.Model):

    name = models.CharField(max_length=100)



    def __str__(self):

        return self.name



class MentalIssue(models.Model):

    name = models.CharField(max_length=100)

    prescription = models.TextField()



    def __str__(self):

        return self.name



class SymptomToIssue(models.Model):

    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    issue = models.ForeignKey(MentalIssue, on_delete=models.CASCADE)



    def __str__(self):

        return f"{self.symptom} - {self.issue}"



class NextSymptomToIssue(models.Model):

    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    issue = models.ForeignKey(MentalIssue, on_delete=models.CASCADE)



    def __str__(self):

        return f"{self.symptom} - {self.issue}"