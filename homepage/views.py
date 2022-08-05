from django.shortcuts import render

# Create your views here.
names = [{'id': 1, 'name': 'Jane'}, {'id': 2, 'name': 'Don'}]
def home(request):
    context = {'names': names}
    return render(request, 'homepage/home.html', context)
def about(request):
    return render(request, 'homepage/about.html')