from django.db import models

# Create your models here.
class mysoftware(models.Model):
    software_title=models.CharField(max_length=100,null=True)
    software_description=models.TextField(null=True)
    software_picture=models.ImageField(upload_to='static/softwarepic/',null=True)
    software_date=models.DateField()
    software_url=models.TextField(null=True)



