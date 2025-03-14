from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'id',
            'namw',
            'patient_id',
            'patient_name',
            'summary',
            'image_url',
            'result',
            'dateTime',
        ]

        labels = {
            'id': 'Id',
            'name': 'Name',
            'patient_id': 'Patient ID',
            'patient_name': 'Patient Name',
            'summary': 'Summary',
            'image_url': 'Image URL',
            'result': 'Result',
            'dateTime': 'Date Time',
        }
