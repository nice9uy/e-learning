from django.shortcuts import render


# Create your views here.
def login(request):
    title = "login"
    return render(request, "pages/login.html", {"title": title})


def reset(request):
    title = "reset password"
    return render(request, "pages/reset.html", {"title": title})
