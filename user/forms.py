from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', 'password1', 'password2']
