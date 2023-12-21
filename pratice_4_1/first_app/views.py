from django.shortcuts import render
from . forms import ExampleForm
from . import models
def home(request):
    return render(request, 'Home.html')

def forms(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, 'Forms.html',{'form':form})

def models_view(request):
    models_ele = models.models_ele.objects.all()
    # print(models_ele)
    return render(request,"Models.html" , {"ele": models_ele})
# def models(request):
