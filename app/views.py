from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Patient , Test , LabReport
from .serializers import PatientSerializer,TestSerializer,LabReportSerializer,LoginSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PatientViewsets(viewsets.ModelViewSet):
#Endpoitns for managing patients
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes =[IsAuthenticated]
   
  

class TestViewSets(viewsets.ModelViewSet):
     queryset = Test.objects.all()
     serializer_class = TestSerializer
     permission_classes =[IsAuthenticated]

class ReportViewsets(viewsets.ModelViewSet):
     queryset = LabReport.objects.all()
     serializer_class = LabReportSerializer
     permission_classes =[IsAuthenticated]

class LoginAPI(APIView):
     permission_classes = [AllowAny]

     def post(self, request):
          serializer = LoginSerializer(data= request.data)
          serializer.is_valid(raise_exception=True)

          user = authenticate(
               username = serializer.validated_data['username'],
               password= serializer.validated_data['password']
          )

          if not user:
               return Response(
                    {"error":"Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
               )
          
          token, _ = Token.objects.get_or_create(user=user)

          return Response ({
               "token":token.key,
               "user_id":user.id,
               "username":user.username
          })
     
                




