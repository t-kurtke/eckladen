from django.contrib.auth.forms import UserCreationForm

class Custom_user_creation_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)