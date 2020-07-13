from django.shortcuts import render, redirect
from .forms import KeyInputForm
from .models import KeyInput
from dj_chartjs.charts import BarChart

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

