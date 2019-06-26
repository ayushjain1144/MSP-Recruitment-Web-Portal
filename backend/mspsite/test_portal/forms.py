from django import forms
from .models import Response
from .models import Candidate

class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('firstname', 'lastname','email', 'bitsid', 'contact')


class GetResponse(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('free_response',)
