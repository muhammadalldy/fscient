from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Document
from .models import Journal


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	noreg = forms.CharField(label='NRM')
	angkatan = forms.CharField(label='Angkatan')
	peminatan = forms.CharField(label='Peminatan')
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2','noreg','angkatan','peminatan', )


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
		
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('description', 'journal', )
		