from django import forms
from .models import Material

class FourXForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['four_x', 'four_x_count']

class RaspashForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['raspash', 'raspash_count']

class BeikaForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['beika', 'beika_count']

class StrochkaForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['strochka', 'strochka_count']

class GorloForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['gorlo', 'gorlo_count']

class YtygForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['ytyg', 'ytyg_count']

class OtkForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['otk', 'otk_count']

class YpakovkaForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['ypakovka', 'ypakovka_count']