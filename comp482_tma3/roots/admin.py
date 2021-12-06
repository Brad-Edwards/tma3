from django.contrib import admin

from . import forms, models

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    form = forms.ClassroomAdminForm


class AttendanceAdmin(admin.ModelAdmin):
    form = forms.AttendanceAdminForm
    filter_horizontal = ('children',)


class ContactInfoAdmin(admin.ModelAdmin):
    form = forms.ContactInfoAdminForm


admin.site.register(models.Classroom, ClassroomAdmin)
admin.site.register(models.Attendance, AttendanceAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
