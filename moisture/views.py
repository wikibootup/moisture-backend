from django.http import HttpResponse

from tasks import save_search

def search(request, text):
    save_search.delay(text)
    return HttpResponse(text)
