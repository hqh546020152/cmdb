
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
#载入应用的models
from myapp import models
import time
import json


usrname = test
tty = models.DUser.objects.filter(user=(usrname))

print(tty)