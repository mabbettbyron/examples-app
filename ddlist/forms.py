from django import forms
from .models import Reading, Country, City

class ReadingForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select())
    
    class Meta:
        model = Reading
        fields = ('name', 'birthdate', 'city')

    # Override
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
