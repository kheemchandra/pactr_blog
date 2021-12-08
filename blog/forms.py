from django import forms
from django.db.models import fields 

from .models import Comment

class ShareForm(forms.Form):
    name = forms.CharField(label='Name', max_length=25)
    from_email = forms.EmailField(label='Email')
    to_email = forms.EmailField(label='To')
    comment = forms.CharField(label='Comment', widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['body', 'name', 'email']


    