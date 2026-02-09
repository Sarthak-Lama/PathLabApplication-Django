from rest_framework import serializers
from .models import Patient, Test, LabReport

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "patient_name", "age", "gender", "test_name"]  # fixed typo
        read_only_fields = ["id"]  # fixed typo

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["id", "test_name", "description", "price", "is_active", "created_at"]
        read_only_fields = ["id", "created_at"]  # fixed typo

class LabReportSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.patient_name', read_only=True)
    test_name = serializers.CharField(source='test.test_name', read_only=True)

    class Meta:
        model = LabReport
        fields = ["id", "patient", "patient_name", "test", "test_name", "status", "result_value", "created_at", "result_date"]
        read_only_fields = ["id", "created_at", "result_date"]