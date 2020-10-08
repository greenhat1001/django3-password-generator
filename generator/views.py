from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
#def home(request):
    #return HttpResponse("Hello user!")
#def home(request):
    #return render(request, 'generator/home.html')


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    # first let's make a list with lowercase Characters
    lwcase_chars = list(string.ascii_lowercase)
    #Then let's check the conditions provided by the user in form
    # let's check if uppercase is True (checkbox 'uppercase' is on)
    if request.GET.get('uppercase'):
    # Second parameter True is optional.
    # If we don't have this parameter, we don't get passwors with Uppercase
    # chars by default when we try to access the password page directly:
    # http://127.0.0.1:8000/password/
        lwcase_chars.extend(list(string.ascii_uppercase))
    # list with uppercase chars bacomes a part of lwcase_chars list
    if request.GET.get('numbers'):
        lwcase_chars.extend(list(string.digits))
    if request.GET.get('special'):
        lwcase_chars.extend(list(string.punctuation))

    length = int(request.GET.get('length', 12))
    # Second parameter - 12 is default value in case of direct access to the
    #password page: http://127.0.0.1:8000/password/

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(lwcase_chars)

    return render(request, 'generator/password.html', {'password':thepassword})
    # Function return password.html page as part of http response.
    # {'password':thepassword}) passes data  {'password':thepassword} to
    # the password.html page
    # In order to display the data on the page, we need to put the name of
    # the key in html file (in any place) in this format {{ password }}
    # This will display the value of the key in html page.

def about(request):
    return render(request, 'generator/about.html')
