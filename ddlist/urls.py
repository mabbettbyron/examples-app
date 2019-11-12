from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ReadingListView.as_view(), name='reading_changelist'),
    path('add/', views.ReadingCreateView.as_view(), name='reading_add'),
    path('<int:pk>/', views.ReadingUpdateView.as_view(), name='reading_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-cities-readings/', views.load_cities_readings, name='ajax_load_readings'),
]
