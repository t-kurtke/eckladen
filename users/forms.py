from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from users.models import Profile
from django.contrib.auth.models import User
class SignupProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('contact',)
    def signup(self, request, user):
        user.profile.contact = self.cleaned_data['contact']
        #user.save()
        #user.profile.save()

class UserDeleteForm(ModelForm):
    class Meta:
        model = User
        fields = []
