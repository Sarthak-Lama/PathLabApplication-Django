from django.db import models

# Create your models here.



STATUS_CHOICES = (
   ('P','Pending'),
   ('C','Complete'),
   ('D','Delivered')
  )


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    test_name = models.CharField(max_length=100)

    def __str__(self):
        return self.test_name
 

class Test(models.Model):
  test_name = models.CharField(max_length=150 , unique=True)
  description =models.TextField()
  price = models.DecimalField(max_digits=15 , decimal_places=2)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
   return self.test_name
  

class LabReport(models.Model):
  
  
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  test = models.ForeignKey(Test , on_delete=models.CASCADE)
  status = models.CharField(max_length=1 , choices=STATUS_CHOICES , default='P')
  result_value = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  result_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.patient.patient_name} - {self.test.test_name}"




  
  
  

