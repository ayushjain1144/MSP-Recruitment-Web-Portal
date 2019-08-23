from django import forms
from .models import ResponseSub, ResponseMCQ, Candidate,ImageMCQ, ImageSub


class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('firstName', 'lastName', 'username', 'email', 'bitsid', 'contact', 'description', )

class ImageFormMCQ(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = ImageMCQ
        fields = ('image', )


class ImageFormSub(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = ImageSub
        fields = ('image', )


class GetResponse(forms.ModelForm):

    class Meta:
        model = ResponseSub
        fields = ('free_response',)

class GetResponseMCQ(forms.ModelForm):

    class Meta:
        model = ResponseMCQ
        fields = ('response1', 'response2', 'response3', 'response4',)
