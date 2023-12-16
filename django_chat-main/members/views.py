from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models



def user_signup(request):
	if request.method == 'POST':
		user_email = request.POST['user_email']
		username = request.POST['username']
		user_pswd = request.POST['user_pass']
		user_model = get_user_model()
		##
		if not username.strip():
			messages.error(request, 'Something is wrong.')
			return render(request, 'app_users/signup.html')
		##
		if user_model.objects.filter(email=user_email).exists():
			messages.error(request, 'Something is wrong.')
			return render(request, 'app_users/signup.html')
		##
		user_obj = user_model.objects.create_user(email=user_email, password=user_pswd)
		user_obj.set_password(user_pswd)
		user_obj.username = username
		user_obj.save()
		user_auth = authenticate(username=user_email, password=user_pswd)
		##
		if user_auth:
			login(request, user_auth)
			return redirect('home')
	return render(request, 'signup.html')


def user_login(request):
	if request.method == 'POST':
		user_email = request.POST['user_email']
		user_pswd = request.POST['user_pass']
		try:
			user_auth = authenticate(username=user_email, password=user_pswd)
			login(request, user_auth)
			return redirect('home')
		except:
			messages.error(request, 'Something is wrong.')
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')


def user_logout(request):
	try:
		logout(request)
	except:
		messages.error(request, 'Something is wrong.')
	return redirect('login')
@login_required
def room(request, slug):
    room = models.Room.objects.get(slug=slug)
    messages = models.Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})