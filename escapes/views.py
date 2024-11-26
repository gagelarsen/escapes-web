from django.http import HttpResponse

def escapes_home(request):
    return HttpResponse('Welcome to Escapes!')
