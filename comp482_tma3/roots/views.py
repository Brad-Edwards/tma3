from django import forms as admin_forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader

from roots.forms import CheckInForm, CheckOutForm, NapForm, RegisterChildForm, ToiletingForm

from django.urls import reverse

# Create your views here.
def check_in(request):
    form = CheckInForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
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
    form = CheckOutForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
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

def index(request):
    template = loader.get_template("roots/index.html")
    context = Context({'moo': "moo"})
    return HttpResponse(template.render(context, request))

def nap(request):
    form = NapForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
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

class DateInput(admin_forms.DateInput):
    input_type = 'date'


def register(request):
    form = RegisterChildForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['register_child_data'] = request.POST
            return HttpResponseRedirect(reverse('roots:register_success'))

    return render(request, "roots/register_form.html", {'form': form})

def register_success(request):
    data = request.session.get('register_child_data',  None)
    return render(request, "roots/register_success.html", {'data': data})

def registration_landing(request):
    template = loader.get_template("roots/registration_landing.html")
    context = Context({'moo': "moo"})
    return HttpResponse(template.render(context, request))

def toileting(request):
    form = ToiletingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['toileting_data'] = request.POST
            kids = request.POST.getlist('children')
            request.session['kids'] = kids
            return HttpResponseRedirect(reverse('roots:toileting_success'))

    return render(request, "roots/check_in.html", {'form': form})

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
