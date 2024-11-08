from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Flowers, Guide
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    categories = Category.objects.all()
    flowers = Flowers.objects.all()[:3]
    context = {
        'categories': categories,
        'flowers': flowers
    }


    return render(request, "./home.html", context)

def flowers_page(request):
    flowers = Flowers.objects.all()
    context = {
        'flowers': flowers
    }
    return render(request, "./flowers.html", context)

def category_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "./categories.html", context)

def guides_page(request):
    guides = Guide.objects.all()
    context = {
        'guides': guides
    }
    return render(request, "./guides.html", context)

def flowers_detail_page(request, pk):
    flowers = get_object_or_404(Flowers, pk=pk)
    context = {
        'flowers': flowers
    }
    return render(request, "./flowers-detail.html", context)

def guide_detail_page(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    context = {
        'guide': guide
    }
    return render(request, "./guide-detail.html", context)

def flowers_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    flowers = Flowers.objects.filter(category=category)
    context = {
        'category': category,
        'flowers': flowers
    }
    return render(request, "./flowers-by-category.html", context)


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')
