from django.shortcuts import render, redirect
from .forms import KeyInputForm
from .models import KeyInput, Club
from dj_chartjs.charts import BarChart
from django.views.generic import TemplateView

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

class ClubChartView(TemplateView):
    template_name = 'app/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Club.objects.all()
        return context
    
