from django.contrib import admin
from .models import Patient , Test , LabReport

# Register your models here.
admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(LabReport)