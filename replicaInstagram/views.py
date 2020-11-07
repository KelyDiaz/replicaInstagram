from datetime import datetime

from django.http import HttpResponse
import pdb

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, la fecha del servidor es: {now}'.format(now=now))

def hi(request):
    pdb.set_trace()
    return HttpResponse('Hi!')
