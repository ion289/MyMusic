from django.forms import ModelForm

from myapp.models import UserMessage



class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = '__all__'