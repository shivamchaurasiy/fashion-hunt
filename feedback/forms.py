from django import forms
from feedback.models import Feedback

# class FeedbackForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     contact_num=forms.IntegerField()
#     email=forms.EmailField()
#     suggestion=forms.CharField(max_length=50)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        
        labels = {'name':'Name', 'contact_num':'Contact Number', 'email':'Email', 'suggestio':'Suggestion'}       
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact_num':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'suggestion':forms.TextInput(attrs={'class':'form-control'}),
        }
        
        