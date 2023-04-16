from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User

class UserUpdate(UserChangeForm):
	class Meta:
		model = User
		fields = ('username','profile_pic','bio')