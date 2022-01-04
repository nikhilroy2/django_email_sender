from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def Mail_Index(request):
    # send mail working in shell but not in view, need to reasearch more about it
    send_mail('subject', 'msg', 'lizaape9@gmail.com', ['to_mail'])
    return render(request, 'index.html')
