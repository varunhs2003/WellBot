# chat_app/admin.py

from django.contrib import admin
from .models import Symptom, MentalIssue, SymptomToIssue, NextSymptomToIssue

admin.site.register(Symptom)
admin.site.register(MentalIssue)
admin.site.register(SymptomToIssue)
admin.site.register(NextSymptomToIssue)
