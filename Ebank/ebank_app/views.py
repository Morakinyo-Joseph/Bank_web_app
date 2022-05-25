from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserInfo


def index(request):
    return render(request, 'index.html', {})


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email address has being used!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                return redirect('logging_in')

        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')

    else:
        return render(request, 'register.html', {})

                                   
def logging_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect('homepage')
        else:
            messages.info(request, 'Invalid Username/Password!')
            return redirect('logging_in')

    else:
        return render(request, 'logging_in.html')


def logging_out(request):
    logout(request)
    return redirect('logging_in')


def homepage(request):
    return render(request, 'homepage.html', {})


def transaction(request):
    return render(request, 'transaction.html', {})


def profile(request):
    user_info = UserInfo.objects.all()
    return render(request, 'profile.html', {'user_info': user_info})


def edit_profile(request):
    user_info = UserInfo.objects.all()

    if request.method == 'POST':
        username_edit = request.POST['edit_username']
        firstname_edit = request.POST['edit_firstname']
        lastname_edit = request.POST['edit_lastname']
        email_edit = request.POST['edit_email']
        phone_number_edit = request.POST['edit_phone']

        if len(phone_number_edit) == 11:
            if int(phone_number_edit) / 1 == 0:
                if User.objects.filter(username=username_edit).exists():
                    messages.info(request, 'Username already exists!')
                    return redirect('edit')

                elif User.objects.filter(email=email_edit).exists():
                    messages.info(request, 'Email has already been used')
                    return redirect('edit')

                else:
                    new_user_info = User.objects.all()

                    new_user_info.username = username_edit
                    new_user_info.first_name = firstname_edit
                    new_user_info.last_name = lastname_edit
                    new_user_info.email = email_edit
                    new_user_info.save()

                    new_user_info_phone = user_info
                    new_user_info_phone.phone_number = phone_number_edit
                    new_user_info_phone.save()

                    return redirect('profile')

            else:
                messages.info(request, 'Phone number not valid')
                return redirect('edit')

        else:
            messages.info(request, 'Phone number not valid')
            return redirect('edit')

    else:
        return render(request, 'profile_edit.html', {'user_info': user_info})


def change_password(request):
    pass
