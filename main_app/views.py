from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Dog
from .forms import FeedingForm
from .models import Toy


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    toy_ids = dog.toys.all().values_list('id')
    available_toys = Toy.objects.exclude(id__in = toy_ids)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'feeding_form': feeding_form,
        'available_toys': available_toys
    })

def add_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id = dog_id) 

def remove_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.remove(toy_id)
  return redirect('detail', dog_id = dog_id)

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        feeding = form.save(commit = False)
        feeding.dog_id = dog_id
        feeding.save()
    return redirect('detail', dog_id = dog_id)

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields= '__all__'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'

class ToyList(ListView):
    model = Toy
    fields = '__all__'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields= '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'