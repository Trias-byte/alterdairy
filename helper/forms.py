from .models import RequestsHelps
from django.forms import ModelForm


class RequestForm(ModelForm):
    class Meta:
        model = RequestsHelps
        fields = ['title', 'subject', 'testQuestion']
