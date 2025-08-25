from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['full_name', 'student_id', 'category', 'description', 'date_of_incident', 'contact_info']
        widgets = {
            'date_of_incident': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_id'].required = True
        self.fields['category'].required = True
        self.fields['description'].required = True
        self.fields['date_of_incident'].required = True