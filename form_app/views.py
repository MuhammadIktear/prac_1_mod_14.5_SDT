from django.shortcuts import render, redirect
from .forms import ExampleForm

def home(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = ExampleForm()
    
    return render(request, 'home.html', {'form': form})
