from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

# Create your views here.
def attendance(request, attendance_id):
    return HttpResponse("You found attendance %s" % attendance_id)

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

def landing(request):
    template = loader.get_template("roots/index.html")
    context = Context({'moo': "moo"})
    return HttpResponse(template.render(context, request))

def menu(request, menu_id):
    return HttpResponse("You found menu %s" % menu_id)

def meal(request, meal_id):
    return HttpResponse("You found meal %s" % meal_id)

def nap(request, nap_id):
    return HttpResponse(f'You found nap {nap_id}')

def parents(request, parent_id):
    return HttpResponse(f'You found parent {parent_id}')

def people(request, person_id):
    return HttpResponse(f'You found person {person_id}')

def registration(request, registration_id):
    return HttpResponse(f'You found {registration_id}')

def toileting(request, toileting_id):
    return HttpResponse(f'You found toileting {toileting_id}')

