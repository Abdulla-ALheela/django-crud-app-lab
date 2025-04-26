from django.urls import path, include
from . import views 

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plant_index, name='plant-index'),
  path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
  path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
  path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
  path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
  path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
  path('plants/<int:plant_id>/waters/create/', views.WaterCreate.as_view(), name='water-create'),
  path('plants/<int:plant_id>/waters/<int:water_id>/', views.water_detail, name='water-detail'),
  path('plants/<int:plant_id>/waters/<int:pk>/update/', views.WaterUpdate.as_view(), name='water-update'),
  path('plants/<int:plant_id>/waters/<int:pk>/delete/', views.WaterDelete.as_view(), name='water-delete'),
]

