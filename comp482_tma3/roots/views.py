import datetime
from django import forms
from django.contrib import admin
from django.db import models
from django.contrib.admin import widgets as adminWidget
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.views.generic.edit import CreateView, FormView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from roots.models import Child, Classroom, ContactInfo, Family, Parent, Person, Registration
from roots.forms import CheckInForm, CheckOutForm, NapForm, RegisterChildForm, ToiletingForm

from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings

# Create your views here.
def attendance(request, attendance_id):
    return HttpResponse("You found attendance %s" % attendance_id)

def check_in(request):
    form = CheckInForm
    if request.method == 'POST':
        request.session['check_in_data'] = request.POST
        kids = request.POST.getlist('children')
        request.session['kids'] = kids
        return HttpResponseRedirect(reverse('roots:check_in_success'))

    return render(request, "roots/check_in.html", {'form': form})

def check_in_success(request):
    data = request.session.get('check_in_data', None)
    kids = request.session.get('kids', None)
    c = []
    if len(kids) == 1:
        c = kids
    else:
        kids.insert(len(kids) - 1, 'and')
        for kid in kids[:-2]:
            c.append(kid + ",")
        c.append(kids[-2])
        c.append(kids[-1])

    return render(request, "roots/check_in_success.html", {'data': data, 'kids': c})

def check_out(request):
    form = CheckOutForm
    if request.method == 'POST':
        request.session['check_out_data'] = request.POST
        kids = request.POST.getlist('children')
        request.session['kids'] = kids
        return HttpResponseRedirect(reverse('roots:check_out_success'))

    return render(request, "roots/check_out.html", {'form': form})

def check_out_success(request):
    data = request.session.get('check_out_data', None)
    kids = request.session.get('kids', None)
    c = []
    if len(kids) == 1:
        c = kids
    else:
        kids.insert(len(kids) - 1, 'and')
        for kid in kids[:-2]:
            c.append(kid + ",")
        c.append(kids[-2])
        c.append(kids[-1])

    return render(request, "roots/check_out_success.html", {'data': data, 'kids': c})

def children(request, child_id):
    return HttpResponse(f'You found child {child_id}')

def classroom(request, classroom_name):
    return HttpResponse("You found classroom %s" % classroom_name)

def contact_info(request, contact_info_id):
    return HttpResponse("You found contact info %s" % contact_info_id)

def families(request, family_id):
    return HttpResponse("You found family info %s" % family_id)

def food(request, food_id):
    return HttpResponse("You found food %s" % food_id)

def index(request):
    template = loader.get_template("roots/index.html")
    context = Context({'moo': "moo"})
    return HttpResponse(template.render(context, request))

def menu(request, menu_id):
    return HttpResponse("You found menu %s" % menu_id)

def meal(request, meal_id):
    return HttpResponse("You found meal %s" % meal_id)

def nap(request):
    form = NapForm
    if request.method == 'POST':
        request.session['nap_data'] = request.POST
        kids = request.POST.getlist('children')
        request.session['kids'] = kids
        return HttpResponseRedirect(reverse('roots:nap_success'))

    return render(request, "roots/nap.html", {'form': form})

def nap_success(request):
    data = request.session.get('nap_data', None)
    kids = request.session.get('kids', None)
    c = []
    if len(kids) == 1:
        c = kids
    else:
        kids.insert(len(kids) - 1, 'and')
        for kid in kids[:-2]:
            c.append(kid + ",")
        c.append(kids[-2])
        c.append(kids[-1])

    return render(request, "roots/nap_success.html", {'data': data, 'kids': c})

def parents(request, parent_id):
    return HttpResponse(f'You found parent {parent_id}')

def people(request, person_id):
    return HttpResponse(f'You found person {person_id}')


class DateInput(forms.DateInput):
    input_type = 'date'

def register(request):
    form = RegisterChildForm
    if request.method == 'POST':
        request.session['register_child_data'] = request.POST
        return HttpResponseRedirect(reverse('roots:register_success'))

    return render(request, "roots/register_form.html", {'form': form})

def register_success(request):
    data = request.session.get('register_child_data',  None)
    return render(request, "roots/register_success.html", {'data': data})

def registration(request, registration_id):
    return HttpResponse(f'You found {registration_id}')

def registration_landing(request):
    template = loader.get_template("roots/registration_landing.html")
    context = Context({'moo': "moo"})
    return HttpResponse(template.render(context, request))

def toileting(request):
    form = ToiletingForm
    if request.method == 'POST':
        request.session['toileting_data'] = request.POST
        kids = request.POST.getlist('children')
        request.session['kids'] = kids
        return HttpResponseRedirect(reverse('roots:toileting_success'))

    return render(request, "roots/toileting.html", {'form': form})

def toileting_success(request):
    data = request.session.get('toileting_data', None)
    kids = request.session.get('kids', None)
    c = []
    if len(kids) == 1:
        c = kids
    else:
        kids.insert(len(kids) - 1, 'and')
        for kid in kids[:-2]:
            c.append(kid + ",")
        c.append(kids[-2])
        c.append(kids[-1])

    return render(request, "roots/toileting_success.html", {'data': data, 'kids': c})

