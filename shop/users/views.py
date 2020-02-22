from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_GET

from .forms import RegistrationForm


def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', context={
            "form": form
        })
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            link = user.get_verification_link()
            user.email_user(
                "Email confirmation",
                f"Please follow the <a href='{link}'>link</a>",
                from_email='admin@admin.com'
            )
            user.verification_email_sent_at = timezone.now()
            user.save()
            return redirect("/")
        else:
            return render(request, 'register.html', context={
                "form": form
            })


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', context={
                "error": True
            })


@login_required
@require_GET
def verify_view(request):
    secret_ket = request.GET.get('key')
    if request.user.check_key(secret_ket):
        return render(request, 'register.html')
    else:
        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")