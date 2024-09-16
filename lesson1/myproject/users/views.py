from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register_view(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            login(req, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(req, "users/register_user.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(req):
    if req.method == "POST":
        logout(req)
        return redirect("home")
