from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField
    auction = forms.BooleanField(required=False)
    image = forms.ImageField
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Advertisement
        fields = ("title", "description", "image", "price", "auction")
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title


#    title = forms.CharField(max_length=128)
#     description = forms.CharField(widget=forms.Textarea)
#     price = forms.DecimalField
#     auction = forms.BooleanField(required=False)
#     image = forms.ImageField