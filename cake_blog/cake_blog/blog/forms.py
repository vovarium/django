from django import forms
from .models import Comment
from captcha.fields import CaptchaField
 

class CommentForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Comment
		exclude = ['create_at', 'post']
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'website': forms.TextInput(attrs={'placeholder': 'website'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'})
        }

