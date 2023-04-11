from django.shortcuts import render

def home(request):
	if request.user.is_authenticated:
		current_user = request.user

	context = {"user":request.user}
	return render(request,"core/home.html",context)