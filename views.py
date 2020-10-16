form django.http import HttpResponse
from django.shorcuts import redirect

def index(request):
    return HttpResponse('index')


def login(request):
    return redirect('/')
