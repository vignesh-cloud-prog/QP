import random
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import UserOTP
from django.core.mail import send_mail
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect("login")

def signup(request):
	if request.method == 'POST':
		get_otp = request.POST.get('otp') #213243 #None

		if get_otp is not None:
			get_usr = request.POST.get('usr')
			usr = User.objects.get(username=get_usr)
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				messages.success(request, f'Account is Created For {usr.username}')
				return redirect('login')
			else:
				messages.warning(request, f'You Entered a Wrong OTP')
				return render(request, 'accounts/register.html', {'otp': True, 'usr': usr})

		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			name = form.cleaned_data.get('name')

			usr = User.objects.get(username=username)
			usr.email = email
			usr.first_name = name
			# usr.last_name = name[1]
			usr.is_active = False
			usr.save()
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)

			mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to QP Web - Verify Your Email",
				mess,
				'qpcom80@gmail.com',
				[usr.email],
				fail_silently = True
				)

			return render(request, 'accounts/register.html', {'otp': True, 'usr': usr})

		
	else:
		form = CreateUserForm()

	return render(request, 'accounts/register.html', {'form':form})

def resend_otp(request):
	if request.method == "GET":
		get_usr = request.GET['usr']
		if User.objects.filter(username = get_usr).exists() and not User.objects.get(username = get_usr).is_active:
			usr = User.objects.get(username=get_usr)
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to QP Web - Verify Your Email",
				mess,
				'qpcom80@gmail.com',
				[usr.email],
				fail_silently = False
				)
			return HttpResponse("Resend")

	return HttpResponse("Can't Send ")


def login_view(request):
	if request.user.is_authenticated:
		return redirect('profile')
	if request.method == 'POST':
		get_otp = request.POST.get('otp') #213243 #None

		if get_otp:
			get_usr = request.POST.get('usr')
			usr = User.objects.get(username=get_usr)
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				login(request, usr)
				return redirect('profile')
			else:
				messages.warning(request, f'You Entered a Wrong OTP')
				return render(request, 'accounts/login.html', {'otp': True, 'usr': usr})


		usrname = request.POST['username']
		passwd = request.POST['password']

		user = authenticate(request, username = usrname, password = passwd) #None
		if user is not None:
			login(request, user)
			return redirect('profile')
		elif not User.objects.filter(username = usrname).exists():
			messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
			return redirect('login')
		elif not User.objects.get(username=usrname).is_active:
			usr = User.objects.get(username=usrname)
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to QP web - Verify Your Email",
				mess,
				'qpcom80@gmail.com',
				[usr.email],
				fail_silently = False
				)
			return render(request, 'accounts/login.html', {'otp': True, 'usr': usr})
		else:
			messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
			return redirect('login')

	context={

    }
	return render(request, 'accounts/login.html', context)

def profile(request):
    context={}
    return render(request, 'accounts/profile.html', context)

def test_view(request):
	context={}
	return render(request,'practice/sheet.html',context)
