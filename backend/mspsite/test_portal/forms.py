from django import forms
from .models import Response, Responsem, Responsei
from .models import Candidate

class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('firstname', 'lastname', 'username', 'password', 'email', 'bitsid', 'contact', 'description', )


class GetResponse(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('free_response',)
        
class GetResponsem(forms.ModelForm):

    class Meta:
        model = Responsem
        fields = ('responsem1', 'responsem2', 'responsem3', 'responsem4',)
        
class GetResponsei(forms.ModelForm):

    class Meta:
        model = Responsei
        fields = ('responsei',)
