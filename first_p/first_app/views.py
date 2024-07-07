from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Accessrecord, Webpage
# Create your views here.
def index(request):
    Webpages_list = Accessrecord.objects.order_by('date')
    date_dict = {'access_records': Webpages_list}
    my_dict = {'insert_me': "Hello I am views.py from first App!"}
    return render(request, 'first_app/index.html', context=date_dict)