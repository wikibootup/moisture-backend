from django.http import HttpResponse

from tasks import save_search

def search(request, text):
    # @TODO - Apply celery server in docker process to run below a line
    # save_search.delay(text)
    save_search(text)
    return HttpResponse(text)
