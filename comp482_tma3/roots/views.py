from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def attendance(request, attendance_id):
    return HttpResponse("You found attendance %s" % attendance_id)

def classroom(request, classroom_name):
    return HttpResponse("You found classroom %s" % classroom_name)

def contact_info(request, contact_info_id):
    return HttpResponse("You found contact info %s" % contact_info_id)

def menu(request, menu_id):
    return HttpResponse("You found menu %s" % menu_id)

def food(request, food_id):
    return HttpResponse("You found food %s" % food_id)
