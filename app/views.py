from django.shortcuts import render, redirect
from .forms import KeyInputForm
from .models import KeyInput

# Create your views here.
def Home(request):
    return render(request, 'app/home.html')

def KeyInput(request):
    form = KeyInputForm
    if request.method == 'POST':
        form = KeyInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'app/keyinput.html', {'form':form})

def Chart(request):
    return render(request, 'app/chart.html')