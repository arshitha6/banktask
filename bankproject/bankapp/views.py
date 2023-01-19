from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import PersonForm
from .models import Person, Branch
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('info')
        else:
            messages.info(request, "Incorrect Password")

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def logout(request):
    auth.logout(request)
    return redirect('/')


def personDetail(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pop_up.html")
    return render(request, 'person_detail.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'person_detail.html', {'form': form})


def load_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by()
    return render(request, 'branch_dropdown.html', {'branches': branches})


def infodata(request):
    return render(request, 'info.html')
def pop_up(request):
    return render(request, 'pop_up.html')