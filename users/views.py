import random
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import UserOTP
from profiles.models import Profile
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def logoutUser(request):
    """
    View to logout user and redirect to home 
    """
    logout(request)
    return redirect("home")


def signup(request, *args, **kwargs):
    """
    Displays and takes user signup form :model:`auth.User`.

    **Context**

    ``mymodel``
        An instance of :model:`auth.User` and :model:`profiles.Profile` and :model:`users.UserOTP`.

    **Template:**

    :template:`users/register.html`
    """
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('profile.id ', profile.id)
        print('id', profile.id)
    except:
        pass
    print(request.session.get_expiry_date())

    profil_id = request.session.get('ref_profile')

    if request.method == 'POST':
        get_otp = request.POST.get('otp')  # 213243 #None

        if get_otp is not None:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                messages.success(
                    request, f'Account is Created For {usr.username}')
                login(request, usr)
                return redirect('update_profile')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'users/register.html', {'otp': True, 'usr': usr})

        form = CreateUserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            if profil_id is not None:
                recomended_by_profile = Profile.objects.get(id=profil_id)
                registered_user = User.objects.get(id=instance.id)
                registered_profile = Profile.objects.get(user=registered_user)
                registered_profile.recomended_by = recomended_by_profile.user
                registered_profile.save()

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
            UserOTP.objects.create(user=usr, otp=usr_otp)

            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to QP Web - Verify Your Email",
                mess,
                'qpcom80@gmail.com',
                [usr.email],
                fail_silently=True
            )

            return render(request, 'users/register.html', {'otp': True, 'usr': usr})

    else:
        form = CreateUserForm()

    return render(request, 'users/register.html', {'form': form})


def resend_otp(request, usr):
    """
    View to resend OTP :model:`users.UserOTP`.

    **Context**

    ``mymodel``
        An instance of :model:`users.UserOTP`.

    """
    print("function called")
    if request.method == "GET":
        get_usr = usr
        if User.objects.filter(username=get_usr).exists() and not User.objects.get(username=get_usr).is_active:
            usr = User.objects.get(username=get_usr)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to QP Web - Verify Your Email",
                mess,
                'qpcom80@gmail.com',
                [usr.email],
                fail_silently=True
            )
            messages.success(
                request, f"{usr.username} your otp is sent to {usr.email}")
            return JsonResponse({"msg": "Resend"})

    return JsonResponse({"msg": "Can't Send"})


def login_view(request):
    """
    View to login user and verify user email if not already verified :model:`auth.User`.

    **Context**

    ``mymodel``
        An instance of :model:`auth.User`.

    **Template:**

    :template:`users/login.html`
    """
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        get_otp = request.POST.get('otp')  # 213243 #None

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                login(request, usr)
                return redirect('update_profile')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'users/login.html', {'otp': True, 'usr': usr})

        usrname = request.POST['username']
        passwd = request.POST['password']

        user = authenticate(request, username=usrname, password=passwd)  # None
        if user is not None:
            login(request, user)
            return redirect('profile')
        elif not User.objects.filter(username=usrname).exists():
            messages.warning(
                request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
        elif not User.objects.get(username=usrname).is_active:
            usr = User.objects.get(username=usrname)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to QP web - Verify Your Email",
                mess,
                'qpcom80@gmail.com',
                [usr.email],
                fail_silently=True
            )
            return render(request, 'users/login.html', {'otp': True, 'usr': usr})
        else:
            messages.warning(
                request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')

    context = {

    }
    return render(request, 'users/login.html', context)
