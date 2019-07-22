from django import forms
from .models import ResponseSub, ResponseMCQ
from .models import Candidate

class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('firstName', 'lastName', 'username', 'password', 'email', 'bitsid', 'contact', 'description', )

class GetResponse(forms.ModelForm):

    class Meta:
        model = ResponseSub
        fields = ('free_response',)
        
class GetResponseMCQ(forms.ModelForm):

    class Meta:
        model = ResponseMCQ
        fields = ('response1', 'response2', 'response3', 'response4',)
        
