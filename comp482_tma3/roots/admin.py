from django.contrib import admin

from . import forms, models

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    form = forms.ClassroomAdminForm


class ChildAdmin(admin.ModelAdmin):
    form = forms.ChildAdminForm


class ContactInfoAdmin(admin.ModelAdmin):
    form = forms.ContactInfoAdminForm


class FoodAdmin(admin.ModelAdmin):
    form = forms.FoodAdminForm


class MealAdmin(admin.ModelAdmin):
    form = forms.MealAdminForm


class MenuAdmin(admin.ModelAdmin):
    form = forms.MenuAdminForm


class NapAdmin(admin.ModelAdmin):
    form = forms.NapAdminForm


class ParentAdmin(admin.ModelAdmin):
    form = forms.ParentAdminForm


class PersonAdmin(admin.ModelAdmin):
    form = forms.PersonAdminForm


class RegistrationAdmin(admin.ModelAdmin):
    form = forms.RegistrationAdminForm


class ToiletingAdmin(admin.ModelAdmin):
    form = forms.ToiletingAdminForm


admin.site.register(models.Child, ChildAdmin)
admin.site.register(models.Classroom, ClassroomAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
admin.site.register(models.Food, FoodAdmin)
admin.site.register(models.Meal, MealAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Nap, NapAdmin)
admin.site.register(models.Parent, ParentAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.Toileting, ToiletingAdmin)
