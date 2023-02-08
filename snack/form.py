from django import forms
from snack.models import Snack


class SnackForm(forms.ModelForm):
    class Meta:
        model=Snack
        fields=('name', 'image', 'url', 'description')