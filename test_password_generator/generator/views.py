from django.shortcuts import render

from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse('HELLO !')
    return render(request, 'generator/home.html', {'password': 'hui4DR1984'})
  
def nutz(request):
    return HttpResponse('<h3>HELLO Nutz !</h3>')

def password(request):
    # return render(request, 'generator/password.html', {'password': 'hui4DR1984'})
    # thepassword = 'NUtz'

    """CHARACTERS"""

    characters = list('abcdefghijklmnopqrstuvwxyz')

    # uppercase: home:form <input type="checkbox" name="uppercase">
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # special: home:form <input type="checkbox" name="special">
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    # numbers: home:form <input type="checkbox" name="numbers">
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    # length = 9
    # length: <select name="length" id="">
    length = int(request.GET.get('length', 9))

    """PASSWORD"""
    
    thepassword = ''
    for length in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')