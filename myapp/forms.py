from django.forms import ModelForm

from myapp.models import UserMessage, Review


class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']
