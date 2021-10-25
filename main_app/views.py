from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Finch, Park, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'sei-finch-collector'

#Auth signup
def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('finches_index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Finch views
@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user) #display only users finches
    return render(request, 'finches/index.html', { 'finches': finches })

@login_required
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    park_finch_doesnt_have = Park.objects.exclude(id__in = finch.parks.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form, 
    'parks': park_finch_doesnt_have})

@login_required
def assoc_park(request, finch_id, park_id):
    Finch.objects.get(id=finch_id).parks.add(park_id)    
    return redirect('detail', finch_id=finch_id)
@login_required
def unassoc_park(request, finch_id, park_id):
    Finch.objects.get(id=finch_id).parks.remove(park_id)    
    return redirect('detail', finch_id=finch_id)

#add_feeding function
@login_required
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

@login_required
def add_photo(request, finch_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to finch_id or finch (if you have a finch object)
            photo = Photo(url=url, finch_id=finch_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', finch_id=finch_id)

class FinchCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = ['breed', 'description', 'size']
    # success_url = '/finches/'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class FinchUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url = '/finches/'


#Park views
class ParkList(LoginRequiredMixin, ListView):
    model = Park

class ParkDetail(LoginRequiredMixin, DetailView):
    model = Park

class ParkCreate(LoginRequiredMixin, CreateView):
    model = Park
    fields = '__all__'

class ParkUpdate(LoginRequiredMixin, UpdateView):
    model = Park
    fields = '__all__'

class ParkDelete(LoginRequiredMixin, DeleteView):
    model = Park
    success_url = '/parks/'



