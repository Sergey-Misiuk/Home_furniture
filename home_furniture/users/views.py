from django.shortcuts import render

def login(request):
    context = {
        'title': 'Home - Авторзация',
    }
    
    return render(request, 'users/login.html', context=context)


def registration(request):
    context = {
        'title': 'Home - Регистрация',
    }
    
    return render(request, 'users/registration.html', context=context)


def profile(request):
    context = {
        'title': 'Home - Кабинет',
    }
    
    return render(request, 'users/profile.html', context=context)


def logout(request):
    context = {
        'title': 'Home - Авторзация',
    }
    
    return render(request, 'users/logout.html', context=context)