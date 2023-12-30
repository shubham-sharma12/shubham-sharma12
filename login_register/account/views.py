from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
	return render(request, 'index.html')


def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		role = request.POST['role']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		print(role, '==============....')

		if password1 == password2:
			user = User.objects.create_user(first_name=first_name, role=role, last_name=last_name, username=username, email=email, password=password1)
			if user:
				# user.set_password(password1)
				user.is_active=False
				user.save()
				messages = 'User successfully registered!!'
				return redirect('login')
		else:
			messages='Password not match'
			return render(request, 'register.html', {'messages': messages})
	return render(request, 'register.html')



def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(username, password)
		user = authenticate(username=username, password=password)
		print(user)
		if user and user.role=='teacher':
			login(request, user)
			# messages = 'logged in'
			return redirect('teacher')
		elif user and user.role=='student':
			login(request, user)
			messages.info(request, 'logged in')
			return redirect('student')
		# messages='Password not match'
		return render(request, 'login.html')
	return render(request, 'login.html')


def logout_user(request):
	logout(request)
	return redirect('login')
	
@login_required(login_url='login')
def teacher(request):
	if request.user.role=='teacher':
		return render(request, 'teachers.html')
	return HttpResponse('<h2>Page Not Found</h2>')

@login_required(login_url='login')
def student(request):
	return render(request, 'students.html')