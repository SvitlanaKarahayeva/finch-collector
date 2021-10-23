from django.shortcuts import render, redirect
from django.urls.base import is_valid_path
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Finch, Park
from .forms import FeedingForm

# class Finch:
#     def __init__(self, breed, description, size):
#         self.breed = breed
#         self.description = description
#         self.size = size

# finches= [
#     Finch('Evening Grosbeak', 'Adult male Evening Grosbeaks are yellow and black birds with a prominent white patch in the wings. They have dark heads with a bright-yellow stripe over the eye.', '16-18 cm'),
#     Finch('Gray-crowned Rosy-Finch', 'Adult males are rich brown suffused with pink on the body, with gray sides of the head and a black forecrown and throat. Adult females are similar but with less extensive pink. The bill is yellow.','14-21 cm')
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Finch views
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form})

#add_feeding function

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


#Park views
class ParkList(ListView):
    model = Park

class ParkDetail(DetailView):
    model = Park

class ParkCreate(CreateView):
    model = Park
    fields = '__all__'

class ParkUpdate(UpdateView):
    model = Park
    fields = '__all__'

class ParkDelete(DeleteView):
    model = Park
    success_url = '/parks/'