from django.http import HttpResponse

def escapes_api_home(request):
    return HttpResponse('Welcome to Escapes API!')
