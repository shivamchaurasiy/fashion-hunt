from django import forms
from auditionregistration.models import AuditionRegistrationModel

class AuditionRegistrationForm(forms.ModelForm):
    class Meta:
        model = AuditionRegistrationModel
        fields = "__all__"
        
        
        labels = {'place-holder':''}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={ 'class':'form-control'}),
        }