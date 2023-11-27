from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError
# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=128, widget = )
#     description = forms.CharField(widget=)
#     price = forms.DecimalField(max_digits=10, decimal_places=2, widget = )
#     auction = forms.BooleanField(widget = )
#     image = forms.ImageField(widget = )

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', "image",'video']
        widgets = { 
            "title" : forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "description" : forms.Textarea(attrs={"class": "form-control form-control-lg"}),
            "image" : forms.FileInput(attrs={"class": "form-control form-control-lg"}),
            "video" : forms.FileInput(attrs={"class": "form-control form-control-lg"})
        }

    def clean_title(self):
        data = self.cleaned_data['title']
        if data and data.startswith("?"):
            raise ValidationError("Вопросительный знак в заголовке")
        return data
