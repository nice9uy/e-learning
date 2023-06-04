from django.shortcuts import render


# Create your views here.
def home(request):
    title = "My Page Title"
    return render(request, "index.html")

def blog(request):
    return render(request,"pages/blog.html")