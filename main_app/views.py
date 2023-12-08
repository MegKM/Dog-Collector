from django.shortcuts import render

dogs = [
  {'name': 'Watson', 'breed': 'Bull Arab', 'description': 'cuddle monster', 'age': 4},
  {'name': 'George', 'breed': 'Spoodle', 'description': 'fluffy', 'age': 6},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })
