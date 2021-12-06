from django.shortcuts import render

# Create your views here.
def attendance(request, attendance_id):
    return HttpResponse("You found attendance %s" % attendance_id)

def classroom(request, classroom_name):
    return HttpResponse("You found classroom %s" % classroom_name)
