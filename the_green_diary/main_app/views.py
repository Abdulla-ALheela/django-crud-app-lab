from django.views.generic.edit import CreateView
from .models import Plant,Watering
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import modelformset_factory
from .forms import WateringForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import PlantForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404



PlantFormSet = modelformset_factory(Plant, fields=('name',), extra=1)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def plant_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    waters = Watering.objects.filter(plant_id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant, 'waters': waters})  

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantForm 
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantForm 
    
    
class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

@login_required    
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('plant-detail', plant_id=plant_id)

class Home(LoginView):
    template_name = 'home.html'
 

def signup(request):
    error_message = ''
    if request.method == 'POST':
  
        form = UserCreationForm(request.POST)
        if form.is_valid():
        
            user = form.save()
      
            login(request, user)
            return redirect('plant-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

   
class WaterCreate(LoginRequiredMixin,CreateView):
    model = Watering
    form_class = WateringForm 
    
    def plant_detail(request, plant_id):
        plant = Plant.objects.get(id=plant_id)
        return render(request, 'watering_form.html', {'plant': plant,})
    
    def form_valid(self, form):
        plant_id = self.kwargs['plant_id']
        form.instance.plant = get_object_or_404(Plant, id=plant_id)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('plant-detail', kwargs={'plant_id': self.kwargs['plant_id']})

@login_required
def water_detail(request, plant_id, water_id):
    plant = Plant.objects.get(id=plant_id)
    water = Watering.objects.get(id=water_id)
    return render(request, 'main_app/water_detail.html', {'plant': plant, 'water': water})  

class WaterUpdate(LoginRequiredMixin,UpdateView):
    model = Watering
    form_class = WateringForm 
    
    def form_valid(self, form):
        plant_id = self.kwargs['plant_id']
        form.instance.plant = get_object_or_404(Plant, id=plant_id)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('water-detail', kwargs={
            'plant_id': self.kwargs['plant_id'],
            'water_id': self.object.id
     })

class WaterDelete(LoginRequiredMixin,DeleteView):
    model = Watering
    
    def get_success_url(self):
        plant_id = self.object.plant.id
        return reverse('plant-detail', kwargs={'plant_id': plant_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        water = self.get_object()
        context['plant'] = water.plant
        context['water'] = water
        return context