from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, "html_file/index.html", {
        "newyear": now.month == 1 and now.day == 11
    })
