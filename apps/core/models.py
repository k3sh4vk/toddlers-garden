from django.core.validators import MaxValueValidator, EmailValidator
from django.db import models
# Create your models here.

class Queries(models.Model):
    query_id = models.AutoField(primary_key=True)
    parent_name = models.CharField(max_length=50)
    child_name = models.CharField(max_length=50)
    child_dob = models.DateField()
    contact_number = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    email_address = models.EmailField(validators=[EmailValidator()])
    filled_details = models.TextField(null=True)
    contacted_parent = models.BooleanField(default=False)
    final_comments = models.TextField(null=False)
