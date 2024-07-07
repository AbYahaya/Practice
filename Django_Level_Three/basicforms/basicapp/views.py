from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

        else:
            print("Invalid form")

    else:
            form = forms.FormName()


    return render(request, 'basicapp/forms.html',{'form': form})