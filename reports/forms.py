from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            #'report_id',
            'name',
            'patient_id',
            'patient_name',
            'summary',
            'image_url',
            'result',
            #'created_at',
        ]

        labels = {
            #'report_id': 'Report Id',
            'name': 'Name',
            'patient_id': 'Patient ID',
            'patient_name': 'Patient Name',
            'summary': 'Summary',
            'image_url': 'Image URL',
            'result': 'Result',
            #'created_at': 'Created At',
        }
