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


class MenuAdmin(admin.ModelAdmin):
    form = forms.MenuAdminForm


class FoodAdmin(admin.ModelAdmin):
    form = forms.FoodAdminForm


admin.site.register(models.Classroom, ClassroomAdmin)
admin.site.register(models.Attendance, AttendanceAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Food, FoodAdmin)

