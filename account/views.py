from django.shortcuts import render, redirect
from django.contrib.auth.models import User   # User is for those new in our website and wants to be authorized
from django.contrib import auth     # auth is use to give authority to those that have access to our website already


def signup(request):

    if request.method == 'POST':

        # User has info and wants an account now!

        if request.POST['password1'] == request.POST['password2']:   # Test if password are equal

            try:
                user = User.objects.get(username=request.POST['username'])    # when testing for password confirming if user name does not exist else give a error below

                return render(request, 'account/signup.html', {'error':'Username exist'})
                # If user has been taken Den hits Error

            except User.DoesNotExist:   # Means if User is new to the website and his username have not been used den an account will be created

                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])

                auth.login(request,user)

                return redirect('create')

        else:

            return render(request, 'account/signup.html', {'error':'Passwords must match'})

    else:

        # If request is the big post then execute the command below it else come to this else statement return account/signup

        return render(request, 'account/signup.html')


def login(request):
        if request.method == 'POST':
                user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:  # User not None means if User is A Genuie User
                        auth.login(request, user)
                        return redirect('create')
                else:  # means a none Genuei User
                        return render(request, 'account/login.html',
                                      {'error': 'Username or Password not found ! , Try Signup'})

        else:
                return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')









