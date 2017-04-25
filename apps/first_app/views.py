
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, 'first_app/index.html', context)

def postresult(request):
    print Course.objects.all()
    if request.method == 'POST':
        if request.POST['add']:
            Course.objects.addcourse(request.POST)
            return redirect('/')

def remove(request):
    if request.method == 'POST':
        if request.POST['remove']:
            request.session['id'] = request.POST['id']
            request.session['name'] = request.POST['name']
            request.session['description'] = request.POST['description']
            return render(request, 'first_app/result.html')


def delete(request):
    if request.method == 'POST':
        if request.POST['remove']:
            id = request.session['id']
            Course.objects.removecourse(id)
    return redirect('/')

# def session_test_1(request):
#     request.session['test'] = 'Session Vars Worked!'
#     return http.HttpResponseRedirect('done/?session=%s' % request.session.session_key)
#
# def session_test_2(request):
#     return http.HttpResponse('<br>'.join([
#         request.session.session_key,
#         request.GET.get('session'),
#         request.session.get('test', 'Session is Borked :(')
#          ]))
