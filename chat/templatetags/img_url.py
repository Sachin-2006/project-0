from django import template
from core.models import User
register = template.Library()

@register.filter
def url(u):
	u = User.objects.get(username=u)
	return u.profile_pic.url