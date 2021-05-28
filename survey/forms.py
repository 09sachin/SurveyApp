from django import forms
from . models import Survey
from .models import Name, Product1, Product2


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'


class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = '__all__'


class P1Form(forms.ModelForm):
    class Meta:
        model = Product1
        exclude = ('name',)


class P2Form(forms.ModelForm):
    class Meta:
        model = Product2
        exclude = ('name',)
