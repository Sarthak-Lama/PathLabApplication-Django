from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient , Test , LabReport
from .serializers import PatientSerializer,TestSerializer,LabReportSerializer


class PatientViewsets(viewsets.ModelViewSet):
#Endpoitns for managing patients
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
   
  

class TestViewSets(viewsets.ModelViewSet):
     queryset = Test.objects.all()
     serializer_class = TestSerializer

class ReportViewsets(viewsets.ModelViewSet):
     queryset = LabReport.objects.all()
     serializer_class = LabReportSerializer





