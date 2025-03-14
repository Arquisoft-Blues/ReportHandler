from django.db import models

class Report(models.Model):
    #report_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=20)  # Ajusta max_length según tus necesidades
    patient_name = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)  # Permite textos largos, opcional
    image_url = models.URLField(blank=True, null=True)   # URL de la imagen, opcional
    result = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    # Se asigna la fecha y hora de creación

    def __str__(self):
        return self.name
