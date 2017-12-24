from django.http import HttpResponse


def search(request, text):
    return HttpResponse(text)
