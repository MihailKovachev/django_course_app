from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Welcome!</h1>")