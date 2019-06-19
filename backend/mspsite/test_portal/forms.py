from django import forms

from .models import Candidate

class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('firstname', 'lastname','email', 'bitsid', 'contact')
