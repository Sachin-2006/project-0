from django import forms
from .models import ProfileDetail


class ProfileDetailForm(forms.ModelForm):
	class Meta:
		model = ProfileDetail
		fields = ["profile_pic","bio"]
		