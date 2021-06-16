from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Genre, Book, Attachment


class BookModelForm(ModelForm):
    def clean_runtime(self):
       data = self.cleaned_data['pages']
       if data <= 0 or data > 22400:
           raise ValidationError('Neplatný počet stránek')
       return data

    def clean_rate(self):
       data = self.cleaned_data['rate']
       if data < 1 or data > 10:
           raise ValidationError('Neplatné hodnocení: musí být v rozsahu 1-10')
       return data

    class Meta:
        model = Book
        fields = ['title', 'plot', 'poster', 'genres', 'release_date', 'pages', 'rate']
        labels = {'title': 'Název knihy', 'plot': 'Stručný děj'}