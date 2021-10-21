from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

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
    return render(request, 'finches/detail.html', {'finch': finch})

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
