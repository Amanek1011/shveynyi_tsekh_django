from django import forms
from apps.shveya.models import Party, Material
from apps.users.models import CustomUser

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['batch_number', 'design']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['color', 'quantity_line', 'tshirt_count']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'number', 'role', 'password']