from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Reading, City
from .forms import ReadingForm

class ReadingListView(ListView):
    model = Reading
    context_object_name = 'readings'
    template_name = 'reading_list.html'

class ReadingCreateView(CreateView):
    model = Reading
    form_class = ReadingForm
    #fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('reading_changelist')
    template_name = 'reading_form.html'

class ReadingUpdateView(UpdateView):
    model = Reading
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('reading_changelist')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities':cities})

def load_cities_readings(request):
    city_id = request.GET.get('city')
    readings = Reading.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'city_reading_list.html', {'readings':readings})
