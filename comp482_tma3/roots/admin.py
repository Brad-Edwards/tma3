from django.contrib import admin

from . import forms
from . import models

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    pass


class AttendanceAdmin(admin.ModelAdmin):
    form = forms.AttendanceAdminForm
    filter_horizontal = ('children',)


admin.site.register(models.Classroom, ClassroomAdmin)
admin.site.register(models.Attendance, AttendanceAdmin)
