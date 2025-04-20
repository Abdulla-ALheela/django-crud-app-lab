from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Plant
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import modelformset_factory


PlantFormSet = modelformset_factory(Plant, fields=('name',), extra=1)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plant_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'
    

 

   


