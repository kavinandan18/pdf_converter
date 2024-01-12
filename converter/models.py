from django.db import models

class ConvertedFile(models.Model):
    original_file = models.FileField(upload_to='uploads/')
    converted_file = models.FileField(upload_to='converted/')
    timestamp = models.DateTimeField(auto_now_add=True)
